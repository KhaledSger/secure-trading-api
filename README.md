# Secure-by-Design Trading API: DevSecOps Pipeline Architecture

A proof-of-concept demonstrating a secure software development lifecycle (SSDLC). This project deploys a containerized Python trading application to AWS via Terraform, enforcing strict security gates and "shift-left" vulnerability scanning directly within the CI/CD pipeline.

## 🛡️ Core Security Enforcements

This repository is built to demonstrate enterprise-grade Zero Trust principles:
- **Pipeline Hard-Failing:** The GitHub Actions workflow is configured to explicitly block and fail deployments if `CRITICAL` or `HIGH` vulnerabilities are detected.
- **Container Security (Trivy):** Automated scanning of the Docker image for OS and library CVEs before it reaches the registry. The Dockerfile is explicitly configured to run as a non-root, least-privilege user.
- **Infrastructure Security (Checkov):** Static Application Security Testing (SAST) for the Terraform code, ensuring AWS cloud misconfigurations (like public S3 buckets or open security groups) are blocked prior to deployment.
- **Automated Linting (Ruff):** Enforcing clean, predictable Python code standards.

## ⚙️ Tech Stack & Tooling

- **Application:** Python 3.10+, Docker
- **Infrastructure as Code (IaC):** Terraform, AWS
- **Security Scanners:** Aquasecurity Trivy, Bridgecrew Checkov
- **Orchestration:** GitHub Actions

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Docker
- AWS CLI configured
- Terraform installed

### Local Development & Linting

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt