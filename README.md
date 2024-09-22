# aborag
AI assistant based on RAG (english, russian)
# Assistant based on RAG
This project based on project **Build RAG with Python**
https://github.com/technovangelist/videoprojects.git
lesson 2024-04-04-build-rag-with-python

What's changed:
1. Added Natasha (https://github.com/natasha/navec)  embeddings model for Russian reference data.
2. Mane model replaced from gemma:2b to llama3.1
3. Application configuration management reimlemented on config package.
4. Remove content download from Web. 
5. Added directory with reference data (in Russian) about bike Suzuki Djebel 200. 



## Installation:
1. `sudo apt-get install libmagic1`  
2. `pip install -r requirements.txt`
3. Make sure you have the models listed in config.ini. so for nomic-embed-text, run `ollama pull nomic-embed-text`. Update the config to show whatever models you want to use.
4. Run ChromaDB in a separate terminal: `chroma run --host localhost --port 8000 --path ./vectordb-stores/chromadb`
5. Put reference txt docs to *knowledge* folder.
5. Edit the list of docs in `sourcedocs.txt`
6. If reference data was updated, update embeddings for reference docs in Chroma DB: `python3 import.py`
7. Run console chat with Assistant: `python3 simple_cli.py`

