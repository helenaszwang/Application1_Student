#from .Student import Student


class Student:

    def __init__(self, name, age, hair_length, major, school_name, bbt):
       self.m_name = name
       self.m_age = age
       self.m_hair_length = hair_length
       self.m_major = major
       self.m_school_name = school_name
       self.m_bbt = bbt

    def setName(self, name):
        self.m_name = name

    def setAge(self, age):
        self.m_age = age

    def setHairLength(self, hair_length):
        self.m_hair_length = hair_length

    def setMajor(self, major):
        self.m_major = major

    def setSchoolName(self, school_name):
        self.m_school_name = school_name

    def setBbt(self, bbt):
        self.m_bbt = bbt

    def getName(self):
        return self.m_name

    def getAge(self):
        return self.m_age

    def getHairLength(self):
        return self.m_hair_length

    def getMajor(self):
        return self.m_major

    def getSchoolName(self):
        return self.m_school_name

    def getBbt(self):
        return self.m_bbt


######################################################################
# User enters their information
u_confirm = "no"

while u_confirm == "no":
# User name - WORKING
    u_name = input("What's your name?: ").strip()
    while len(u_name) == 0:
         print("Your name needs to have at least one letter")
         u_name = input("What's your name?:").strip()
    # # User age - WORKING
    u_age = input("What's your age?: ").strip()
    while isinstance(u_age, str):
        try:
            u_age = int(u_age)
        except:
            print("Please enter an integer")
            u_age = input("What's your age?: ").strip()
    while u_age < 0 or u_age > 200:
        print("Your age has to be between 0 to 200")
        u_age = input("What's your age?: ").strip()
        while isinstance(u_age, str):
            try:
                u_age = int(u_age)
            except:
                print("Please enter an integer")
                u_age = input("What's your age?: ").strip()
    # User Hair -  WORKING
    u_hair_length = input("What's your hair length? Please select from short, medium, and long: ").strip().lower()
    while u_hair_length != "short" and u_hair_length != "medium" and u_hair_length != "long":
        print("Please select from short, medium, and long")
        u_hair_length = input("What's your hair length?: ").strip().lower()

    # User Major
    u_major = input("What's your major?: ").strip()
    while len(u_major) == 0:
         print("Please enter your major")
         u_major = input("What's your major?: ").strip()

    # User school name
    u_school_name = input("What's the name of your school?: ").strip()
    while len(u_school_name) == 0:
        print("Please enter the name of your school")
        u_school_name = input("What's the name of your school?: ").strip()

    # User bubble tea
    u_bbt = input("Do you like bubble tea?: ").strip().lower()
    while u_bbt != "no" and u_bbt != "yes":
        print("Please answer Yes or No")
        u_bbt = input("Do you like bubble tea?: ").strip().lower()

    # Confirm user answers
    print("Your name: " + u_name +
          "\nYour age: " + str(u_age) +
          "\nYour hair length: " + u_hair_length +
          "\nYour major: " + u_major +
          "\nYour school name: " + u_school_name +
          "\nLike bubble tea: " + u_bbt)
    u_confirm = input("Is the above information correct?: ").strip().lower()
    while u_confirm != "no" and u_confirm != "yes":
        print("Please answer Yes or No")
        u_confirm = input("Is the above information correct?: ").strip().lower()
    if u_confirm == "yes":
        print("Thank you")

# Enter the number of students
number = input("Please enter the number of students: ").strip()
while isinstance(number, str):
    try:
        number = int(number)
    except:
        print("Please enter an integer")
        number = input("Please enter the number of students: ").strip()
while number < 2 or number > 10:
    print("The number of students should be between 2 to 10")
    number = input("Please enter the number of students: ").strip()
    while isinstance(number, str):
        try:
            number = int(number)
        except:
            print("Please enter an integer")
            number = input("Please enter the number of students: ").strip()
student_list = []
c = 1
while c <= number:
    print("Please enter the information of Student #" + str(c))
    s_confirm = "no"
    while s_confirm == "no":
        student = Student("name", "age", "hair_length", "major", "school_name", "bbt")
        s_name = input("Name: ").strip()
        while len(s_name) == 0:
            print("The name needs to have at least one letter")
            s_name = input("Name: ").strip()
        student.setName(s_name)
#       print(student.getName())

        # age
        s_age = input("Age: ").strip()
        while isinstance(s_age, str):
            try:
                s_age = int(s_age)
            except:
                print("Please enter an integer")
                s_age = input("Age: ").strip()
        while s_age < 0 or s_age > 200:
            print("The age has to be between 0 to 200")
            s_age = input("Age: ").strip()
            while isinstance(s_age, str):
                try:
                    s_age = int(s_age)
                except:
                    print("Please enter an integer")
                    s_age = input("Age:").strip()
        student.setAge(s_age)

        # Hair
        s_hair_length = input("Hair length (Please select from short, medium, and long): ").strip().lower()
        while s_hair_length != "short" and s_hair_length != "medium" and s_hair_length != "long":
            print("Please select from short, medium, and long")
            s_hair_length = input("Hair length: ").strip().lower()
        student.setHairLength(s_hair_length)

        # Major
        s_major = input("Major: ").strip()
        while len(s_major) == 0:
            print("Please enter the major")
            s_major = input("Major: ").strip()
        student.setMajor(s_major)

        # school name
        s_school_name = input("School name: ").strip()
        while len(s_school_name) == 0:
            print("Please enter the name of the student's school")
            s_school_name = input("School name: ").strip()
        student.setSchoolName(s_school_name)

        # bubble tea
        s_bbt = input("Bubble tea preference (Please enter yes or no): ").strip().lower()
        while s_bbt != "no" and s_bbt != "yes":
            print("Please answer Yes or No")
            s_bbt = input("Bubble tea preference: ").strip().lower()
        student.setBbt(s_bbt)

# Confirm answers
        print("Name: " + student.getName(),
              "\nAge: " + str(student.getAge()),
              "\nHair length: " + student.getHairLength(),
              "\nMajor: " + student.getMajor(),
              "\nSchool name: " + student.getSchoolName(),
              "\nLike bubble tea: " + student.getBbt())

        s_confirm = input("Is the above information correct for student #" + str(c) + "?:").strip().lower()
        while s_confirm != "no" and s_confirm != "yes":
            print("Please answer Yes or No")
            s_confirm = input("Is the above information correct for student #" + str(c) + "?:").strip().lower()
        if s_confirm == "yes":
            c += 1
            print("Thank you")
            student_list.append(student)

# Enter common feature (ALL, name, age, hair length, major, school, bbt)
cc = 0
while cc < 10:
    feature = input("What feature would you like to check? Please select from the following: "
                    "\n 1. ALL features"
                    "\n 2. Name"
                    "\n 3. Age"
                    "\n 4. Hair length"
                    "\n 5. Major"
                    "\n 6. School"
                    "\n 7. Bubble tea preference"
                    "\n ").strip()
    if feature < 0 or feature > 7:
        print("Please select from numbers 1 to 7")
        feature = input("What feature would you like to check?"
                        "\n 1. ALL features"
                        "\n 2. Name"
                        "\n 3. Age"
                        "\n 4. Hair length"
                        "\n 5. Major"
                        "\n 6. School"
                        "\n 7. Bubble tea preference"
                        "\n ").strip()

    while isinstance(feature, str):
        try:
            feature = int(feature)
        except:
            print("Please select from numbers 1 to 7")
            feature = input("What feature would you like to check?"
                            "\n 1. ALL features"
                            "\n 2. Name"
                            "\n 3. Age"
                            "\n 4. Hair length"
                            "\n 5. Major"
                            "\n 6. School"
                            "\n 7. Bubble tea preference"
                            "\n ").strip()
    if feature == 1:
        print("All of your features match with:")
        cc += 1
        c1 = 0
        for i in student_list:
            if u_name == i.getName() and u_age == i.getAge() and u_hair_length == i.getHairLength and u_major == i.getMajor() and u_school_name == i.getSchoolName() and u_bbt == i.getBbt:
                print(i.getName())
                c1 += 1
        if c1 == 0:
            print("There is no student who shares all the features with.")

    if feature == 2:
        print("Your name matches with:")
        cc += 1
        c2 = 0
        for i in student_list:
            if u_name == i.getName():
                print(i.getName())
                c2 += 1
        if c2 == 0:
            print("There is no student who has the same name as yours.")

    if feature == 3:
        print ("Your age matches with:")
        cc += 1
        c3 = 0
        for i in student_list:
            if u_age == i.getAge():
                print(i.getName())
                c3 += 1
        if c3 == 0:
            print("There is no student with the same age as you.")

    if feature == 4:
        print("Your hair length matches with:")
        cc += 1
        c4 = 0
        for i in student_list:
            if u_hair_length == i.getHairLength():
                print(i.getName())
                c4 += 1
        if c4 == 0:
            print("There is no student with the same hair length as you.")

    if feature == 5:
        print("Your major matches with:")
        cc += 1
        c5 = 0
        for i in student_list:
            if u_major == i.getMajor():
                print(i.getName())
                c5 += 1
        if c5 == 0:
            print("There is no student with the same major as you.")

    if feature == 6:
        print("Your school matches with:")
        cc += 1
        c6 = 0
        for i in student_list:
            if u_school_name == i.getSchoolName():
                print(i.getName())
                c6 += 1
        if c6 == 0:
            print("There is no student who goes to the same school as you.")

    if feature == 7:
        print("Your bubble tea preference matches with:")
        cc += 1
        c7 = 0
        for i in student_list:
            if u_bbt == i.getBbt():
                print(i.getName())
                c7 += 1
        if c7 == 0:
            print("There is no student with the same bubble tea preference as you.")


# Extract the feature from all students and user
# Use compare function to see if it matches
# If match, return student name, if no match, return None

# MAKE IT A LIST!!

# For ALL, check if all features match with user, if yes, return the name of the student


