FROM python:3.11.5
RUN apt-get update && apt-get -y install git && rm -rf /var/lib/apt/lists/*
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/app"
EXPOSE ${PORT}
CMD ["python3", "./main.py"]