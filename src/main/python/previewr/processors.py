import logging
from previewr import utils
from abc import abstractmethod
from docutils import core
from docutils.parsers.rst import directives


class Processor(object):

    name = "unknown"

    """
        A processor is responsible to convert the source file into a html file.
    """
    def __init__(self, file_to_process):
        self.file_to_process = file_to_process

    @abstractmethod
    def process(self):
        """
        Performs the effective conversion and returns the result
        """
        return ""

    @abstractmethod
    def is_applicable(self):
        """
        Returns true if the current processor can be applied for the current file
        (eg. by using the get_file_extension method).
        """
        pass

    def get_file_extension(self):
        """
        Utility method to access the file extension of the file with which the class was instantiated
        """
        return self.file_to_process.split(".")[-1]

    def get_contents(self):
        """
        Returns the contents of the source file
        """
        f = open(self.file_to_process, 'r')
        contents = f.read()
        f.close()
        return contents


class MarkdownProcessor(Processor):
    """
        Processor specific for the markdown format.
    """
    name = "markdown"

    def process(self):
        import markdown
        return markdown.markdown(self.get_contents())

    def is_applicable(self):
        if self.get_file_extension() in ["md", "markdown"]:
            return True
        return False


class RstProcessor(Processor):
    """
        Processor specific for the restructuredText format
    """

    name = "rst"

    def process(self):
        directives.register_directive('code', utils.Pygments)
        directives.register_directive('sourcecode', utils.Pygments)
        return core.publish_parts(self.get_contents(), writer_name="html")["html_body"]

    def is_applicable(self):
        if self.get_file_extension() in ["rst"]:
            return True
        return False


class Processors:
    """
    A utility class providing methods to access all processors.
    """

    # A list of all available processors
    processors = [MarkdownProcessor, RstProcessor]

    @classmethod
    def processor_names(cls):
        """
        Returns a list of all available processor names/
        """
        values = []
        for processor in cls.processors:
            values.append(processor.name)
        return values

    @classmethod
    def get_processor_by_name(cls, name):
        """
        Returns the processor with the given name (first match, first win).
        If none is found, None is returned.
        """
        for processor in cls.processors:
            if processor.name == name:
                return processor
        return None

    @classmethod
    def select_applicable_processor(cls, file_to_process):
        """
        Selects a matching processor for the given file
        """
        for processor_cls in cls.processors:
            instance = processor_cls(file_to_process)
            if instance.is_applicable():
                logging.debug("Using processor %s" % processor_cls.__name__)
                return processor_cls

        raise Exception("No processor found for the given file!")
