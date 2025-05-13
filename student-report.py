def welcome_message():
    print("Hey there! how are you doin? ")

def name_student():
    student_name = input("Whats your name? ")
    print(student_name)
    return student_name

def return_name_student():
    student_name = input("Whats your name? ")
    return student_name

def student_marks():
    user_marks = input("Whats your score?")
    user_marks1 = input("Whats your score?")
    user_marks2 = input("Whats your score?")
    return user_marks, user_marks1, user_marks2

def add_marks():

    user_marks, user_marks1, user_marks2 = student_marks()
    marks_sum = (user_marks1+user_marks+user_marks2)
    print (marks_sum)
    return marks_sum

def avg_marks():
    marks_sum = add_marks()
    marks_avg = (marks_sum/3)
    print (marks_avg)
    return marks_avg

def grade():
    marks_avg = avg_marks()
    if marks_avg < 200:
        return "B"
    
    else:
        return "A"
    
def student_report_card ():
    student_name = student_name()
    total_marks = add_marks()
    marks_avg = avg_marks()
    student_grade = grade()

    print (f"Name: {student_name}")
    print (f"Total marks: {total_marks}")
    print (f"Average marks: {marks_avg}")
    print (f"Grade: {student_grade}")

welcome_message()
name_student()
return_name_student()
student_marks()
add_marks()
avg_marks()
student_report_card()


