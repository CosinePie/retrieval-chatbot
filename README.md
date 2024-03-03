# End-to-end-RAG-Chatbot

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```

### STEP 1- Create a conda environment after opening the repository

```bash
conda create -n rag-chatbot
```

```bash
conda activate rag-chatbot
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your OpenAI credentials as follows:

```ini
API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- OpenAI
- FAISS