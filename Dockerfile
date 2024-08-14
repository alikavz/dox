FROM python:3.9

ENV PYHTONDONTWRITTEBYTECODE 1
ENV PYTHONUBUFFERED 1

WORKDIR /codes

COPY requirements.txt /codes/
RUN pip install -r requirements.txt

COPY . /codes/
