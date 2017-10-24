FROM python:3.5
LABEL maintainer="Adolfo Lopez (adolfolopez88@gmail.com)"

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y 

WORKDIR /app
COPY . ./

RUN pip install -r requirements.pip

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000