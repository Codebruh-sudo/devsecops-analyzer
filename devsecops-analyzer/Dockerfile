FROM python:3.11-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    lsb-release \
    git \
    wget \
    tar \
    && rm -rf /var/lib/apt/lists/*

# Trivy install
RUN curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh

# Gitleaks install
RUN wget https://github.com/gitleaks/gitleaks/releases/download/v8.17.0/gitleaks_8.17.0_linux_x64.tar.gz \
    && tar -xvzf gitleaks_8.17.0_linux_x64.tar.gz \
    && mv gitleaks /usr/local/bin/gitleaks \
    && rm gitleaks_8.17.0_linux_x64.tar.gz

# Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt yamllint

# App code
COPY app/ app/


CMD ["python", "-m", "app"]
