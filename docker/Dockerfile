# Base image

FROM python:3.11-slim
# Set working directory

WORKDIR /app
# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

