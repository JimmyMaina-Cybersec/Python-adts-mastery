# Use official Python slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python tools
RUN pip install --upgrade pip setuptools wheel

# Copy your project files
WORKDIR /app
COPY . /app

# Install Python dependencies (add whatever you need)
RUN pip install \
    pytest \
    pytest-cov \
    pytest-benchmark \
    black \
    flake8 \
    pylint \
    memory-profiler \
    line-profiler \
    py-spy

# Default command (can be overridden in docker-compose or docker run)
CMD ["python"]
