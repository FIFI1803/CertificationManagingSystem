# Student Certification Management System

A command-line application for managing student certifications, module data, and assessment results. This system provides an intuitive interface for educational institutions to track student progress, manage certification modules, and generate comprehensive reports.

## Features

- Student Management
- Add, view, edit, and delete student records
- Track individual student progress
- Manage student certification status

- Module Management
- Create and modify certification modules
- Set module requirements and criteria
- Track module completion rates

- Results Management
- Record and update assessment results
- Track pass/fail rates
- Monitor student performance

- Reporting
- Generate detailed student progress reports
- Export certification statistics
- Create summary reports for modules

- User-friendly Interface
- Clear console-based menu system
- Rich text formatting for better readability
- Intuitive navigation

## Requirements

- Python 3.7 or higher
- SQLite3
- Required Python packages:
- rich
- sqlite3
- pandas

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/certification-management.git
cd certification-management
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
python main.py --init-db
```

## Usage

Run the application:
```bash
python main.py
```

### Main Menu Options:

1. **Students**
- View all students
- Add new student
- Edit student details
- Delete student record

2. **Modules**
- View all modules
- Add new module
- Edit module details
- Delete module

3. **Results**
- View student results
- Record new result
- Update existing result
- Delete result

4. **Reports**
- Generate student progress report
- View certification statistics
- Export results to CSV

5. **Exit**
- Save and exit the application

Use arrow keys to navigate the menu and Enter to select an option. Follow the on-screen prompts to perform various operations.

