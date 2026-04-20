FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./src ./src
COPY ./data.parquet ./config.yaml ./start.sh ./

RUN chmod +x ./start.sh
ENTRYPOINT ["./start.sh"]
