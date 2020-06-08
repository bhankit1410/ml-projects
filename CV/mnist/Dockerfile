FROM python:3.7-slim
WORKDIR /microservice

RUN apt-get update && \
apt-get -yq install gcc && \
    apt-get clean && \
    pip install --upgrade pip

COPY requirements.txt .
RUN  pip install --no-cache-dir -r requirements.txt

COPY . /microservice

EXPOSE 5000


ENV MODEL_NAME SeldonWrapper
ENV API_TYPE REST
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0
ENV FLASK_ENV development
CMD exec seldon-core-microservice $MODEL_NAME $API_TYPE --service-type $SERVICE_TYPE --persistence $PERSISTENCE