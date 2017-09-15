FROM python:3.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_CONFIG production

EXPOSE 5000

CMD [ "python", "./manage.py", "runserver", "--host", "0.0.0.0"]