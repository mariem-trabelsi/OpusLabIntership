# Stage 1: Build dependencies
FROM python:3.12-slim AS builder

WORKDIR /app

# Copy requirements and install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime image
FROM python:3.12-slim

WORKDIR /app

# Copy installed deps from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy app code
COPY app.py .
COPY templates/ templates/

# Expose port and run
EXPOSE 5000
CMD ["python", "app.py"]