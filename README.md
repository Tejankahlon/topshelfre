# TopShelfRE Take Home Assessment - Tejan Kahlon

Hello! I'm Tejan Kahlon and here is my submission for the TopShelfRE coding assignment. I used Python with FastAPI, added full functionality to the API endpoints, and included testing. The server code and tests are combined in `test_and_app.py`. The application is also containerized using Docker.

## Setup Instructions

### Clone the Repo and Install Dependencies
1. **Clone the repository**:
   git clone https://github.com/yourusername/topshelfre.git
   cd topshelfre

##
2. **Install dependencies**:

pip install -r requirements.txt

## Running the Application
1. Start the FastAPI server:
uvicorn test_and_app:app --reload

2. Access the application:
Open your browser and go to http://127.0.0.1:8000

## Running Tests
pytest

## Running in Docker
Build and Run Docker Container

1. Ensure Docker is installed:
Download and install Docker from Docker's official site.

2. Build the Docker image:
docker build -t myfastapiapp .

3. Run the Docker container:
docker run -d -p 8000:8000 myfastapiapp

4. Access the application:
Open your browser and go to http://127.0.0.1:8000

## Dockerfile Used

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