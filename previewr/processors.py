import logging
import time
from abc import abstractmethod
from previewr.utils import  get_resource_path

class Processor(object):
    """
        A processor is responsible to convert the source file into a html file.
    """
    def __init__(self, file_to_process, destionation_directory):
        self.file_to_process = file_to_process
        self.destination_directory = destionation_directory
        self.json_template = get_resource_path("templates/template.json")

    @abstractmethod
    def process(self):
        """
        Performs the effective conversion
        """
        pass

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

    def write(self, contents):
        """
        Writes the given string contents into a HTML file. This allows templating and automatic refreshing.
        """

        # Process HTML template
        replacements = {'filename': self.file_to_process, 'contents': contents}
        self._process_template(get_resource_path("templates/template.html"), self.destination_directory + '/index.html', replacements)

        # Process last refresh json
        replacements = {'date': str(time.time())}
        self._process_template(get_resource_path("templates/template.json"), self.destination_directory + '/last_refresh.json', replacements)

    @staticmethod
    def _process_template(template_file, output_file, replacements):
        # Read the template
        f = open(template_file, 'r')
        template = f.read()
        f.close()

        # Replace placeholders
        for (placeholder, replacement) in replacements.items():
            template = template.replace('${'+placeholder+'}', replacement)

        # Write to destination file
        f = open(output_file, 'w')
        f.write(template)
        f.close()

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

    def process(self):
        import markdown
        out = markdown.markdown(self.get_contents())
        self.write(out)

    def is_applicable(self):
        if self.get_file_extension() in ["md", "markdown"]:
            return True
        return False


class RstProcessor(Processor):
    """
        Processor specific for the restructuredText format
    """
    def process(self):
        try:
            from docutils import core
            out = core.publish_parts(self.get_contents(), writer_name="html")["html_body"]
            self.write(out)
        except Exception as e:
            print(e)
            self.write("Unexpected error:")

    def is_applicable(self):
        if self.get_file_extension() in ["rst"]:
            return True
        return False

# A list of all available processors
processors = [MarkdownProcessor, RstProcessor]


def select_applicable_processor(path, dst):
    """
    Selects a matching processor for the given file
    """
    for processor_cls in processors:
        instance = processor_cls(path, dst)
        if instance.is_applicable():
            logging.debug("Using processor %s" % processor_cls.__name__)
            return instance

    raise Exception("No processor found for the given file!")