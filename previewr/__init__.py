from previewr.server import *
from tornado.options import define


def main():
    """
        Runs the module.
    """

    # Setup CLI parameters
    define("port", default=8000, help="run on the given port", type=int)
    define("format", default="auto",
           help="The format to enforce. Possible values are: " + ", ".join(Processors.processor_names()))

    # Setup logging
    level = logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s',)
    access_log = logging.getLogger("tornado.access")
    access_log.setLevel(logging.WARNING)

    # Launch the app
    app = Application()
    try:
        app.serve()
    except KeyboardInterrupt:
        app.shutdown()

if __name__ == "__main__":
    main()