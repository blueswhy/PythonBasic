# 时间模块中包含有两个模块,一个是time模块,另外一个是datatime模块
# time模块, 详细可见python Documentation中的time模块介绍
# epoch: Jan 1, 1970, 00:00:00(UTC)
# 表达时间的方式一般有三种: 时间戳timestamp(float类型,秒作为单位), 元组struct_time, 格式化的时间字符串
# struct_time: 含有9个成员, year, mon, mday, hour, min, sec, wday, yday, isdst(后面三个指代周几, 一年中的第几天, 是否为夏令时)
# 其format 表达对应关系如下, 主要用于strftime的格式问题:
# %y 两位数的年份表示(00-99)
# %Y 四位数的年份表示(000-9999)
# %m 月份(01-12)
# %d 月内的某一天(1-31)
# %H 24小时制小时数(0-23)
# %I 12小时制小时数(01-12)
# %M 分钟数(00-59)
# %S 秒数
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化月份名称
# %B 本地完整月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天(001-366)
# %p 本地A.M.或者P.M.的等价符
# %U 一年中的星期数(00-53),一周中的周日作为周始
# %w 星期(0-6), 周日作为周始
# %W 星期(0-6), 周一作为周始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称

# 三种时间之间的转化关系
# gmtime(): 时间戳->struct_time in UTC
# localtime(): 时间戳->struct_time in Local time
# mktime(): struct local time->时间戳
# strftime(): struct time->时间字符串
# strptime(): 时间字符串->struct time

import time

t1 = time.time()
struct_t1 = time.localtime(t1)
format1Str_t1 = time.strftime('%x %X %w-%j-%U-%Z', struct_t1)
format2Str_t1 = time.strftime('%a %m-%d %H:%M:%S %Y %j-%W-%Z', struct_t1)
print('The first timestamp:%f s' % t1)
print('The first timestamp convert to struct time:', struct_t1)
print('The first timestamp convert to format1 string:', format1Str_t1)
print('The first timestamp convert to format2 string:', format2Str_t1)

format3Str_t2 = '2013/10/12 19:09:45'
format3Str = '%Y/%m/%d %H:%M:%S'
struct_t2 = time.strptime(format3Str_t2, format3Str)
print('The second format string time:', format3Str_t2)
print('The second format string convert to struct time:', struct_t2)

# 另外一种特殊时间格式: %a %b %d %H:%M:%S %Y, 记作fstr_asc
# asctime(): struct_time->fstr_asc
# ctime(): time stamp->fstr_asc
print('The first timestamp convert to fstr_asc:', time.ctime(t1))
print('The second struct time convert to fstr_asc:', time.asctime(struct_t2))

t3 = time.time()
print('The seconds during the execution above: %.4f s' % (t3 - t1))

# datetime模块: 对time模块进行重新封装, 提供更多接口, date, time, datetime, timedelta, tzinfo
#               由于time模块转换的基础是时间戳(一个浮点数), 因此表达的时间年限受限于处理器的位宽
import datetime as dt

# class date: year, month, day ::int
# attribute: weekday(), 以周一作为结果0依次输出, 0-6
#            isoweekday(), 以周一作为结果1依次输出, 1-7
#            isocalendar(), 返回元组(Y, M, D)
#            isoformat(), 返回字符串YYYY-MM-DD
print('date.max:{}, date.min:{}'.format(dt.date.max, dt.date.min))
date1 = dt.date(2012, 10, 12)
date2 = date1.replace(month=9)  # 替换原有date对象的若干属性生成一个新的date对象, 原对象不变
print('The first date:{}, after replace:{}'.format(date1, date2))
print('The first date convert to format string:', date1.strftime('%m/%d/%Y'))
# class time: hour[ , minute[ , second[ , microsecond[ , tzinfo]]]] ::int
# 注意上述time列表的嵌套格式, time模块下的时间分辨率为1微秒
# attribute: tzinfo: 指代时间区域信息
#            isoformat(): HH:MM:SS的时间字符串
#            replace(): 同上
#            strftime(): 同time模块的format格式
t1 = dt.time(20, 12, 13, 79)
t2 = t1.replace(minute=23)
print('The first time:{}, the changed time convert to format string:{}'.format(t1, t2.strftime('%X')))
# class datetime: year, month, day[ , time]
# attribute: now(): 本地时间
#            utcnow(): 本地格林威治时间
#            combine(): 根据提供的date和time组建一个datetime对象
#            fromtimestamp(): 时间戳->datetime对象
#            strptime(): 格式化字符串->datetime对象
#            replace(), weekday(), isocalendar(), isoformat():  同上
#            ctime(): 等效于将datetime转化成fstr_asc格式
#            strftime(): datetime对象->格式化字符串
dt1 = dt.datetime.now()
dt2 = dt.datetime.utcnow()
print('The datetime now:', dt1)
print('The datetime of world now:', dt2)
dt3 = dt.datetime(2019, 3, 12, 8, 20)
print('The datetime of specified time:', dt3)
#  字符串转换, 注意datetime()中周几是其成员函数计算出来的, 不需要直接转换为数据
format4Str_t1 = '2017年9月30日星期六8时42分24秒'
format4Str = '%Y年%m月%d日星期六%H时%M分%S秒'
dt4 = dt.datetime.strptime(format4Str_t1, format4Str)
dt5 = dt.datetime(2016, 9, 28, 20, 3, 43)
format5Str = '%B %d, %Y, %I:%M:%S %p'
print('The format4 string: {} convert to datetime: {}'.format(format4Str_t1, dt4))
print('The datetime: {} convert to format5 string: {}'.format(dt5, dt5.strftime(format5Str)))
# class timedelta: 利用该类直接在datetime对象中在days, hour, min, sec, msec, microsec上进行加减, 月份加减需要另外的方法
dt6 = dt5 + dt.timedelta(days=-1)
print('Yesterday before datetime5 is ', dt6)
dlt_dt45 = dt4 - dt5
print('The days between datetime4 and datetime5: ', dlt_dt45.days)
# class tzinfo: timezone 指代时区, 一般格式为tzinfo = UTC(0-23) 以格林威治时间为基准, 划分相应时区
