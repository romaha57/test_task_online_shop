FROM python

WORKDIR /app

EXPOSE 8000

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "online_shop/manage.py", "makemigrations"]
CMD ["python", "online_shop/manage.py", "migrate"]
CMD ["python", "online_shop/manage.py", "runserver", "0.0.0.0:8000"]