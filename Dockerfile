FROM python:3.11-slim-buster

WORKDIR /app

COPY dev_requirements.txt .

RUN pip3 install  -r dev_requirements.txt
RUN pip3 install  transformers

COPY . .

CMD ["fastapi", "run", "Translator_endpoint.py"]