FROM python:3.10-slim

# set working directory
WORKDIR /app

# copy requirement file and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy app files
COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]
