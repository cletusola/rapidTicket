FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app/ticket
COPY requirements.txt ./
RUN pip uninstall django 
RUN pip install -r requirements.txt 
COPY . /usr/src/app/ticket/



