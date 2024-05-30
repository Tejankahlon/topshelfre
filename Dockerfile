# Use the Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copt the rest of the application code to the container
COPY . .

# Command to run the FASTAPI server
CMD ["uvicorn", "test_and_app:app", "--host", "0.0.0.0", "--port", "8000"]