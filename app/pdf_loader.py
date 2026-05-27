from pypdf import PdfReader


def extractor(path:str)->str:
    reader=PdfReader(path)
    
    full_text=" "
    for page in reader.pages:
        text=page.extract_text()
        
        if text:
            full_text+= text + "/n"
            
    return full_text
def chunk_text(text, chunk_size=500, overlap=100):

    chunks = []

    start = 0
    chunk_id = 0

    while start < len(text):

        chunk = text[start:start + chunk_size]

        chunks.append({
            "id": chunk_id,
            "text": chunk
        })

        chunk_id += 1

        start += chunk_size - overlap

    return chunks
    