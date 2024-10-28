FROM python:3-slim

WORKDIR /app

# Installer netcat
RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Corriger les permissions et les fins de ligne
RUN apt-get install -y dos2unix \
    && dos2unix wait-for-db.sh \
    && chmod +x wait-for-db.sh

CMD ["./wait-for-db.sh"]