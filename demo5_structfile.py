# 利用configparser 创建一个结构化文本文件
# PS: 当一个结构化文件中有bool变量时, 最好将bool变量转化成整型变量0/1存储, 防止由于取出成为一个字符串之后失去了其bool属性
#      另外一种在取值时使用 config[section].getboolean('option')转化成bool变量
import configparser
import os


class Score:
    def __init__(self, name, score):
        self.sLessonName = name
        self.score = score


class Student:
    def __init__(self, sno='', name='', age=0):
        self.sNo = sno
        self.sName = name
        self.iAge = age
        self.scores = []

    def addScore(self, lessonName, lessonScore):
        self.scores.append(Score(lessonName, lessonScore))

    def save(self, filename):
        assert self.sNo
        assert self.scores
        data = configparser.ConfigParser()
        sSection = 'Basic'
        data[sSection] = {}
        data[sSection]['sno'] = self.sNo
        data[sSection]['sname'] = self.sName
        data[sSection]['iage'] = str(self.iAge)

        sSection = 'Scores'
        data[sSection] = {}
        data[sSection]['scores.size'] = str(len(self.scores))
        for idx, iscore in enumerate(self.scores):
            data[sSection][f'slessonname[{idx}]'] = iscore.sLessonName
            data[sSection][f'score[{idx}]'] = str(iscore.score)

        sSection = 'Extension'
        data[sSection] = {}
        dataRead = configparser.ConfigParser()
        dataRead.read(filename)
        if dataRead.has_option(sSection, 'iCount'):
            iCount = int(dataRead[sSection]['iCount'])
        else:
            iCount = 0
        data[sSection]['iCount'] = str(iCount + 1)

        with open(filename, 'w') as f:
            data.write(f)

    def load(self, filename):
        dataRead = configparser.ConfigParser()
        dataRead.read(filename)
        sSection = 'Basic'
        self.sNo = dataRead[sSection]['sno']
        self.sName = dataRead[sSection]['sname']
        self.iAge = int(dataRead[sSection]['iage'])

        sSection = 'Scores'
        scoreSize = int(dataRead[sSection].get('scores.size', '0'))
        for idx in range(0, scoreSize):
            slessonname = dataRead[sSection].get(f'slessonname[{idx}]', 'UNKNOWN')
            iscore = float(dataRead[sSection].get(f'score[{idx}]', '0'))
            self.addScore(slessonname, iscore)

        sSection = 'Extension'
        if dataRead.has_option(sSection, 'iCount'):
            iCount = int(dataRead[sSection]['iCount'])
        else:
            iCount = 0
        dataRead.set(sSection, 'iCount', str(iCount + 1))
        with open(filename, 'w') as f:
            dataRead.write(f)


steven = Student('20110012', 'Steven', 20)
steven.addScore('DataStructrue', 83.2)
steven.addScore('C++', 91.2)
steven.addScore('SingleVariableCalculus', 93.3)
filename1 = 'TestDoc' + os.sep + f'{steven.sName}.ini'
steven.save(filename1)

stevenCopy = Student()
stevenCopy.load(filename1)
filename2 = 'TestDoc' + os.sep + 'stevencopy.ini'
stevenCopy.save(filename2)
