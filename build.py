from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("copy_resources")

name = "previewr"
default_task = "publish"

summary = "Simple Markdown/reStructured Text previewer"
authors = [Author("Raphael Zimmermann", "mister.norbert@gmail.com")]
description = open('README.rst').read()
license = "MIT"
url = "http://raphael.li/projects/previewr/"
version = "0.4.0.dev"


@init
def set_properties(project):
    # Scripts directory
    project.set_property("distutils_console_scripts", ["previewr = previewr:main"])

    project.include_file('previewr', 'templates/*')
    project.include_file('previewr', 'static/*')

    # Also builde resources
    project.set_property("copy_resources_target", "$dir_dist/previewr")
    project.set_property("copy_resources_glob", ['static/*', 'templates/*'])

    project.set_property("distutils_classifiers", [
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
    ])

    # Don't break the build for covarage
    project.set_property('coverage_break_build', False)

    # Dependencies from requirements.txt
    project.depends_on_requirements("requirements.txt")
