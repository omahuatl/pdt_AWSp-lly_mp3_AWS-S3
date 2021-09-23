"""Getting Started Example for Python 2.7+/3.3+
https://docs.aws.amazon.com/polly/latest/dg/what-is.html
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.synthesize_speech
"""
from AWSpolly import AWSpolly
from PDFtoTxt import PDFtoText

new_speach = AWSpolly()
a_pdf = PDFtoText()
a_pdf.the_pdf = "libro-la-gran-victoria-mexica-la-noche-triste-del-conquistador-INPI.pdf"
a_pdf.the_txt = "texto.txt"
a_pdf.convert_pdf_to_text()

new_speach.long_text_to_mp3(a_pdf.the_text)
#new_speach.text_to_mp3("esta es una clase", "unMP3.mp3")
#new_speach.hear_result()
