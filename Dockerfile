FROM python:3.7-buster

COPY . /app
EXPOSE 5000
WORKDIR /app
RUN pip install -r requirements.txt

CMD [ "streamlit" , "run" , "main.py"] 

