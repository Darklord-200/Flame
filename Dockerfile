FROM python:3.10.4

# set working directory
WORKDIR /app

# install requirements
COPY /requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]