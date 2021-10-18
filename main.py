from Calculate import calculate
from RandomNumber import random_num
from randomSymbols import random_symbols
from Result import DeResult

grade = int(input("Please enter your grade?"))
questionNum = int(input("Please enter the number of questions?"))
correctNum = 0
# 判断一下输入是否合法？
for nowNum in range(questionNum):
    # 这里获取随机数 numA numB
    numA = random_num(grade)
    numB = random_num(grade)

    # 这里获取符号随机数 sig (0~3)
    sig = random_symbols(grade)

    # 输出算式
    calStr = str(numA)+sig+str(numB)
    print(calStr,"=?")
    ansStd = calculate(calStr)
    print("####ansStd: ",ansStd)
    ansUser = float(input())
    print("####ansUser: ",ansUser)
    if DeResult(ansUser,ansStd) == 1:
        print("####correct")
        correctNum += 1
    # correctNum += DeResult(ansUser,ansStd)

if questionNum == correctNum:
    print("Excellent! All right, that's great! Your score is 100")
elif correctNum == 0:
    print("Fail! All incorrect. Your score is 0")
else :
    print("Finish! Your score is ", int(correctNum/questionNum*100))