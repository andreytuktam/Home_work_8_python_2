


def teacher(request_teacher):
    print('id учителя:/имя учителя/номер класса ученика\n')
    my_file = open("class_new.txt", "r")
    for line in my_file:
        for i in line.split(":"):
            if i == request_teacher:
                print(line)
                line_t = line.split('/')
                t3 = line_t[2]         
    my_file.close()

    print('список учеников вашего класса:\nid ученика:/имя ученика/номер класса ученика/успеваемость ученика\n')
    my_file_1 = open("pupils.txt", "r")
    for line_1 in my_file_1:
        for j in line_1.split('/'):
            if j in t3:
                print(line_1)    
    my_file_1.close()


def find_gr(request_teacher_2):
    print('id ученика:/имя ученика/номер класса ученика/успеваемость ученика\n')
    my_file_1 = open("pupils.txt", "r")
    for line_1 in my_file_1:
        for j in line_1.split(':'):
            if j == request_teacher_2:
                print(line_1, 'внесите оценки (5 4 3 2):\n')
                new_grade = str(input()) 
                for i in line_1.split('/'):
                    line_2 = line_1.split('/')
                    itog_scet = "/".join(line_2)
                    if i == line_2[3]:
                        line_2[3] = i + " " + new_grade
                        itog = "/".join(line_2)
    my_file_1.close()

    with open('pupils.txt', 'r') as f1, open('pupils_1.txt', 'w') as f2:
        lines = f1.readlines()
        for line in lines:
            line = line.strip()
            print(line)
            if line in itog_scet:
                f2.write(itog)
            else:
                f2.write(line + '\n')
    
    with open('pupils_1.txt', 'r') as f1, open('pupils.txt', 'w') as f2:
        lines = f1.readlines()
        for line in lines:
            line = line.strip()
            f2.write(line + '\n')
    
    
    
    
    
    
    
    
    
    # my_file = open("pupils_copy.txt", "a+")
    # for lineq in my_file:
    #     for i in lineq.split(":"):
    #         if i != request_teacher_2:
    #             print(lineq)
                
    # my_file.close()
    
    
    # my_file = open("pupils_copy.txt", "a")
    # my_file.write(itog)
    # my_file.close()
    
    # my_file = open("pupils.txt", "r")
    # for line in my_file:
    #     print (line)
    # my_file.close()
    
    
                            
                        
                            
                             
                        
                
                
                   
    
    