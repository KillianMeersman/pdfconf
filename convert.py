from pdf2image import convert_from_bytes
from pdftotext import PDF
from pytesseract import image_to_string
import logging

logger = logging.getLogger(__name__)


def pdf_to_string(f):
    logger.debug("converting pdf to text")

    f.seek(0)
    images = convert_from_bytes(f.read())
    f.seek(0)

    for i, page in enumerate(PDF(f)):
        if len(page) >= 10:
            logger.debug(f"using pdftotext for page {i}")
            yield page
        else:
            logger.debug(f"using OCR for page {i}")
            yield image_to_string(images[i])
