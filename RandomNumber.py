import random
from fractions import Fraction


def random_num(grade):
    ran_sum = 0;  #随机数结果
    ran_num = 0;  #随机整数
    ran_snum = 0; #随即小数
    ran_snum = (random.random())  #生成随机整数
    ran_num = (random.randint(0, 100))  #生成随机小数
    ran_snum = round(ran_snum, 2)  #小数保留俩位数字
    if grade > 1 and grade < 4:  #如果是低年级
        ran_sum = ran_num
    if grade > 4:   #如果是高年级
       ran_sum = ran_num + ran_snum;
    return  ran_sum

