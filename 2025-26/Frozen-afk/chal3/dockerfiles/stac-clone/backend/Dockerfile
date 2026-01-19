FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
# Upgrade pip
RUN pip install --upgrade pip
# Copy the requirements file
COPY requirements.txt ./
# Install dependencies 
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]