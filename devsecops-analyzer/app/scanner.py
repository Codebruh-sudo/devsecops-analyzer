import subprocess
import os

def run_trivy(file_path):
    try:
        result = subprocess.run(
            ["trivy", "config", "--format", "json", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        return {"output": result.stdout}
    except FileNotFoundError:
        return {"error": "[Trivy] Binary not found. Make sure it's installed and in PATH."}
    except subprocess.CalledProcessError as e:
        return {"error": f"[Trivy] Scan failed: {e.stderr}"}

def run_gitleaks(file_path):
    try:
        result = subprocess.run(
            ["gitleaks", "detect", "--source", file_path, "--report-format", "json"],
            capture_output=True,
            text=True
        )
        return {"output": result.stdout, "exit_code": result.returncode}
    except FileNotFoundError:
        return {"error": "[Gitleaks] Binary not found. Check install path."}
    except Exception as e:
        return {"error": str(e)}

def run_yamllint(file_path):
    if not file_path.endswith((".yml", ".yaml")):
        return {"skipped": "File not YAML, skipping yamllint."}
    try:
        result = subprocess.run(
            ["yamllint", "-f", "json", file_path],
            capture_output=True,
            text=True,
            check=False  # allow non-zero exit code when errors are found
        )
        return {"output": result.stdout, "exit_code": result.returncode}
    except FileNotFoundError:
        return {"error": "[yamllint] Binary not found."}
    except Exception as e:
        return {"error": str(e)}
