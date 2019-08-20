import PyPDF2


class PDF_Doc():

    def __init__(self, filename):
        self.filename = filename
        self.display = filename.split('/')[-1]
        self.pdf = load_pdf(filename)
        self.pages = self.pdf.getNumPages()
        self.start = 1
        self.end = self.pages

    def add_to_writer(self, writer):
        for i in range(self.start-1, self.end):
            writer.addPage(self.pdf.getPage(i))


def load_pdf(filename):
    f = open(filename, 'rb')
    return PyPDF2.PdfFileReader(f)
