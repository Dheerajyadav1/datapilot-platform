FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt first to cache dependencies
COPY requirements.txt .

# Install python packages
RUN pip install --no-cache-dir grpcio grpcio-status
RUN pip install --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt

# Set PYTHONPATH to include the project directory
ENV PYTHONPATH="/app:${PYTHONPATH}"

# Expose Streamlit's default port
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "app/Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
