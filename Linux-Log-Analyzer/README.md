# Project 7: Automated Linux Log Analyzer (Bash)

## Objective
To automate the parsing of server authentication logs to quickly identify brute-force SSH attacks and extract malicious IP addresses for firewall blocking.

## Skills Demonstrated
* **Linux Command Line:** Proficient in shell navigation and file permissions.
* **Bash Scripting:** Utilized `grep`, `awk`, `sort`, and `uniq` to pipe data outputs.
* **Threat Hunting:** Transformed raw, unstructured log data into actionable threat intelligence.

## The Script in Action


## Manager's Summary
Manual log review is highly inefficient. 
By automating this process with a Bash script, I reduced the Mean Time to Detect (MTTD) for brute-force attacks from minutes to milliseconds. 
In a live environment, this script's output could be piped directly into an IP table rule to automatically ban the attacking IP addresses.
