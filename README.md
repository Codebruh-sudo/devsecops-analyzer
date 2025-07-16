### DevSecOps Analyzer
A modular Flask-based backend that scans code for security issues and configuration errors using Trivy, Gitleaks, and yamllint. Built with containerization, CI/CD pipelines, and automated deployment in mind.

🚀 Features
🔍 Container image vulnerability scanning via Trivy

🔑 Secrets detection via Gitleaks

📄 YAML linting for config hygiene

🐳 Dockerized with clean build context

🔁 CI/CD ready using GitHub Actions

### 🧰 Tech Stack
Tool	Purpose
Flask	Backend API server
Trivy	Container vulnerability scanner
Gitleaks	Secrets detection in code
yamllint	Linting YAML configuration files
Docker	Containerization
GitHub Actions	CI/CD Pipeline
🛠️ Installation & Usage
1. Clone the repo:
bash
git clone https://github.com/<your-username>/devsecops-analyzer.git
cd devsecops-analyzer
2. Build Docker image:
bash
docker build . -t devsecops-analyzer
3. Run the container:
bash
docker run -p 5000:5000 devsecops-analyzer
Access Flask API at http://localhost:5000

### 🔐 Run Security Scans (Locally)
Gitleaks:
bash
curl -sSL https://github.com/gitleaks/gitleaks/releases/latest/download/gitleaks-linux-amd64 -o gitleaks
chmod +x gitleaks
./gitleaks detect --source . --no-banner
Trivy:
bash
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh
./trivy image devsecops-analyzer
⚙️ GitHub Actions Workflow
Located in .github/workflows/final.yml

CI flow includes:
✅ Build Docker image from correct subfolder

✅ Timestamped image tagging

✅ Ready for integration with security scans

Example CI snippet:

yaml
- name: Build Docker image
  run: |
    cd devsecops-analyzer
    docker build . -t devsecops-analyzer:$(date +%s)
🧪 API Folder Structure
devsecops-analyzer/
├── Dockerfile
├── app/
│   └── main.py
├── requirements.txt
├── uploads/
└── run.sh
