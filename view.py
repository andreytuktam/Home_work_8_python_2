

def view_pupils():
    print('id ученика:имя ученика/номер класса ученика/успеваемость ученика\n')
    my_file = open("pupils.txt", "r")
    for line in my_file:
        print (line)
    my_file.close()
    

def view_class_new():
    print('id классного руководителя:имя классного руководителя/номер класса классного руководителя/коэфицент успеваемости учеников в классе\n')
    my_file = open("class_new.txt", "r")
    for line in my_file:
        print (line)
    my_file.close()