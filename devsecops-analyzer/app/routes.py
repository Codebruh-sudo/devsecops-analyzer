from flask import Blueprint, request, jsonify
import os, json
from .scanner import run_trivy, run_gitleaks, run_yamllint
from .result_saver import save_results

bp = Blueprint("routes", __name__)
UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@bp.route("/", methods=["GET"])
def index():
    """
    Welcome route showing available endpoints.
    ---
    responses:
      200:
        description: Root route with endpoint listing
        examples:
          application/json: {
            "message": "Welcome to the DevSecOps Analyzer API",
            "endpoints": ["/upload", "/results/<filename>", "/healthz", "/apidocs"]
          }
    """
    return jsonify({
        "message": "Welcome to the DevSecOps Analyzer API",
        "endpoints": [
            "/upload (POST)",
            "/results/<filename> (GET)",
            "/healthz (GET)",
            "/apidocs (Swagger UI)"
        ]
    }), 200

@bp.route("/upload", methods=["POST"])
def upload_file():
    """
    Upload a file for security scanning using Trivy, Gitleaks, and yamllint.
    ---
    consumes:
      - multipart/form-data
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: The file to scan (.yml, .yaml, Dockerfile, etc)
    responses:
      200:
        description: Scan results from all tools
        examples:
          application/json: {
            "filename": "Dockerfile",
            "trivy": {"output": "..."},
            "gitleaks": {"output": "..."},
            "yamllint": {"skipped": "File not YAML"},
            "saved_to": "results/result_2025-07-16_02-49-00_Dockerfile.json"
          }
    """
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    trivy_result = run_trivy(filepath)
    gitleaks_result = run_gitleaks(filepath)
    yamllint_result = run_yamllint(filepath)

    result_data = {
        "filename": file.filename,
        "trivy": trivy_result,
        "gitleaks": gitleaks_result,
        "yamllint": yamllint_result
    }

    saved_path = save_results(result_data, file.filename)
    result_data["saved_to"] = saved_path

    return jsonify(result_data)

@bp.route("/healthz", methods=["GET"])
def health_check():
    """
    Health check endpoint to verify API status.
    ---
    responses:
      200:
        description: API is running
        examples:
          application/json: {"status": "ok"}
    """
    return jsonify({"status": "ok"}), 200

@bp.route("/results/<filename>", methods=["GET"])
def get_result(filename):
    """
    Retrieve a saved scan result by filename.
    ---
    parameters:
      - name: filename
        in: path
        type: string
        required: true
        description: JSON result filename (e.g. result_2025-07-16_02-49-00_Dockerfile.json)
    responses:
      200:
        description: Result content
      404:
        description: File not found
    """
    path = os.path.join(RESULT_FOLDER, filename)
    if not os.path.exists(path):
        return jsonify({"error": "File not found"}), 404

    with open(path) as f:
        content = json.load(f)
    return jsonify(content)
