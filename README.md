# SEPAD (The Persian acronym for Student Online Monitoring System) - Teacher App

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
git clone https://github.com/SEPAD-Project/Teacher-App.git
```
2. Navigate to the student-app directory:
```bash
cd teacher-app
```
3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
python source/gui/authentication_page.py
```

## Directory Structure
```bash
teacher-app/
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

# 📝 Contribution  
1. Fork the repository  
2. Create feature branch (`git checkout -b feature/NewFeature`)  
3. Commit changes (`git commit -m 'Add NewFeature'`)  
4. Push to branch (`git push origin feature/NewFeature`)  
5. Open a Pull Request  

# 📬 Contact  
**Email**: SepadOrganizations@gmail.com  
**Issues**: [GitHub Issues](https://github.com/SEPAD-Project/Teacher-App/issues)  