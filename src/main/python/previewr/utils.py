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

    def __init__(self, path, observer):
        self.path = path
        self.observer = observer
        self.modification_timestamp = self._fetch_modification_timestamp()

        self.observer()

    def poll(self):
        """
        The effective poll method to be called regularly
        """
        date = self._fetch_modification_timestamp()
        logging.debug("Timestamp for file '%s' is '%s'" % (self.path, str(date)))

        if self.modification_timestamp != date:
            logging.info("File change detected on file '%s'" % self.path)
            self.observer()
            self.modification_timestamp = date

    def _fetch_modification_timestamp(self):
        """
        Fetches the last modification timestamp from the file to poll and returns it.
        """
        return time.ctime(os.path.getmtime(self.path))


# -*- coding: utf-8 -*-
"""
    The Pygments reStructuredText directive
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This fragment is a Docutils_ 0.5 directive that renders source code
    (to HTML only, currently) via Pygments.

    To use it, adjust the options below and copy the code into a module
    that you import on initialization.  The code then automatically
    registers a ``sourcecode`` directive that you can use instead of
    normal code blocks like this::

        .. sourcecode:: python

            My code goes here.

    If you want to have different code styles, e.g. one with line numbers
    and one without, add formatters with their names in the VARIANTS dict
    below.  You can invoke them instead of the DEFAULT one by using a
    directive option::

        .. sourcecode:: python
            :linenos:

            My code goes here.

    Look at the `directive documentation`_ to get all the gory details.

    .. _Docutils: http://docutils.sf.net/
    .. _directive documentation:
       http://docutils.sourceforge.net/docs/howto/rst-directives.html

    :copyright: Copyright 2006-2010 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

# Options
# ~~~~~~~

# Set to True if you want inline CSS styles instead of classes
INLINESTYLES = False

from pygments.formatters import HtmlFormatter

# The default formatter
DEFAULT = HtmlFormatter(noclasses=INLINESTYLES)

# Add name -> formatter pairs for every variant you want to use
VARIANTS = {
    # 'linenos': HtmlFormatter(noclasses=INLINESTYLES, linenos=True),
}


from docutils import nodes
from docutils.parsers.rst import directives, Directive

from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer

class Pygments(Directive):
    """ Source code syntax hightlighting.
    """
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = dict([(key, directives.flag) for key in VARIANTS])
    has_content = True

    def run(self):
        self.assert_has_content()
        try:
            lexer = get_lexer_by_name(self.arguments[0])
        except ValueError:
            # no lexer found - use the text one instead of an exception
            lexer = TextLexer()
        # take an arbitrary option if more than one is given
        formatter = self.options and VARIANTS[self.options.keys()[0]] or DEFAULT
        parsed = highlight(u'\n'.join(self.content), lexer, formatter)
        return [nodes.raw('', parsed, format='html')]
