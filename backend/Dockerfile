FROM python:3-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD flask --app server run -h 0.0.0.0 -p 5000