import sqlite3
import main

def student_data():
    conn = sqlite3.connect('cert_project.db')
    c = conn.cursor()
    c.execute('SELECT * FROM student')
    student_list = c.fetchall()
    conn.close()
    print('========= Student Data =========')
    for student in student_list:
        print(f'ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}, Age: {student[3]}')
        print('----------------------------------------')


def module_data():
    conn = sqlite3.connect('cert_project.db')
    c = conn.cursor()
    c.execute('SELECT * FROM module')
    module_list = c.fetchall()
    conn.close()
    print('========= Module Data =========')
    for module in module_list:
        print(f'ID: {module[0]}, Module Name: {module[1]}')
        print('----------------------------------------')

def edit_student():
    print('========= Edit Student =========')
    student_id = input('Enter student ID you want to change or press 0 to quit:')
    if student_id == '0':
        main.navigation()
    new_first_name = input('Enter new first name:')
    new_last_name = input('Enter new last name:')
    new_age = input('Enter new age:')
    
    conn = sqlite3.connect('cert_project.db')
    c = conn.cursor()
    c.execute('UPDATE student SET first_name = ?, last_name = ?, age = ? WHERE id = ?', (new_first_name, new_last_name, new_age, student_id))
    conn.commit()

def edit_module():
    print('========= Edit Module =========')
    module_id = input('Enter module ID you want to change or press 0 to quit:')
    if module_id == '0':
        main.navigation()
    new_module_name = input('Enter new module name:')

    conn = sqlite3.connect('cert_project.db')
    c = conn.cursor()
    c.execute('UPDATE module SET module = ? WHERE id = ?', (new_module_name, module_id))
    conn.commit()

def check_result():
    print('========= Check Result =========')
    student_id = input('Enter student ID to check result or press 0 to quit:')
    if student_id == '0':
        main.navigation()
    conn = sqlite3.connect('cert_project.db')
    c = conn.cursor()
    c.execute('SELECT student.id, result.result FROM student JOIN result on student.id = result.student_id WHERE student.id = ?', (student_id,))
    for student in c.fetchall():
        student_id, result = student
        print(f'Student ID: {student[0]}, Result: {student[1]}')
    conn.close()
    back = input('Press 0 to leave: ')
    if back == '0':
        main.navigation()

def get_name(student_id):
    conn = sqlite3.connect('cert_project.db')
    c = conn.cursor()
    c.execute('SELECT first_name, last_name FROM student WHERE id = ?', (student_id,))
    name = c.fetchone()
    for student in name:
        first_name, last_name = name
        return(f'{name[0]} {name[1]}') 

def generate_report():
    grades = {
        1: 'Unsuccessful',
        2: 'Pass',
        3: 'Merit',
        4: 'Distinction'
    }
    print('========= Generate Report =========')
    unsuccessful = 0
    student_id = input('Enter student ID to generate report or press 0 to quit: ')
    if student_id == '0':
        main.navigation()
    conn = sqlite3.connect('cert_project.db')
    c = conn.cursor()
    c.execute('SELECT student.id, module.module, result.result FROM student JOIN result on student.id = result.student_id JOIN module on result.module_id = module.id WHERE student.id = ?', (student_id,))
    data = c.fetchall()
    with open(f'CertReportStudentID{student_id}.txt', 'w') as file:
        file.write('========= Certification Report =========\n')
        file.write(f'Student ID: {student_id} Name:{get_name(student_id)}\n')
        file.write('----------------------------------------\n')
        for student in data:
            student_id,module, result = student
            if result < 50:
                file.write(f'Module: {student[1]}| Grade: {grades[1]}' + '\n')
                unsuccessful += 1
                file.write('----------------------------------------\n')
            elif 50 <= result < 64:
                file.write(f'Module: {student[1]}| Grade: {grades[2]}' + '\n')
                file.write('----------------------------------------\n')
            elif 65 <= result < 79:
                file.write(f'Module: {student[1]}| Grade: {grades[3]}' + '\n')
                file.write('----------------------------------------\n')
            else:
                file.write(f'Module: {student[1]}| Grade: {grades[4]}' + '\n')
                file.write('----------------------------------------\n')
            
        if unsuccessful == 0:
            file.write(f'Overall: Full Certification Achieved\n')
        elif unsuccessful == 4:
            file.write(f'Overall: No Certification Achieved\n')
        else:
            file.write(f'Overall: Partial Certification Achieved\n')
    print('Report has been generated.')
    main.navigation()