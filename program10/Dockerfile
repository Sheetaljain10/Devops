# Use Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy application code
COPY . /app

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
