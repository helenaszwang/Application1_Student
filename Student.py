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









