from xml.etree import ElementTree
from helpers import isxml, ispdf, tmpfile, rmfile, has_cmd, run_cmd, getext, minzero
from globals import APP_CMD

__all__ = ['ParsePDF', 'ParsePDFConvertError', 'TXTSEP']

TXTSEP = '\n'


class ParsePDF:
    convert_cmd = 'pdftohtml'

    def __init__(self, path):
        if not has_cmd(self.convert_cmd):
            raise EnvironmentError('\'%s\' command is required' % self.convert_cmd)
        if not ispdf(path):
            raise FileNotFoundError('File not found or not PDF: %s' % path)
        self.pdf_file = path
        self.xml_file = ''
        self.pages = []
        self.__convert()
        self.__parse()

    @property
    def total_pages(self):
        return len(self.pages)

    def has_data(self):
        return len(self.pages) > 0

    def get_page(self, pagenum):
        assert self.has_data()
        index = minzero(pagenum - 1)
        return self.pages[index]

    def get_text(self):
        ret = []
        for index, page in enumerate(self.pages):
            ret.append('Page%s%s%s' % (index + 1, TXTSEP, page))
        return TXTSEP.join(ret).strip()

    def __parse(self):
        assert isxml(self.xml_file)
        tree = ElementTree.parse(self.xml_file)
        pages = tree.findall('page')
        for page in pages:
            self.pages.append(
                TXTSEP.join(getext(text).strip() for text in page.findall('text')).strip()
            )
        rmfile(self.xml_file)

    def __convert(self):
        self.xml_file = tmpfile(prefix=APP_CMD, suffix='.xml')
        cmd = '{} -c -i -hidden -xml {} {}'.format(self.convert_cmd, self.pdf_file, self.xml_file)
        if not run_cmd(cmd=cmd):
            rmfile(self.xml_file)
            raise ParsePDFConvertError('Unable to convert PDF file: %s' % self.pdf_file)


class ParsePDFConvertError(Exception):
    pass
