# -*- coding: utf-8 -*-

# --------------------------------------------------------------
#    Description：
#
#
# --------------------------------------------------------------

# 计算Course Hours
def cur_courseTime(data):
    res = ""
    day = ["", "Monday", "Tuesday", "Wednesday",
           "Thursday", "Friday", "Saturday", "Sunday"]
    beginNo = data[1]
    endNo = data[1]+data[2]-1
    res = "Sections "+str(beginNo)+" to "+str(endNo)+", "+day[int(data[0])]
    return res

# 计算Exam Time


def cur_examTime(data):
    res = data[0].isoformat()+"<br />"+str(data[1])+" - "+str(data[2])
    return res
