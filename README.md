# Student Attention Platform (SAP) - Teacher App

## Overview
The Teacher Panel in SAP (Student Attention Platform) is a management interface that allows teachers to monitor students' attention levels in real-time during online classes. This panel collects data on their focus (through facial recognition and gaze analysis via webcam) and displays it .

## Requirements
Before installation, ensure you meet these requirements:
- Python 3.8 or higher
- Minimum hardware specifications:
  - Dual-core processor
  - 2GB RAM

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SAP-Program/Teacher-App.git
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
**Email**: sapOrganizations@gmail.com  
**Issues**: [GitHub Issues](https://github.com/SAP-Program/Teacher-App/issues)  

# 📜 License (MIT)  
```text
MIT License

Copyright (c) 2023 SAP Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```