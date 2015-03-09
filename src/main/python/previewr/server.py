from previewr.utils import *
from previewr.processors import *
from tornado.web import StaticFileHandler

import logging
import os.path
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket

from tornado.options import options


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )

        handlers = [
            (r"/", MainHandler),
            (r"/update", UpdateSocketHandler),
            (r"/(.*)", StaticFileHandler, {"path": os.getcwd()}),
        ]
        # Get the file to preview from the CLI parameters...
        args = tornado.options.parse_command_line()
        # Verify the argument is present!
        if len(args) != 1:
            print("You must provide exactly one file to preview")
            exit(1)

        self.file_to_preview = os.path.abspath(args[0])

        # Initialize the poller and scheduler
        self.processor = self._get_processor()(self.file_to_preview)
        self.poller = FilePoller(self.file_to_preview, self.update_client_html)
        self.scheduler = Scheduler(0.25, self.poller.poll)

        # Call parent constructor
        tornado.web.Application.__init__(self, handlers, **settings)

    def _get_processor(self):
        """
        Selects the processor to use and returns it.
        """
        processor_name = options.format
        if processor_name == "auto":
            return Processors.select_applicable_processor(self.file_to_preview)

        processor = Processors.get_processor_by_name(processor_name)
        if processor is None:
            raise Exception("No Processor called %s" % processor_name)
        return processor

    def serve(self):
        """
        Starts to serve the application.
        """
        self.listen(options.port)
        self.scheduler.start()
        logging.info("Running at http://localhost:%s" % options.port)
        tornado.ioloop.IOLoop.instance().start()

    def shutdown(self):
        """
        Shuts down the application
        """
        self.scheduler.stop()

    def update_client_html(self):
        """
        This method does re-process the file to watch and updates all clients.
        """
        res = self.processor.process()
        UpdateSocketHandler.notify_clients(res)


class MainHandler(tornado.web.RequestHandler):
    """
    Main RequestHandler to send the index to the client.
    """
    def get(self):
        self.render("index.html",
                    contents=self.application.processor.process(),
                    filename=self.application.file_to_preview)


class MainResourceHandler(tornado.web.RequestHandler):
    """
    Main RequestHandler to send the index to the client.
    """
    def get(self, a):
        print(a)


class UpdateSocketHandler(tornado.websocket.WebSocketHandler):
    """
    WebSocket Handler to allow server push if the file to observe has changed.

    Attributes:
        clients     All clients to notify when the file has changed

    """
    clients = set()

    def allow_draft76(self):
        # for iOS 5.0 Safari
        return True

    def open(self):
        logging.debug("New connection opened")
        UpdateSocketHandler.clients.add(self)

    def on_close(self):
        logging.debug("Connection closed to a waiter")
        UpdateSocketHandler.clients.remove(self)

    @classmethod
    def notify_clients(cls, msg):
        """
        Sends the given HTML message to all registered clients.
        """
        logging.debug("sending update broadcast to %d waiters", len(cls.clients))
        for client in cls.clients:
            try:
                client.write_message(msg)
            except:
                logging.error("Error sending message", exc_info=True)
