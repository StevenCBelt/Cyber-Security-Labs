# Project 10: Enterprise Compliance Crosswalk Matrix (SOC 2 & FedRAMP)

## Objective
To translate technical security controls into a unified Governance, Risk, and Compliance (GRC) matrix, mapping internal corporate policies to external regulatory frameworks.

## Scenario
The organization is preparing for a SOC 2 Type II audit and a FedRAMP Moderate authorization. As part of the readiness assessment, internal Access Control Policies must be mapped directly to the corresponding framework controls to prove compliance.

---

## 1. Internal Access Control Policy (Excerpt)
* **AC-Pol-01 (Multi-Factor Authentication):** All user accounts, including administrative and service accounts, must enforce MFA using an authenticator application or hardware token. SMS-based MFA is prohibited.
* **AC-Pol-02 (Principle of Least Privilege):** Users shall only be granted the minimum access permissions necessary to perform their job functions (Role-Based Access Control - RBAC).
* **AC-Pol-03 (Account Termination):** IT Security must revoke all access credentials within 24 hours of an employee's termination or transfer.
* **AC-Pol-04 (Access Reviews):** System owners must conduct automated or manual audits of all active user accounts on a quarterly basis.

---

## 2. The Compliance Crosswalk Matrix

| Internal Policy ID | Technical Implementation | SOC 2 (TSC) Mapping | FedRAMP (NIST 800-53) Mapping |
| :--- | :--- | :--- | :--- |
| **AC-Pol-01** | AWS IAM Python Auditor Script | **CC6.3:** Require authorized users to authenticate identity. | **IA-2:** Identification and Authentication (Organizational Users). |
| **AC-Pol-02** | AWS IAM Roles & Groups | **CC6.1:** Implement logical access security software. | **AC-6:** Least Privilege. |
| **AC-Pol-03** | Automated Bash Deprovisioning | **CC6.2:** Prior to issuing credentials, verify identity. | **AC-2 (3):** Account Management | Disable Accounts. |
| **AC-Pol-04** | Quarterly IAM Log Review | **CC6.3:** Review access systematically. | **AC-2 (4):** Account Management | Automated Audit Actions. |

---

## Analysis
Security tools are only as effective as the policies governing them. By developing this Crosswalk Matrix, I demonstrated the ability to bridge the gap between technical engineering (like writing AWS MFA auditor scripts) and executive compliance requirements. 
This ensures that the technical safeguards implemented on the ground satisfy the strict legal and regulatory demands required to keep the business operational.
