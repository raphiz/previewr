from previewr.utils import *
from previewr.processors import *
from previewr.server import serve
from optparse import OptionParser
import logging
import tempfile
import os
import shutil


def main():

    (options, args) = parse_cli_parameters()

    # Set log level and formatting
    level = (logging.DEBUG if options.debug else logging.INFO)
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s',)

    # Get absolute path of the source file
    file_to_preview = os.path.abspath(args[0])

    # Make a temporary directory to store the result into
    directory = tempfile.mkdtemp()
    logging.debug("temporary directory is: '%s'" % directory)

    # Copy static resources....
    shutil.copytree(get_resource_path('static'), directory+'/static')

    processor = select_applicable_processor(file_to_preview, directory)
    poller = FilePoller(file_to_preview, processor)
    scheduler = Scheduler(0.25, poller.poll)

    try:
        scheduler.start()
        serve(directory)
    except KeyboardInterrupt:
        scheduler.stop()


def parse_cli_parameters():
    parser = OptionParser()
    parser.add_option("-d", "--debug", dest="debug",
                      action="store_true",
                      help="Enables debug output")
    return parser.parse_args()

if __name__ == "__main__":
    main()
