import logging

from pdf2image import convert_from_bytes
from pdftotext import PDF
from pytesseract import image_to_string

logger = logging.getLogger(__name__)


def pdf_to_string(f):
    logger.debug("converting pdf to text")

    f.seek(0)
    content = f.read()
    f.seek(0)

    for i, page in enumerate(PDF(f)):
        if len(page) >= 10:
            logger.debug(f"using pdftotext for page {i + 1}")
            yield page.strip()
        else:
            logger.debug(f"using OCR for page {i + 1}")
            image = convert_from_bytes(
                content, size=1000, first_page=i + 1, last_page=i + 1
            )[0]
            text = image_to_string(image)
            if len(page) >= len(text):
                yield page.strip()
            else:
                yield text.strip()
