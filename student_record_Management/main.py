### student record management application 


def student_info_input(): # student information input function

    n = int(input("enter total students number"))

    for i in range (n):
        print(f"enter details for student{i+1}")

        student_data = input("enter according id, name, age, subjects ").split(",")
        
        #student string list to dictionary format
        student_info={

            "id":int(student_data[0]),
            "name":student_data[1].strip(),
            "age":int(student_data[2]),
            "subjects":[s.strip() for s in student_data[3:]]
        }
        # inputing all to file 
        with open("student.txt","a") as f:
            f.write(str(student_info)+"\n")
        print(f"all{n}student seved success fully")




def student_scarch(): # student scarch function

    student_id = int(input("enter student id :\n"))
    found = False
    
    with open ("student.txt","r") as f:
        for line in f:
            student = eval(line.strip()) # string to disonari format

            if student["id"] == student_id:
                print("student Found:\n")
                print(student)
                found = True
                break
    if not found:
        print("student not found Plz try again with valid id")



def all_record(): # student all info printing function

    with open("student.txt","r") as f:      
        print(f.read())




def delete_student(): # student deleteng function
    student_id= int(input("enter student id :"))
    with open("student.txt","r")as f:
        lines = f.readlines()

    new_liens=[]
    delete_line=False

    for line in lines:
        student = eval(line.strip())

        if student["id"] != student_id:
                new_liens.append(line)
        else:
            delete_line = True
        
    with open("student.txt","w") as f:
         
         f.writelines(new_liens)

    if delete_line:
        print(f"student id{student_id} is deleted.")
    else:
        print(f"student id {student_id} has not found try again.")

while True:# unnassari caling the functin becuse I have not any GUI
    sele = str(input("plese select what you need\n1. for student info input enter A\n2. for student scarch B\n3. for All student info C\n4. for delete student D\n5. foe exit enter E")).capitalize()

    if sele == "A":
        student_info_input()
    elif sele == "B":
        student_scarch()
    elif sele == "C":
        all_record()
    elif sele == "D":
        delete_student()
    elif sele == "E":
        break
    else:
        print("invalid input")


# it have protential to add more