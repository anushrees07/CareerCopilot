from pathlib import Path

import fitz  # PyMuPDF
from docx import Document


def extract_text(uploaded_file):
    """
    Extract text from PDF or DOCX uploaded through Streamlit.
    """

    if uploaded_file is None:
        return ""

    extension = Path(uploaded_file.name).suffix.lower()

    # -------------------------
    # PDF
    # -------------------------
    if extension == ".pdf":

        try:

            pdf_bytes = uploaded_file.read()

            document = fitz.open(stream=pdf_bytes, filetype="pdf")

            text = ""

            for page in document:
                text += page.get_text()

            document.close()

            uploaded_file.seek(0)

            return text.strip()

        except Exception as e:

            raise Exception(f"Unable to read PDF:\n{e}")

    # -------------------------
    # DOCX
    # -------------------------
    elif extension == ".docx":

        try:

            document = Document(uploaded_file)

            text = "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
                if paragraph.text.strip()
            )

            uploaded_file.seek(0)

            return text.strip()

        except Exception as e:

            raise Exception(f"Unable to read DOCX:\n{e}")

    # -------------------------
    # Unsupported
    # -------------------------
    else:

        raise ValueError(
            "Unsupported file format. Please upload a PDF or DOCX file."
        )