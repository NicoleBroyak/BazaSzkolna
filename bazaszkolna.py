from importyyyy import ALLOWED_USER_TYPES

students_list = list()
student_info_temp = dict()
mentors_list = list()
mentor_info_temp = dict()
supervisors_list = list()
supervisor_info_temp = dict()
class_list = set()
ALLOWED_COMMANDS = ('add', 'delete', 'books', 'stop')

class Student:
    def __init__(self):
        self.firstname = input('firstname: ')
        while not self.firstname:
            self.firstname = input('Type correct firstname: ')
        self.lastname = input('lastname: ')
        while not self.lastname:
            self.lastname = input('Type correct lastname: ')
        self.id = input('id: ')
        while not self.id:
            self.id = input('Type correct id: ')
        self.class_no = input('class: ')
        while not self.class_no:
            self.class_no = input('Type correct class:')
        self.title = "Student"

    def database_add(self):
        students_list.append({'firstname': self.firstname
                            ,'lastname': self.lastname
                            ,'id': self.id
                            ,'class': self.class_no
                            ,'title': "Student"})
        class_list.add(self.class_no)

    def class_command_print():
        print('Students:')
        for stud in students_list:
            if stud['class'] == command:
                f = stud['firstname']
                l = stud['lastname']
                i = stud['id']
                print(f'{f} {l} ID: {i}')

    def stud_command_print():
        for stud in students_list:
            studname = stud['firstname'] + ' ' + stud['lastname']
            id = stud['id']
            studclass = stud['class']
            if command == studname or command == id:
                print(f'\nMentors of student [{studname} ID: {id}]')
                for ment in mentors_list:
                    for classes in ment['classes']:
                        if classes == studclass:
                            mentname = ment['firstname'] + " " + ment['lastname']
                            id = ment['id']
                            subject = ment['subject']
                            print(f'{mentname} ID: {id}, subject: {subject}')


class Mentor:
    def __init__(self):
        self.firstname = input('firstname: ')
        while not self.firstname:
            self.firstname = input('Type correct firstname: ')
        self.lastname = input('lastname: ')
        while not self.lastname:
            self.lastname = input('Type correct lastname: ')
        self.id = input('id: ')
        while not self.id:
            self.id = input('Type correct id: ')
        self.subject = input('Subject: ')
        while not self.subject:
            self.subject = input('Type correct subject: ')
        self.classes = []
        class_input = input('class:')
        while not class_input:
            class_input = input('Type correct class:')
        while class_input:
            self.classes.append(class_input)
            class_input = input('Another class [submit empty line to abort]:')
        self.title = "Mentor"

    def database_add(self):
        mentors_list.append({'firstname': self.firstname
                            ,'lastname': self.lastname
                            ,'id': self.id
                            ,'subject': self.subject
                            ,'classes': self.classes
                            ,'title': "Mentor"})
        for classes in self.classes:
            class_list.add(classes)

    def ment_command_print():
        for ment in mentors_list:
            mentname = ment['firstname'] + " " + ment['lastname']
            id = ment['id']
            mentclasses = ment['classes']
            if command == mentname or command == id:
                print(f'\nSupervisors of classes which mentor '
                    f'[{mentname} ID: {id}] has lessons with:')
                for classes in mentclasses:
                    for superv in supervisors_list:
                        for classes_s in superv['classes']:
                            if classes == classes_s:
                                print(superv['firstname'] + ' ' 
                                    + superv['lastname'] + ' ID: '
                                    + superv['id'] + "class: "
                                    + classes_s)


class Supervisor:
    def __init__(self):
        self.firstname = input('firstname: ')
        while not self.firstname:
            self.firstname = input('Type correct firstname: ')
        self.lastname = input('lastname: ')
        while not self.lastname:
            self.lastname = input('Type correct lastname: ')
        self.id = input('id: ')
        while not self.id:
            self.id = input('Type correct id: ')
        self.classes = []
        class_input = input('class:')
        while not class_input:
            class_input = input('Type correct class:')
        while class_input:
            self.classes.append(class_input)
            class_input = input('Another class [submit empty line to abort]:')

    def database_add(self):
        supervisors_list.append({'firstname': self.firstname
                            ,'lastname': self.lastname
                            ,'id': self.id
                            ,'classes': self.classes
                            , 'title': "Supervisor"})
        for classes in self.classes:
            class_list.add(classes)

    def class_command_print():
        print('Supervisors:')
        for superv in supervisors_list:
            for classes in superv['classes']:
                if classes == command:
                    f = superv['firstname']
                    l = superv['lastname']
                    i = superv['id']
                    print(f'{f} {l} ID: {i}')

    def superv_command_print():
        for superv in supervisors_list:
            supervname = superv['firstname'] + ' ' + superv['lastname']
            id = superv['id']
            if command == supervname or command == id:
                print(f'\nStudents of supervisor: {supervname} ID: {id}')
                for stud in students_list:
                    if stud['class'] in superv['classes']:
                        f = stud['firstname']
                        l = stud['lastname']
                        i = stud['id']
                        print(f'{f} {l} ID: {i}')


def list_of_users(type_list):
    for user_type in type_list:
        name = user_type['firstname'] + ' ' + user_type['lastname']
        title_and_name = user_type['title'] + ": " + name
        id = user_type['id']
        print(title_and_name + ', ID: ' + id)

def allowed_commands_print():
    print('Allowed commands:')
    print('[NAME OF STUDENT]: shows student\' subjects and mentors')
    print('[NAME OF CLASS]: shows class\' supervisor and students')
    print('[NAME OF SUPERVISOR]: shows supervisor\'s students')
    print('[NAME OF MENTOR]: shows supervisors whose classes have lessons with'
          ' mentor')
    print('Available users(if exact names, enter user ID instead of name)')

def user_input():
    print(f'Allowed user types: {ALLOWED_USER_TYPES}')
    user_type = input('User type:')
    while user_type not in ALLOWED_USER_TYPES:
        print(f'Allowed user types: {ALLOWED_USER_TYPES}')
        user_type = input('Correct user type:')
    print("")
    return user_type


user_type = user_input()
while user_type in ALLOWED_USER_TYPES:
    if user_type == ALLOWED_USER_TYPES[0]:
        stud = Student()
        stud.database_add()
    elif user_type == ALLOWED_USER_TYPES[1]:
        ment = Mentor()
        ment.database_add()
    elif user_type == ALLOWED_USER_TYPES[2]:
        superv = Supervisor()
        superv.database_add()
    elif user_type == ALLOWED_USER_TYPES[3]:
        break
    user_type = user_input()
allowed_commands_print()
list_of_users(mentors_list)
list_of_users(students_list)
list_of_users(supervisors_list)
command = input('\nType command (enter empty line to abort): ')
print("")
while command:
    if command in class_list:
        Supervisor.class_command_print()
        Student.class_command_print()
    else:
        Supervisor.superv_command_print()
        Mentor.ment_command_print()
        Student.stud_command_print()
    command = input('\nType command (enter empty line to abort): ')
    print("")
                        