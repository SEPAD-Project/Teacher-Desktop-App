[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/SEPAD-Project/Teacher-Desktop-App/blob/main/README.md)
[![fa](https://img.shields.io/badge/lang-fa-blue.svg)](https://github.com/SEPAD-Project/Teacher-Desktop-App/blob/main/README.fa.md)
# SEPAD (The Persian acronym for Student Online Monitoring System) - Teacher-Desktop-App
This repository is a part of the SEPAD project and was developed by [Abolfazl Rashidian](https://github.com/abolfazlrashidian) for students to enter the class and send their attention level to the server.

Click [here](https://github.com/SEPAD-Project) to visit the SEPAD organization.

## Overview
The Teacher Panel in SEPAD (Student Attention Platform) is a management interface that allows teachers to monitor students' attention levels in real-time during online classes. This panel collects data on their focus (through facial recognition and gaze analysis via webcam) and displays it desktop app.

## Requirements
Before installation, ensure you meet these requirements:
- Python 3.8 or higher
- Minimum hardware specifications:
  - Dual-core processor
  - 2GB RAM

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SEPAD-Project/Teacher-Desktop-App.git
```
2. Navigate to the Teacher-desktop-app directory:
```bash
cd Teacher-desktop-app
```
3. Create a virtual environment:
```bash
python -m venv .venv
```
4. Activate the virtual environment:
```bash
.venv\Scripts\activate.bat
```
5. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
python source/gui/authentication_page.py
```

## Directory Structure
```bash
teacher-desktop-app/
├── source/
├── └──
├──── gui/                          # GUI components
│     └── authentication_page.py    # Main application entry point
├──── backend/                      # Attention analysis models
├── RUN.py                          # Run login page
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation
└── .gitignore                      # Git ignore file
```

# 📬 Contact  
**Email**: SepadOrganizations@gmail.com  
**Issues**: [GitHub Issues](https://github.com/SEPAD-Project/Teacher-Desktop-App/issues)  