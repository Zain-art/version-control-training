# Use an official Python image as base
FROM python:alpine

# Set working directory in the container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Run the Python script
CMD ["python", "app.py"]
