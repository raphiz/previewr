from distutils.core import setup
setup(
    name = "previewr",
    packages = ["previewr"],
    version = "0.0.1",
    description = "Simple markdonw/reStructured Text previewer",
    author = "Raphael Zimmermann",
    author_email = "mister.norbert@gmail.com",
    url = "http://github.com/raphiz/previewr",
    download_url = "http://github.com/raphiz/previewr ... .tgz",
    keywords = ["preview", "markdown", "rst", "md", "restructuredText"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ],
    long_description = """\
Previewr -  a simple preview tool
-------------------------------------

Previewer provides you a preview of your markdown and reSturcturedText files in your preferred browser. It runs completely independent
of the browser.

This version requires Python 3 or later
"""
)