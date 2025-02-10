import app
import os

os.system('clear')

def view():
    print('========= View Data =========')
    print('1. Student')
    print('2. Module')
    view_options = input('Choose which data you want to view:')
    if view_options == '1':
        app.student_data()
        if input('Press 0 to leave: ') == '0':
            navigation()
    elif view_options == '2':
        app.module_data()
        if input('Press 0 to leave: ') == '0':
            navigation()
    else:
        print('Invalid input. Please try again.')
        view()

def edit():
    print('========= Edit Data =========')
    print('1. Student')
    print('2. Module')
    edit_options = input('Choose which data you want to add or press 0 to quit:')
    if edit_options == '1':
        app.student_data()
        app.edit_student()
        navigation()
    elif edit_options == '2':
        app.module_data()
        app.edit_module()
        navigation()
    elif edit_options == '0':
        navigation()
    else:
        print('Invalid input. Please try again.')
        edit()
def result():
    app.check_result()

def get_report():
    app.generate_report()


def navigation():
    print('========= Certification Management System =========')
    print('1. View Data')
    print('2. Edit Data')
    print('3. Check Result')
    print('4. Generate Report')
    navigation_options = input('Choose which option you want to use or press 0 to quit:')
    if navigation_options == '1':
        view()
    elif navigation_options == '2':
        edit()
    elif navigation_options == '3':
        result()
    elif navigation_options == '4':
        get_report()
    elif navigation_options == '0':
        print('Goodbye')
        exit()
    else:
        print('Invalid input. Please try again.')
        navigation()


def main():
    navigation()

if __name__ == '__main__':
    main()