#  介绍类一般一个项目中一个类就作为一个单独文件存储，和函数一样
# 万物皆对象
# 每个对象都有类型
# 程序由通过互相发送消息进行协同工作的若干对象构成
# 每个对象都有各自的存储空间，该信息由对象构成
# 相同类型的对象间可以传递相同类型的消息
from enum import Enum


# 1. 创建一个枚举类型
class Gender(Enum):  # 表示一个继承类

    male = 1
    female = 0


class Job(Enum):
    student = 0
    teacher = 1
    worker = 2
    police = 3
    scientist = 4
    artist = 5


# 2. 创建一个父类，以公民为例,以下idNo认定中国身份证编码方式
# 其中定义的两个函数称作父类的method,本例中这两个函数相当于冗余项，因为可以从idNo中直接提取
# 加__的函数一般是系统自定义函数，因此为了防止重名，自定义函数不要加__
# 在一个类中的属性或者方法定义前面加上’_‘符号，表示这个符号是该类的私有属性和私有方法，无法被继承和调用


# 调用枚举类型时，只需要在文件中声明对枚举类的调用即可--from doc import Enumclass
class Person:
    """User defined class"""

    def __init__(self, idNo='N/A', name='N/A'):
        self.idNo = idNo
        self.iName = name
        self.iGender = Gender.male
        self.job = Job.student
        self.iAge = -1
        self.iBirthday = ''
        if idNo != 'N/A':
            self.idNoToBirth()
            self.GetiAge()
            self.GetGender()
        else:
            print('Please input the Person\'s idNo and Name.')

    def idNoToBirth(self):
        assert isinstance(self.idNo, str)
        assert len(self.idNo) == 18
        idNo = self.idNo
        # self.iBirthday = idNo[6:10] + '-' + idNo[10:12] + '-' + idNo[12:14]
        self.iBirthday = '-'.join((idNo[6:10], idNo[10:12], idNo[12:14]))

    def GetiAge(self):

        assert len(self.iBirthday) == 10
        import datetime
        iBirthday = self.iBirthday
        nowdate = datetime.datetime.now()
        iAge = nowdate.year - int(iBirthday[0:4])
        if nowdate.month >= int(iBirthday[5:7]) and nowdate.day >= int(iBirthday[8:10]):
            self.iAge = iAge
        else:
            self.iAge = iAge - 1

    def GetGender(self):

        assert isinstance(self.idNo, str)
        assert len(self.idNo) == 18
        genderCheck = int(self.idNo[16])
        self.iGender = Gender.male if genderCheck % 2 == 1 else Gender.female

    def description(self):
        print('Person Information :')
        print('Name:%s\t idNo:%s' % (self.iName, self.idNo))
        print('Gender:%s\tJob:%s' % ('Male' if self.iGender == Gender.male else 'Female', self.job))


# 3. 用继承的方式创建Person的子类，作为职业类
#  子类和父类都有的函数，在子类中被重载，当对象属于子类中调用子类的函数
#  一个子类有两个以上的父类的时候叫做多继承，此时Python会根据MRO来查找所属对象的方法或者属性
#  在这两个子类中定义变量或者方法时要注意防止重名
#  MRO原则：（广度优先遍历原则，一个子类有多个父类时，要在定义的时候规定好其查找父类的顺序）
#  1. 子类会先于父类被检查
#  2. 多个父类根据其在MRO列表中的顺序来检查
#  3. 若对于下一个类有两个合法选择，选择第一个父类
class Degree(Enum):
    primary = 0
    junior = 1
    senior = 2
    bachelor = 3
    master = 4
    doctor = 5


class StudentGrade:
    """User defined class Grade:存放高中六学期的成绩单"""

    def __init__(self, sNo='N/A'):
        assert isinstance(sNo, str)
        self.sNo = sNo
        self.report = [{}, {}, {}, {}, {}, {}]

    def GetStudentGrade(self, term, **gradelist):
        assert term and gradelist
        assert 0 < term <= 6

        self.report[term - 1].update(gradelist)
        self.report[term - 1].update(Gradesum=sum(gradelist.values()))

    def ReportStudentGrade(self, term):
        assert self.report  # 非空即真
        assert isinstance(term, int)
        assert 0 < term <= 6
        print('Term:{}, \t Student No: {}'. \
              format(term, self.sNo))
        for subject, scores in self.report[term - 1].items():
            print(subject, ':', scores, end='    ')
        print()


class Student(Person, StudentGrade):
    """User defined class Student"""

    def __init__(self, sNo='N/A', idNo='N/A', name='N/A'):
        # super(Student, self).__init__()
        Person.__init__(self, idNo, name)
        StudentGrade.__init__(self, sNo)
        self.sNo = sNo
        self.school = 'N/A'
        self.degree = Degree.senior

    def description(self):
        print('Student information:')
        print('Name:%s\t IdNo:%s\t sNo:%s' % (self.iName, self.idNo, self.sNo))
        print('Gender:%s\tSchool:%s\t Degree:%s' % ('Male' if self.iGender \
                                                              == Gender.male else 'Female', self.school, self.degree))

    def ReportStudentAllGrade(self):
        assert self.report
        assert isinstance(self.sNo, str)
        assert isinstance(self.iName, str)
        gradeSum = 0
        validNum = 0   # 记录非空的成绩单个数
        for term in range(0, 6):
            if self.report[term]:
                print('The scores of Term %d, Student:%s,   Sno:%s' % (term + 1, self.iName, self.sNo))
                print(self.report[term])
                validNum += 1
                gradeSum += self.report[term]['Gradesum']
            else:
                continue
        if validNum == 0:
            print('{} is new to {}.{} doesn\'t have grade report now.' \
                  .format(self.iName, self.school, 'He' if self.iGender == Gender.male else 'She'))
        else:
            print('{}\'s average grade till now:'.format(self.iName), end=' ')
            print('%.2f' % (gradeSum / validNum))


#  4 抽象类，Abstract Class
#  抽象类相当于对其子类的一种行为规范，该类不能被实例化，而其子类只有在实现了抽象类中定义的抽象方法后，才能被实例化，否则也无法使用。
#  定义抽象方法的时候需要加上@abstractmethod, 由于其函数不被实例化，函数内部一般用pass替代。

from abc import ABC, abstractmethod


class DrawShape(ABC):
    @abstractmethod
    def getSize(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class DrawCircle(DrawShape):
    """A workable instance of ABC  """

    def getSize(self):
        print('Please input the Ra and Rb of the Circle.')

    def draw(self):
        print('Circle drawn.')


class DrawRect(DrawShape, ABC):
    """An unworkable instance of ABC"""

    def getSize(self):
        print('Please input the a and b of the Rect.')


# 5.Property 函数：函数属性化
# 假设在一个类中定义 x=property(fget, fset, fdel, doc),x的具体对象是a
# 调用a.x触发fget函数，a.x=b触发fset函数，del a.x触发fdel函数，doc为属性说明
# 有一个类属性在本例中定义
class RectPot:
    """User defined class using Property"""
    RectCallNum = 0  # 该类自身的属性，记录该类下的对象总数

    def __init__(self, size=(0, 0)):
        self.length, self.width = size

        self.RectCallNum += 1
        RectPot.RectCallNum += 1

    def getRectSize(self):
        return self.length, self.width

    def setRectSize(self, size):
        self.length, self.width = size

        self.area = self.length * self.width

    size = property(getRectSize, setRectSize)

# 6. 类序列化
# 使用__setitem__和__getitem__使得调用类的时候创建类

# class Fab
