# CyberGrandpa-RAT 👴💻

> A Python-based Remote Access Tool (RAT) built for cybersecurity students and ethical hackers to simulate red team operations inside isolated lab environments.

⚠️ **Disclaimer:** This tool is strictly for **educational purposes only**. Do **not** use it on real systems or networks without explicit written permission. Unauthorized access is **illegal** and unethical.

## 🔥 Features
- Reverse Shell Connection
- Remote Command Execution
- Screenshot Capture
- Webcam Snapshot
- Keylogging
- Remote Keyboard Control

## 🧪 How to Use
1. Run `server/server.py` on the **attacker's machine** (e.g. Windows or Kali VM).
2. Build and execute `client/client.py` on the **victim's machine** inside a virtual lab.
3. Control the victim system using commands from the attacker's terminal.

## 🛠 Lab Setup
Use 2 virtual machines (VirtualBox or VMware):
- **Attacker:** Runs the command & control server.
- **Victim:** Executes the RAT client.

Refer to `lab_setup/how_to_test_in_vm.md` for full lab setup instructions.

## ⚖️ License
MIT License – See `LICENSE`

## 🧙 Author
**CyberGrandpa 👑**  
Follow me on [Twitter/X @cybergrandpa](https://twitter.com/cybergrandpa__)
