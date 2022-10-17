
import record as rec
import view 
import view_grades 
import view_teacher 


def main():
    my_file = open("pupils.txt", "a")
    my_file.close()

    my_file_1 = open("class_new.txt", "a")
    my_file_1.close()
    
    count = 1
    count_1 = 100
    flag = True
    while flag == True:
        
        with open("pupils.txt", "r") as file:            
            lines = file.readlines()
            for i in lines:
                b = i.split(":")
                if int(b[0]) >= 1:
                    count = int(b[0]) + 1
        file.close()
    
        with open("class_new.txt", "r") as file_1:            
            lines_1 = file_1.readlines()
            for j in lines_1:
                a = j.split(":")
                if int(a[0]) >= 100:
                    count_1 = int(a[0]) + 1
        file_1.close()
        
        hello = str(input('Для входа в базу данных "школа №70" укажите категорию доступа:\
            \n -введите "1", если вы администратор\
                \n -введите "2", если вы учитель\
                    \n -введите "3", если вы ученик\
                        \n -введите "0" для выхода из программы\n'))
        
        
        
        if hello == '1':    
            request = str(input('Администратор добро пожаловать в базу данных "школа №70":\
                \n -введите "1" для внесения новой записи БД"класс" \
                    \n -введите "2" для внесения новой записи БД"ученик"\
                        \n -введите "3" для просмотра содержимого БД"класс" \
                            \n -введите "4" для просмотра содержимого БД"ученик"\
                                \n -введите "0" для выхода из программы\n'))
            
            if request == '0':
                flag = False
            
            if request == '1':
                class_new = (str(input(" -введите имя классного руководителя:\n"))\
                    + "/" + str(input(" -введите номер класса классного руководителя:\n")))     
                rec.record_class_new(class_new, count_1)
            
            if request == '2':
                pupils = (str(input(" -введите имя ученика:\n"))\
                    + "/" + str(input(" -введите номер класса ученика:\n"))\
                        + "/" + str(input(" -введите успеваемость ученика (5 4 3 2) :\n")))
                rec.record_pupils(pupils, count)
            
            if request == '3':
                view.view_class_new()
                
            if request == '4':
                view.view_pupils()
                
        if hello == '2': 
            t = 0
            while t == 0:
                request_teacher = str(input('Учитель добро пожаловать в базу данных "школа №70":\
                    \n -введите свой id:\
                        \n -для выхода введите "0":\n'))
                if request_teacher.isdigit() and int(request_teacher) == 0:
                    t = 1
                if request_teacher.isdigit() and 100 <= int(request_teacher) <= count_1 - 1:
                    t = 1
                    view_teacher.teacher(request_teacher)
                    t2 = 0
                    while t2 == 0:
                        request_teacher_2 = str(input(' -для внесения оценок введите id ученика:\
                            \n -для выхода введите "0":\n'))
                        if request_teacher_2.isdigit() and int(request_teacher_2) == 0:
                            t2 = 1
                        if request_teacher_2.isdigit() and 1 <= int(request_teacher_2) <= count - 1:
                            t2 = 1
                            view_teacher.find_gr(request_teacher_2)
                        else:
                            print("Введеный id ученика не существует!")
                            # t2 = 0 
                else:
                    print("Введеный id учителя не существует!")
                    # t = 0        
            
        if hello == '3':
            k = 0
            while k == 0:
                request_id_1 = str(input('Ученик добро пожаловать в базу данных "школа №70":\
                    \n -введите свой id:\
                        \n -для выхода введи "0":\n'))
                if request_id_1.isdigit() and 1 <= int(request_id_1) <= count - 1:
                    k = 1
                    request_1 = str(input('Ученик добро пожаловать в базу данных "школа №70":\
                        \n -введите "1" для просмотра своих оценок:\
                            \n -введите "2" для просмотра среднего балла:\
                                \n -введите "0" для выхода в основное меню:\n')) 
                    if request_1 == '1':
                        view_grades.grades(request_id_1)
                        k = 0
                    if request_1 == '2':
                        view_grades.grades_sr(request_id_1)
                        k = 0
                    if request_1 == '0':
                        k = 1
                if request_id_1.isdigit() and int(request_id_1) == 0:
                    k = 1
                else:
                    print("введеный id не существует!")
                    # k = 0 
                    
               
        if hello == '0': 
            flag = False
            
main()