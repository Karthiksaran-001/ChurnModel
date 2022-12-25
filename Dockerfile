FROM python:3.7-buster

COPY . /app
EXPOSE 5000
WORKDIR /app
RUN pip install -r requirements.txt

CMD [ "streamlit" , "run" , "main.py"] 


## docker build -t karthiksaran11/churnmlproject .
## docker run --name mlproject -d -p 5000:8501 karthiksaran11/churnmlproject (8501 is default streamlit run port we change to 5000)

## docker push karthiksaran11/churnmlproject:latest  (Push Local --> Hub Always use Username in  your Image while create Image)
