FROM python:3.11-slim

WORKDIR /opt/app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy package
COPY simple_interest_calculator/ ./simple_interest_calculator/

# Set PYTHONPATH
ENV PYTHONPATH=/opt/app

# Run FastAPI server
CMD ["uvicorn", "simple_interest_calculator.api:app", "--host", "0.0.0.0", "--port", "8080"]
