
# README.md

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
Follow me on [Twitter/X @cybergrandpa__](https://twitter.com/cybergrandpa__)

---

# LICENSE (MIT)

MIT License

Copyright (c) 2025 CyberGrandpa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

---

# builder/build_exe_guide.md

## 🧱 Build the Client Executable

### 1. Install PyInstaller
```bash
pip install pyinstaller
```

### 2. Build the Executable
```bash
pyinstaller --noconsole --onefile client.py
```

The `.exe` file will appear in the `dist/` folder.

---

# lab_setup/how_to_test_in_vm.md

## 🧪 Setting Up the CyberGrandpa-RAT Lab

### Requirements
- VirtualBox or VMware
- Two VMs (one attacker, one victim)
- Python 3 on both machines

### Steps
1. Set the attacker VM to Host-Only or Bridged Adapter networking.
2. Run `server.py` on the attacker.
3. Build and run `client.py` on the victim.
4. Control the victim safely inside the lab.

NEVER run this tool on real devices.

---

# requirements.txt

pyautogui
pynput
opencv-python
