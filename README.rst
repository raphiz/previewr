Overview
========
Previewer provides you a preview of your markdown and reSturcturedText files in your preferred browser. It runs completely independent
of the browser.

So here is how you use it:

    previewr hello-world.rst

And now open  `<http://localhost:8000/>`_. You can now edit you markdown file and after saving it,
it will be automatically refreshed (it might take 2 seconds)
Please note that I just wrote this tool in one Afternoon, therefore many functionality as well as unit tests are missing.\
However, it works so far (on my machine :) ) and I'm open for feedback and pull requests!
Additionally, Python is not my "native" (primary) programming language. So  if I could improve stuff, please let me know!

Why another toool?
------------------
Many tools provide almost the same or even more functionality. However, I don't want to use for each language another tool,
for example when I write my software in VI, why should I use another editor to preview my markdown/reSt documents?
That's basically why I wrote this tool.

Installation
============
Just run:

    pip previewr


Roadmap
==================

The following things have to be done next:

* Allow user to select the file processor with a option parameter
* Provide a plugin mechanism for more processors
* Improve documentation
* Write unit tests
* Use Websockets
* allow to change the port
* Bootstrap stuff shall be included using submodules

Contribute
==========
Feel free to submit any pull requests or just file an Issue!
If anything is unclear or annoying, let me know!


License
=======
Everything is under MIT license!