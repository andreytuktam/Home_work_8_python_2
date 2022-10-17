

def record_pupils(pupils, count):
    
    my_file = open("pupils.txt", "a")
    my_file.write(str(count) + ":/" + pupils + '/!\n')
    my_file.close()


def record_class_new(class_new, count_1):
    
    my_file_1 = open("class_new.txt", "a")
    my_file_1.write(str(count_1) + ":/" + class_new + '/!\n')
    my_file_1.close()