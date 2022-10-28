


#Adding classes first

class User:
    name = 'No Name Provided'
    email = ' '
    password = '1234abcd'
    schoolId = '12345'


class Student(User): #All students will have major and year and above
    major = ' '
    year = ' '

class Teacher(User): 
    lectures = ' ' #Stringnumber of lectures
    all_access = True #Teachers have full access to certain things later
