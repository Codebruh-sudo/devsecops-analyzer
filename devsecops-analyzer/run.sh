#!/bin/bash
echo "🔧 Building Docker image..."
docker build -t devsecops-analyzer .

echo "🚀 Running container on port 5000..."
docker run -p 5000:5000 devsecops-analyzer
