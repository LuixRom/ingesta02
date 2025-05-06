FROM python:3-slim

WORKDIR /programas/ingesta

RUN pip install boto3 pymysql pandas cryptography

COPY . .

CMD [ "python3", "./ingesta.py" ]
