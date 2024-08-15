FROM python:3.11-slim

WORKDIR /var/app

COPY . /var/app/

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN set -a; source .env; set +a

EXPOSE 5000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "-w", "4"]
