import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r'C:\\danyProject\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files (x86)\Tesseract-OCR\\tesseract.exe"

pdf_file = r"C:\\pdfFiles"
pages = convert_from_path(
    "C:\\pdfFiles\\test1.pdf", 500, poppler_path=r"C:\\danyProject\\poppler-0.68.0\\bin"
)
for i in range(len(pages)):
    image = pdf_file.split(".")[0] + str(i) + ".jpg"
    pages[i].save(image, "JPEG")
    t = pytesseract.image_to_string(Image.open(image), lang="fas")
    print(t)


# for pdf_file in os.listdir(r'C:\\pdfFiles\\'):
#      if pdf_file.endswith(".pdf"):
#          print(pdf_file)
#          pages = convert_from_path(pdf_file,500,poppler_path=r'C:\\danyProject\\poppler-0.68.0\\bin')
#          for i in range(len(pages)):
#              image=pdf_file.split('.')[0]+ str(i) + '.jpg'
#              pages[i].save(image,'JPEG')
#              t = pytesseract.image_to_string(Image.open(image),lang="fas")
#              print(t)
