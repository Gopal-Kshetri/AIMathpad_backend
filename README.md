# AI Mathpad

## Instructions To Run This Project:
- Clone this repo, go into the root folder of this project and open a terminal.
- `python 3.9` is required in your environment.
- Run the command `pip install -r requirements.txt` to install all the requirements.
- Then start the fastapi server using the command `uvicorn main:app --reload`.
- Go to the url `127.0.0.1:8000` in your browser. (Check in the terminal the url where the server is listening)

## Documentation
- `main.py` contains the implementation of api routes in fastapi, including receiving uploaded image for prediction.
- `config.yaml` contains the configuration for the model used ([pix2tex](https://lukas-blecher.github.io/LaTeX-OCR/)).
- `models` contains the trained models.
- Dataset used for finetuning: [handwrittenmathsymbols](https://www.kaggle.com/datasets/xainano/handwrittenmathsymbols)
