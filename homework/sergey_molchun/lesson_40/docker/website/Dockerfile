FROM python:latest
RUN apt-get update


# Set environment variables
ENV COOL_PORT 8000
ENV COOL_IP 0.0.0.0
ENV COOL_LOG log

# Expose the port the app runs on
EXPOSE 8000/tcp

# Create necessary directories
RUN mkdir log
RUN mkdir /bulldog-app/

# Add a text file (this could also be done using COPY if the file exists locally)
RUN echo "Bulldog reminder website" > /bulldog-app/bulldog-text.txt

# Clone your GitHub repository
RUN git clone https://github.com/Moserios/bulldoggy-reminders-app.git /bulldoggy-reminders-app

# Install required Python packages
RUN pip install --no-cache-dir fastapi==0.100.0 \
    Jinja2==3.1.2 \
    PyJWT==2.7.0 \
    pytest-playwright==0.3.3 \
    python-multipart==0.0.6 \
    requests==2.31.0 \
    tinydb==4.8.0 \
    "uvicorn[standard]==0.22.0"

WORKDIR /bulldoggy-reminders-app

# Command to run the application
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0"]

