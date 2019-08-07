FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /ssharma
WORKDIR /ssharma
COPY  requirements.txt /ssharma/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /ssharma/

