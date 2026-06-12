# Project 6: Container Security Posture Management (CSPM)

## Objective
To enforce Zero Trust principles in a containerized environment (Kubernetes/OpenShift) by pre-scanning container images for vulnerabilities prior to deployment.

## Tools Used
* **OS:** Kali Linux
* **Scanner:** Trivy (Aqua Security)
* **Target:** Vulnerable Web App Container Image

## Methodology
In high-velocity OpenShift environments, vulnerable containers can compromise the entire cluster. 
I utilized Trivy to perform a static vulnerability scan on a target Docker image. 

## Findings & Remediation

The scan revealed multiple CRITICAL vulnerabilities in the image dependencies. 
**Remediation Policy:** 
In a live OpenShift environment, CI/CD pipelines must be configured to automatically block any container deployment that returns a "High" or "Critical" CVE score during the Trivy scan.
