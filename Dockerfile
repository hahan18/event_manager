FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN git clone https://github.com/hahan18/event_manager.git /drf_src

WORKDIR /drf_src

RUN ls .

RUN pip install -r requirements.txt

VOLUME /drf_src

EXPOSE 8000

RUN python manage.py makemigrations && python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
