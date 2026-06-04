import chromadb
from pathlib import Path

file_path = Path("notes.txt")

file_path.write_text("""
Python is widely used in machine learning.

AWS provides cloud computing services.

Vector databases store embeddings.

Cricket is a popular sport in India.

RAG combines retrieval and generation.
""")

print("File created!")

with open ("notes.txt","r") as f:
    text = f.read()

chunks = [chunk.strip()for chunk in text.split("\n\n")if chunk.strip()]    

print (chunks)

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

print(embeddings.shape)


client = chromadb.Client()

collection = client.create_collection("Notes")

for i,chunk in enumerate(chunks):
    collection.add(
        documents = [chunk],
        ids = [str(i)]
    )


while True:
    query = input("Ask: ")

    results = collection.query(
        query_texts=[query],
        n_results=2
    )

    print("\nRetrieved:\n")

    for doc in results["documents"][0]:
        print("-", doc)

    print()
    

