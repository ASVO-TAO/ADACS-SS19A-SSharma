FROM python:3.6
ENV PYTHONUNBUFFERED 1

WORKDIR / code
RUN mkdir /code
WORKDIR /code
COPY  requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/


WORKDIR /code/galaxia
RUN tar -zxvf galaxia-0.8.1.tar.gz
WORKDIR galaxia-0.8.1
RUN ./configure --datadir=/GalaxiaData
RUN make
RUN make install
RUN cp -r GalaxiaData /

RUN pip install ebfpy

RUN echo Y | galaxia -s warp; exit 0

RUN rm -R /code/galaxia/galaxia-0.8.1

WORKDIR /code




