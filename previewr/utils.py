from threading import Timer
import time
import os
import logging


class Scheduler(object):
    """
    The scheduler class allows to execute a task in regular intervals
    """

    def __init__(self, interval, function):
        self._timer = None
        self.function = function
        self.interval = interval
        self.is_running = False

    def _run(self):
        # Execute
        self.function()

        # Reschedule
        if self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()



    def start(self):
        """
        Starts the scheduled task.
        """
        if not self.is_running:
            self.is_running = True
            self._run()


    def stop(self):
        """
        Stops the scheduled task
        """
        logging.debug("Stopping scheduler")
        self._timer.cancel()
        self.is_running = False


class FilePoller(object):
    """
    This class is responsible to poll a certain file and call a "processor" if it has changed.
    """

    def __init__(self, path, processor):
        self.path = path
        self.processor = processor
        self.modification_timestamp = self._fetch_modification_timestamp()

        self.processor.process()

    def poll(self):
        """
        The effective poll method to be called regularly
        """
        date = self._fetch_modification_timestamp()
        logging.debug("Timestamp for file '%s' is '%s'" % (self.path, str(date)))

        if self.modification_timestamp != date:
            logging.info("File change detected on file '%s'" % self.path)
            self.processor.process()
            self.modification_timestamp = date

    def _fetch_modification_timestamp(self):
        """
        Fetches the last modification timestamp from the file to poll and returns it.
        """
        return time.ctime(os.path.getmtime(self.path))


def get_resource_path(project_relative_path):
    return os.path.join(os.path.split(__file__)[0], project_relative_path)