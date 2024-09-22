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
1. `pip install -r requirements.txt`
1. Download Navec model
```shell 
cd emb_models
wget https://storage.yandexcloud.net/natasha-navec/packs/navec_hudlit_v1_12B_500K_300d_100q.tar
```
4. Make sure you have the models listed in config.ini. so for nomic-embed-text, run:
```shell 
ollama pull nomic-embed-text
```
  Update the config to show whatever models you want to use.
5. Run ChromaDB in a separate terminal:
```shell
chroma run --host localhost --port 8000 --path ./vectordb-stores/chromadb
```
6. Put reference txt docs to a folder *knowledge* .
1. Edit the list of docs in `sourcedocs.txt`
1. If reference data was updated, update embeddings of reference docs in the Chroma DB:
```shell
python3 aborag-gen-ref.py
```
9. Run console chat with Assistant:
```shell
python3 aborag-cli.py
```

