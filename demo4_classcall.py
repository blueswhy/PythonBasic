from demo4_myclass import *

# 1. 用类来创建对象
Amy = Person('313201198010230124', 'Amy')
Amy.job = Job.teacher

Amy.description()
print('Birthday:{} \tAge:{}'.format(Amy.iBirthday, Amy.iAge))
# 2. 父类和子类 父类(parent/base/super class)子类（inherited/sub class)
# 子类对象可以调用父类的method，但是父类对象不能调用子类的method
Bob = Student('GZ10021', '31234320000429079X', 'Bob')
Bob.degree = Degree.senior
Bob.school = 'SHGZ'
Bob.description()  # 当父类和子类有同名的method时，执行子类的method

Bob.GetStudentGrade(1, **{'Chinese': 120, 'Math': 130, 'English': 120})
Bob.GetStudentGrade(2, **{'Chinese': 110, 'Math': 135, 'English': 130})
Bob.GetStudentGrade(5, **{'Chinese': 130, 'Math': 145, 'English': 130})

# print(Bob.report)
Bob.ReportStudentGrade(1)
Bob.ReportStudentAllGrade()

# 类的一些简单的函数
print('Class Student\'s base class:', Student.__base__)
print('Class Student\'s base MRO regulation:', Student.__mro__)

# 3. 抽象类函数的调用
# S1 = DrawShape()
C1 = DrawCircle()
# R1 = DrawRect()

# 4. Property 函数和类属性
# 函数中的类属性在调用的时候只在类调用时使用，若其对象也有该属性，则首先找其对象的这个属性而非类的属性
# 若对象没有这个属性，则按照MRO原则找到该类的属性作为对象的属性
R1 = RectPot()
R2 = RectPot()
R3 = RectPot()
R1.size = (10, 20)
# R2.size = (20,30)
# R3.size = (20,10)
print('R1__Size:{}, \t Area:{}'.format(R1.size, R1.area))
print('R2.RectCallNum:', R2.RectCallNum)  # R2没有RN这个属性，因此在object找到属性值为1，再加1得到2
print('RectPot.RectCallNum:', RectPot.RectCallNum)
