FROM python:3.14-slim

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./src ./src
COPY ./data.parquet ./config.yaml ./start.sh ./

RUN chmod +x ./start.sh
ENTRYPOINT ["./start.sh"]
