import logging

from pdf2image import convert_from_bytes
from pdftotext import PDF, Error as PDFError
from pytesseract import image_to_string

logger = logging.getLogger(__name__)


def pdf_to_string(f, password=None):
    logger.debug("converting pdf to text")

    f.seek(0)
    content = f.read()
    f.seek(0)

    try:
        pdf = PDF(f, password=password or "")
    except PDFError:
        raise ValueError("Wrong password or corrupt PDF file")

    for i, page in enumerate(pdf):
        if len(page) >= 10:
            logger.debug(f"using pdftotext for page {i + 1}")
            yield page.strip()
        else:
            logger.debug(f"using OCR for page {i + 1}")
            image = convert_from_bytes(
                content, size=1000, first_page=i + 1, last_page=i + 1, userpw=password
            )[0]
            text = image_to_string(image)
            if len(page) >= len(text):
                yield page.strip()
            else:
                yield text.strip()
