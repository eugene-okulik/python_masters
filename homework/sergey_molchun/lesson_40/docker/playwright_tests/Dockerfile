FROM python:latest

# Install necessary system dependencies
RUN apt-get update && apt-get install -y python3-venv wget git build-essential \
    libssl-dev libffi-dev python3-dev

# Install Google Chrome for Playwright
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && apt-get install -y google-chrome-stable

# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Clone your GitHub repository
RUN git clone https://github.com/Moserios/docker_automation.git /automation

# Set the working directory
WORKDIR /automation

# Install Playwright and browser binaries
RUN pip install playwright && playwright install

# Create a virtual environment and activate it for subsequent commands
RUN python -m venv venv
ENV PATH="/automation/venv/bin:$PATH"

# Install Python dependencies
RUN pip install -r requirements.txt

# Set additional environment variables
ENV COOL_PORT=8160 \
    COOL_IP=0.0.0.0 \
    COOL_LOG=log

# Expose the port the app runs on
EXPOSE 8160/tcp

# Create necessary directories
RUN mkdir log

# Add a text file
RUN echo "Playwright Python Autotests" > readme.md

# Command to keep the container running
CMD ["sleep", "infinity"]
