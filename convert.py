from pdf2image import convert_from_bytes
from pytesseract import image_to_string


def pdf_to_string(content: bytes):
    images = convert_from_bytes(content)
    texts = [image_to_string(img) for img in images]
    return "\n\n".join(texts).strip()
