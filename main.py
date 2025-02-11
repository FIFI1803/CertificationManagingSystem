import app
import os
import rich as console

def clear():
    os.system('clear')

def view():
    clear()
    console.print('[cyan][bold]====================[/bold][/cyan] [purple][bold]View Data[/bold][/purple] [cyan][bold]====================[/bold][/cyan]')
    console.print('[green][bold]1.[/bold][/green] Student')
    console.print('[green][bold]2.[/bold][/green] Module')
    console.print('[cyan][bold]===================================================[/bold][/cyan]')

    view_options = input('Enter option (1-2) or press 0 to quit:')
    if view_options == '1':
        clear()
        app.student_data()
        if input('Press 0 to leave: ') == '0':
            navigation()
    elif view_options == '2':
        clear()
        app.module_data()
        if input('Press 0 to leave: ') == '0':
            navigation()
    elif view_options == '0':
        navigation()
    else:
        clear()
        print('Invalid input. Please try again.')
        view()

def edit():
    clear()
    console.print('[cyan][bold]====================[/bold][/cyan] [purple][bold]Edit Data[/bold][/purple] [cyan][bold]====================[/bold][/cyan]')
    console.print('[green][bold]1.[/bold][/green] Student')
    console.print('[green][bold]2.[/bold][/green] Module')
    console.print('[cyan][bold]===================================================[/bold][/cyan]')

    edit_options = input('Enter option (1-2) or press 0 to quit:')
    if edit_options == '1':
        clear()
        app.student_data()
        app.edit_student()
        navigation()
    elif edit_options == '2':
        clear()
        app.module_data()
        app.edit_module()
        navigation()
    elif edit_options == '0':
        navigation()
    else:
        print('Invalid input. Please try again.')
        edit()

def result():
    clear()
    app.check_result()

def get_report():
    clear()
    app.generate_report()


def navigation():
    clear()
    console.print('[cyan][bold]=========[/bold][/cyan] [purple][bold]Certification Management System[/bold][/purple] [cyan][bold]=========[/bold][/cyan]')
    console.print('[green][bold]1.[/bold][/green] View Data')
    console.print('[green][bold]2.[/bold][/green] Edit Data')
    console.print('[green][bold]3.[/bold][/green] Check Result')
    console.print('[green][bold]4.[/bold][/green] Generate Report')
    console.print('[cyan][bold]===================================================[/bold][/cyan]')
    navigation_options = input('Enter option (1-4) or press 0 to quit:')
    if navigation_options == '1':
        view()
    elif navigation_options == '2':
        edit()
    elif navigation_options == '3':
         result()
    elif navigation_options == '4':
        get_report()
    elif navigation_options == '0':
        exit()
    else:
        print('Invalid input. Please try again.')
        navigation()


def main():
    navigation()

if __name__ == '__main__':
    main()