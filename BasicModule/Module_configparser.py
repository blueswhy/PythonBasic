# 适用于编写和window下ini配置文件格式相同的文件, 类似于一个字典有很多键值对, sections: options-item
# 该文件中, 一个文件可以存储一个对象的全部信息, 并且可以直接对其中的属性进行改动操作
# PS: 在PythonConsule中使用configparser定位文件时, 由于configparser的dir和文件自身目录不同, 需要作path修正如下
#     path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
#     config.read(os.path.join(path, filename))
import configparser
import os
import json

# 查看文件, pycharm中的一个配置文件为例
pycharmIniPath = r'D:\Program Files\PyCharm\PyCharm 2020.1.1\plugins\python\helpers\pydev' + os.sep + 'tox.ini'
configTox = configparser.ConfigParser()
configTox.read(pycharmIniPath)
print('The ini doc\'s available sections as a list: ', configTox.sections())
print('Is tox in configTox: ', 'tox' in configTox)
for key in configTox['tox']:
    print('Section:Tox, key{}, value:{}'.format(key, configTox['tox'][key]))

for x, y in zip(configTox.options('testenv'), configTox.items('testenv')):
    print('Section:testenv, key:{}, value:{}'.format(x, y))

# 创建配置文件: 创建一个configparser对象->存入文件中->对其中的一些值进行修改
TestIniPath = '../demo' + os.sep + 'TestDoc' + os.sep + 'expIni.txt'
configExp = configparser.ConfigParser()
configExp['DEFAULT'] = {'ServerAliveInterval': '45',
                        'Compression': 'yes',
                        'CompressionLevel': '8',
                        'ForwardX11': 'yes'
                        }
configExp['bitbucket.org'] = {'User': 'Bob'}
configExp['topsecret.server.com'] = {'Port': '50022',
                                     'ForwardX11': 'no'
                                     }
with open(TestIniPath, 'w') as f1:
    configExp.write(f1)

# 读取配置文件并修改
configExpU = configparser.ConfigParser()
configExpU.read(TestIniPath)
configExpU.add_section('UserInfo')
UserInfoPath = '../demo' + os.sep + 'TestDoc' + os.sep + 'dictBob.txt'
fUser = open(UserInfoPath, 'r')
UserDictInfo = json.load(fUser)
for option, item in UserDictInfo.items():
    configExpU.set('UserInfo', str(option), str(item))
configExpU.remove_option('topsecret.server.com', 'ForwardX11')
configExpU.set('topsecret.server.com', 'Port', '50024')
TestIniPathU = '../demo' + os.sep + 'TestDoc' + os.sep + 'expIniU.txt'
f2 = open(TestIniPathU, 'w')
configExpU.write(f2)
fUser.close()
f2.close()
