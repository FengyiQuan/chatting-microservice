FROM public.ecr.aws/docker/library/python:3.9.9-slim

EXPOSE 8080

WORKDIR /app

COPY app/requirements.txt /app/

RUN pip install -r requirements.txt

COPY app/server.py /app/

CMD [ "python",  "server.py"]