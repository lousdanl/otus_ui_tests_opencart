FROM python:3.7

WORKDIR /app

COPY . .

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install allure -y
RUN pip install -U pip
RUN --mount=type=cache,target=/home/root/.cache/pip pip3 install -r requirements.txt;

CMD python3 -m pytest -s --alluredir=/app/allure-reports