Overview
========
Previewr provides you a continuous preview of your Markdown_ and reStructuredText_ files in your favourite web browser.
You need nothing else than python  a web browser installed. It works with every editor.

And here is how you use it:

.. code:: bash

    $ previewr hello-world.rst

After running the command open `<http://localhost:8000/>`_ in the browser. You will now see a fancy preview of your document. If you make further changes to your document, the page will automatically refresh.


Why another tool?
------------------
You might think now, that there are some editors out there that have this preview integrated or that there are some other tools out there that do almost the same. This is true, but what makes previewr unique is that it allows you to stay in you favourite editor that might not support a preview out of the box. All you need is python installed on your computer and any modern web browser.

How it works
------------
Initially, the given file is processed (with the Markdown_ or the reStructuredText_ processor) and therefore converted into HTML. This HTML is then served with a minimal web server (Powered by the Tornado_ framework).
In the background, previewr observes the given file for changes. If the modification date changes, the contents are processed again and sent to the client (the web browser) using WebSockets.


What's missing?
---------------
Previewr currently only supports a very basic subset of all possible style outputs.


Installation
============
Just run:

.. code:: bash

    $ pip install previewr

or using *easy_install*:

.. code:: bash

    $ easy_install previewr

Note that previewr is written in python3, so you might have to run pip3 if pip points to pip2. Same applies to easy_install.

Root permissions might also be required for the installation.

Usage
==========
Usage: /usr/bin/previewr [OPTIONS] file

Options:

  --format      The format to enforce. Possible values are:
                markdown, rst (default auto)
  --help        show help information
  --port        run on the given port (default 8000)

Arguments:

  file          The file to preview

Here an example:

.. code:: bash

    $ previewr --port=8443 --format=markdown example.markdown

Changelog
=========
0.4.0
-----
* Support Fenced code blocks in markdown
* Syntax highlighting in markdown

0.3.0
-----
* Template improved (now using mistype.css)
* Pygments support added
* Migrated project to pybuilder

0.1.0
-----
* Rewrite of most components
* Migration to the Tornado_ Framework to make use of WebSockets and to make the code cleaner.
* Template improved / Table of contents added
* Port and processors can now be specified using the command line
* other small fixes

0.0.1
-----
* Initial Release

Roadmap
=======
These things should be done next:

* Provide a plugin mechanism for more processors
* Improve documentation
* Write unit tests
* Provide multiple themes
* Specific style for printing

Do you have another idea what has to be done next? Don't hesitate to suggest it using the `Github issue tracker <https://github.com/raphiz/previewr/issues>`_.!

Contribute
==========
Feel free to submit any pull requests or just file an Issue!
If anything is unclear, annoying or anything else let me know, feedback is always welcome.


License
=======
Previewr licensed under the MIT_ license.


Attribution
===========
* Favicon is by Sergio Sánchez López, found via `IconFinder <https://www.iconfinder.com/icons/7680/adept_magnifying_glass_preview_icon>`_.
* CSS template is based on the `Mistype <http://zdroid.roon.io/mistype>`_.
* Syntax highlighting powerd by `Pygments <http://pygments.org/>`_.
* Markdown_ processing is powered by `markdown <https://pythonhosted.org/Markdown/>`_.
* reStructuredText_ processing is powered by the `python docutils library <https://pypi.python.org/pypi/docutils>`_.
* JQuery_
* Table of contents JavaScript powered by the `TOC jQuery plugin <http://projects.jga.me/toc/>`_.


.. _JQuery: http://jquery.com/
.. _MIT: http://opensource.org/licenses/MIT
.. _Markdown: http://daringfireball.net/projects/markdown/syntax
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Tornado: http://www.tornadoweb.org/
