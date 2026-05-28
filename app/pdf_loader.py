from pypdf import PdfReader


def extractor(path):

    reader = PdfReader(path)

    pages = []

    for i, page in enumerate(reader.pages):

        text = page.extract_text()

        pages.append({
            "page": i + 1,
            "text": text
        })

    return pages
def chunk_text(pages, chunk_size=500, overlap=100):

    chunks = []

    chunk_id = 0

    for page_data in pages:

        page_number = page_data["page"]

        text = page_data["text"]

        start = 0

        while start < len(text):

            chunk = text[start:start + chunk_size]

            chunks.append({
                "text": chunk,
                "page": page_number,
                "chunk_id": chunk_id
            })

            chunk_id += 1

            start += chunk_size - overlap

    return chunks