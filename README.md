# Medical-Chatbot-Using-Llama2
This version of Medical Chatbot utilizes use of [Pinecone](https://www.pinecone.io/) for vector storage and uses Meta's LLM [LLAMA-2](https://llama.meta.com/llama2/). The UI is made on Flask Server.


## Create a virtual env (ubuntu)
``` bash
    python3 -m venv mchatbot
```

## Activate it
```bash
    source mchatbot/bin/activate
```

## Install dependencies

```bash
    pip install -r requirements.txt
```

To check all the dependencies have been installed, run after creating a `test_installation.py` file
```bash
    python test_installation.py
```