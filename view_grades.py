
def grades(request_id_1):
    print('id ученика:/имя ученика/номер класса ученика/успеваемость ученика\n')
    my_file = open("pupils.txt", "r")
    for line in my_file:
        for i in line.split(":"):
            if i == request_id_1:
                print(line)       
    my_file.close()


def grades_sr(request_id_1):
    my_file = open("pupils.txt", "r")
    for line in my_file:
        for i in line.split(":"):
            if i == request_id_1:
                sr = line.split("/")
                sr_1 = sr[3].split(" ")
                sum = 0
                count_noisdigit = 0
                for j in sr_1:
                    if j.isdigit():
                        sum = sum + int(j)
                    else:
                        count_noisdigit +=1       
                print('ваш средний балл ',sum / (len(sr_1) - count_noisdigit))   
    my_file.close()
    