
from fastapi import FastAPI, Form
from .Translator import Summary_brief
from typing import Annotated
app = FastAPI()

summarizer_model = Summary_brief()


class Summary_api:
    def __init__(self):
        pass

    @app.get("/")
    async def index():
        return {'Hello guys':'Welcome to the summarizer?'}

    @app.post("/translate")
    async def translate(paragraph: Annotated[str,  Form(...)]):
        text_summary = summarizer_model.summarize(paragraph)
        return  text_summary


if __name__=="__main__":
    translate_ = Summary_api()









