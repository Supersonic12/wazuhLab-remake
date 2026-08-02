# wazuhLab-remake

My own SIEM demonstration lab — a small, self-contained Wazuh / SIEM demo environment.

This repository contains three primary documents that explain the lab, guide setup, and provide demos/exercises. This README is a single entry point to make those documents easier to find and navigate.

Quick links
- [1. Overview: Setting up our attack and defense](./Setting%20up%20our%20attack%20and%20defense.md) — High-level description of the lab, objectives, and suggested attack/defense scenarios.
- [2. Setup: Setup windows agent for wazuh](./Setup%20windows%20agent%20for%20wazuh.md) — Step-by-step instructions to install and configure the Wazuh Windows agent.
- [3. Deployment: Wazuh Deployment on Ubuntu Server](./Wazuh%20Deployment%20on%20Ubuntu%20Server.md) — Instructions to deploy the Wazuh manager and supporting services on Ubuntu Server.

Getting started (one-line)
1. Read the Overview to understand the scope and scenarios.
2. Follow the Deployment guide to provision the Wazuh manager (Ubuntu Server).
3. Install the Windows agent using the Setup guide and run the demo exercises in the Overview.

Why these three docs?
- The Overview explains what the lab demonstrates and gives example exercises to try.
- The Deployment doc contains the server-side installation and configuration needed to receive data and alerts.
- The Windows agent doc shows how to connect a Windows host so you can generate telemetry and validate alerts and rules.

Navigation & tips
- Use the Quick links above to jump to the most important docs.
- Each linked document should include a table of contents — if they don't, please add one to improve navigation.
- If you rename files to remove spaces, update the links in this README accordingly.

Common tasks
- Quick start (Docker/VM): See the "Quick start" section inside "Wazuh Deployment on Ubuntu Server.md" (or add one if missing).
- Troubleshooting: Check logs on the manager and the agent; search for "wazuh" and "ossec" in log files.

Contributing
Contributions, bug reports and improvements are welcome. To add a new document, add a short entry here under Quick links and open a PR.

License
This repository is provided as-is for demonstration/learning purposes. See LICENSE if present.
