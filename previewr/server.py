from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer
import os
import logging


def serve(directory, port=8000):
    os.chdir(directory)
    httpd = HTTPServer(('', port), SpecificHTTPRequestHandler)
    logging.info("Running at localhost:%s" % port)
    httpd.serve_forever()


class SpecificHTTPRequestHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.debug("%s - - [%s] %s" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format % args))