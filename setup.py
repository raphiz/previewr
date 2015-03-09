import os
import sys
from distutils.core import setup

README = open('README.rst').read()
VERSION = '0.2.0'


def read(file_name):
    abs_file_name = os.path.join(os.path.dirname(__file__), file_name)
    with open(abs_file_name) as file:
        return file.read()


setup(
    version = VERSION,
    include_package_data=True,
    tests_require = read('test_requirements.txt'),

    download_url = "https://github.com/raphiz/previewr/archive/" + VERSION + ".zip",
    keywords = ["preview", "markdown", "rst", "md", "restructuredText"],
    
)
