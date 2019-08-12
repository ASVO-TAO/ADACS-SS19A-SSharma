FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /galaxia
WORKDIR /galaxia
COPY  ./galaxia /galaxia/
RUN tar -zxvf galaxia-0.8.1.tar.gz
WORKDIR galaxia-0.8.1
RUN ./configure --datadir=/GalaxiaData
RUN make
RUN make install
RUN cp -r GalaxiaData /

WORKDIR /galaxia
RUN tar -zxvf ebfpy-0.0.14.tar.gz
WORKDIR ebfpy-0.0.14
RUN python setup.py install --install-scripts=/bin/

RUN echo Y | galaxia -s warp

WORKDIR /
RUN mkdir /code
WORKDIR /code
COPY  requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/


#WORKDIR /code/galaxia
#RUN tar -zxvf galaxia-0.8.1.tar.gz
#WORKDIR galaxia-0.8.1
#RUN ./configure --datadir=/GalaxiaData
#RUN make
#RUN make install
#RUN cp -r GalaxiaData /
#
#WORKDIR /code/galaxia
#RUN tar -zxvf ebfpy-0.0.14.tar.gz
#WORKDIR ebfpy-0.0.14
#RUN python setup.py install --install-scripts=/bin/
#
#RUN echo Y | galaxia -s warp
#
#RUN rmdir /code/galaxia/galaxia-0.8.1
#
#WORKDIR /code



