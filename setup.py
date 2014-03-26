from distutils.core import setup

README = open('README.rst').read()

setup(
    name = "previewr",
    packages = ["previewr"],
    package_data = {
       "previewr": [
            "templates/*",
            "static/*"],
    },
    version = "0.0.1",
    license = "MIT",
    include_package_data=True,
    zip_safe=False,
    install_requires= [ 'markdown', 'docutils'],
    entry_points = {
        'console_scripts': [
            'previewr = previewr:main']
    },
    description = "Simple markdonw/reStructured Text previewer",
    author = "Raphael Zimmermann",
    author_email = "mister.norbert@gmail.com",
    url = "https://github.com/raphiz/previewr",
    download_url = "https://github.com/raphiz/previewr/archive/master.zip",
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
    long_description=README
)