import PyPDF2

class PDFtoText():
    def __init__(self):
        self.the_pdf=""
        self.the_txt=""
        self.the_text=""

    def convert_pdf_to_text(self):
        try:
            pdffileobj = open(self.the_pdf, 'rb')
            # create reader variable that will read the pdffileobj
            pdfreader = PyPDF2.PdfFileReader(pdffileobj)
        except FileNotFoundError as error:
            print(f"OAMA-{error}")
            exit(-1)

        try:
            with open(self.the_txt,'w',encoding = 'utf-8') as f:
                for page in range(0,pdfreader.numPages-1):
                    pageobj = pdfreader.getPage(page)
                    pdf_text = pageobj.extractText()
                    f.writelines(pdf_text)
                    self.the_text=self.the_text+pdf_text
            f.close()

        except NameError as error:
            print(f"OAMA-{error}")
            exit(-1)

#x = pdfreader.numPages
# create a variable that will select the selected number of pages
#pageobj = pdfreader.getPage(x-1)
#pdf_text = pageobj.extractText()
