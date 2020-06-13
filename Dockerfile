FROM python:3.7

WORKDIR /app

COPY .. .

RUN apt-get update
RUN apt-get install allure -y
RUN pip install -U pip
RUN pip install -r requirements.txt;

CMD python3 -m pytest -s --selenoid=true --alluredir=allure-results