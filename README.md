# Home Lab Projects

## Project 0: Kali Linux Virtual Machine Setup
This is the foundation of my security lab. I have configured a Kali Linux environment for penetration testing and security analysis.

![Kali Linux Screenshot](KaliScreenshot1.png)

## Project 1: Home Network Security Audit
Objective: Perform a baseline audit of a home network to identify connected assets and verify network visibility.

Tools Used:
Virtualization: VirtualBox
OS: Kali Linux
Tool: Nmap (Network Mapper)

Methodology:
Configured Kali Linux VM with a Bridged Adapter to ensure direct network visibility.
Executed "sudo nmap -sn 192.168.x.x/24" to discover active hosts.
Mapped connected devices to identify potential assets.

Findings:
![Kali Linux Screenshot](NetworkSecurityAudit1.png)
Total Devices Discovered: 4

Observation: I identified 4 devices. This scan confirms my visibility into the network, which is the foundational step for any incident response process.

Analysis
Effective security starts with knowing what you own. By performing this audit, I established a baseline for my home network. In a corporate environment, this process is known as "Asset Inventory Management", which is critical for ensuring only authorized devices access sensitive data. I know who is allowed on my network, any potential threats can be quikcky identified.

## Project 2: Phishing Email Triage Playbook
I created a fake phishing email because my security systems already block most spam and phishing emails. I would not be able to take a screenshot for this project.
### Analysis of Phishing Sample #1

> **Subject:** ACTION REQUIRED: Final Notice - Account Suspension
> **From:** IT Support <security-alerts@micros0ft-support.com>

**Red Flags Identified:**

* **1. Sender Domain:** The domain `micros0ft-support.com` contains a "zero" instead of an "o" (typosquatting). A legitimate company would use `microsoft.com`.
* **2. Urgency:** The phrase "Failure to act within 24 hours" is a psychological tactic designed to prevent the user from verifying the request.
* **3. Generic Greeting:** "Dear Valued Employee" is often used in mass-phishing campaigns to avoid using the target's actual name.

Intake & Classification
Definition: What does a "Suspicious Email" look like?

Analysts should categorize reports into:
Malicious (Confirmed Phish),
Spam (Non-malicious noise),
or False Positive (Legitimate email).

The Analysis Checklist
Sender: Is the email address domain matching the company name? (e.g., hr@microsoft-security.com vs hr@microsoft.com).
Urgency: Does the email threaten account deletion or promise "free money" to force an emotional reaction?
Links: (Crucial!) Tell the reader: "Never click. Hover the mouse to reveal the actual destination. Does the URL look like a random string of characters?"
Attachments: Are there unexpected .zip, .exe, or .iso files?

Escalation/Remediation
If verified as malicious:
Block the sender domain at the email gateway.
Search email logs for other users who received the same message.
Purge the email from all inboxes.

Analysis:
Phishing triage is not just about blocking emails; it is about Risk Mitigation. 
By establishing a clear, repeatable process, we reduce the 'Mean Time To Respond' (MTTR), ensuring that a single user error doesn't become a company-wide data breach.
