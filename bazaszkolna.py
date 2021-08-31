students_list = list()
student_info_temp = dict()
mentors_list = list()
mentor_info_temp = dict()
supervisors_list = list()
supervisor_info_temp = dict()
class_list = set()
ALLOWED_USER_TYPES = ('student', 'mentor', 'supervisor', 'end')


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

print(f'bazaszkolna.py instruction:')
print(f'Allowed user types: {ALLOWED_USER_TYPES}')
user_type = input('User type:')
while user_type not in ALLOWED_USER_TYPES:
    user_type = input('User type:')
while user_type in ALLOWED_USER_TYPES:
    if user_type == ALLOWED_USER_TYPES[0]:
        stud = Student()
        students_list.append({'firstname': stud.firstname
                            ,'lastname': stud.lastname
                            ,'id': stud.id
                            ,'class': stud.class_no})
        class_list.add(stud.class_no)
    elif user_type == ALLOWED_USER_TYPES[1]:
        ment = Mentor()
        mentors_list.append({'firstname': ment.firstname
                            ,'lastname': ment.lastname
                            ,'id': ment.id
                            ,'subject': ment.subject
                            ,'classes': ment.classes})
        for classes in ment.classes:
            class_list.add(classes)
    elif user_type == ALLOWED_USER_TYPES[2]:
        superv = Supervisor()
        supervisors_list.append({'firstname': superv.firstname
                            ,'lastname': superv.lastname
                            ,'id': superv.id
                            ,'classes': superv.classes})
        for classes in superv.classes:
            class_list.add(classes)
    elif user_type == ALLOWED_USER_TYPES[3]:
        break
    user_type = input('User type:')
    while user_type not in ALLOWED_USER_TYPES:
        user_type = input('User type:')
print('Allowed commands:')
print('[NAME OF STUDENT]: shows student\' subjects and mentors')
print('[NAME OF CLASS]: shows class\' supervisor and students')
print('[NAME OF SUPERVISOR]: shows supervisor\'s students')
print('[NAME OF MENTOR]: shows supervisors whose classes have lessons with'
      ' mentor')
print('Available users(if exact names, enter user ID instead of name)')
for ment in mentors_list:
    name = 'Mentor: ' + ment['firstname'] + ' ' + ment['lastname']
    id = ment['id']
    print(name + ', ID: ' + id)
for stud in students_list:
    name = 'Student: ' + stud['firstname'] + ' ' + stud['lastname']
    id = stud['id']
    print(name + ', ID: ' + id)
for superv in supervisors_list:
    name = 'Supervisor: ' + superv['firstname'] + ' ' + superv['lastname']
    id = superv['id']
    print(name + ', ID: ' + id)
command = input('Type command: ')
if command in class_list:
    print(f'class: {command}')
    print('Supervisors:')
    for superv in supervisors_list:
        for classes in superv['classes']:
            if classes == command:
                f = superv['firstname']
                l = superv['lastname']
                i = superv['id']
                print(f'{f} {l} ID: {i}')
    print('Students:')
    for stud in students_list:
        if stud['class'] == command:
            f = stud['firstname']
            l = stud['lastname']
            i = stud['id']
            print(f'{f} {l} ID: {i}')
else:
    for superv in supervisors_list:
        supervname = superv['firstname'] + ' ' + superv['lastname']
        id = superv['id']
        if command == supervname or command == id:
            print(f'\nStudents of supervisor: {supervname} ID: {id}\n')
            for stud in students_list:
                if stud['class'] in superv['classes']:
                    f = stud['firstname']
                    l = stud['lastname']
                    i = stud['id']
                    print(f'{f} {l} ID: {i}')
    for ment in mentors_list:
        mentname = ment['firstname'] + " " + ment['lastname']
        id = ment['id']
        mentclasses = ment['classes']
        if command == mentname or command == id:
            print(f'Supervisors of classes which mentor '
                  f'[{mentname} ID: {id}] has lessons with:')
            for classes in mentclasses:
                for superv in supervisors_list:
                    for classes_s in superv['classes']:
                        if classes == classes_s:
                            print(superv['firstname'] + ' ' 
                                 + superv['lastname'] + ' ID: '
                                 + superv['id'] + ", classes: "
                                 + superv['classes'])
    for stud in students_list:
        studname = stud['firstname'] + ' ' + stud['lastname']
        id = stud['id']
        studclass = stud['class']
        if command == studname or command == id:
            print(f'Mentors of student [{studname} ID: {id}]')
            for ment in mentors_list:
                for classes in ment['classes']:
                    if classes == studclass:
                        mentname = ment['firstname'] + " " + ment['lastname']
                        id = ment['id']
                        subject = ment['subject']
                        print(f'{mentname} ID: {id}, subject: {subject}')
                        

