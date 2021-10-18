grade = int(input("Please enter your grade?"))
questionNum = int(input("Please enter the number of questions?"))
correctNum = 2
# 判断一下输入是否合法？
for nowNum in range(questionNum):
    # 这里获取随机数 numA numB
    numA = 33
    numB = 3
    # 这里获取符号随机数 sig (0~3)
    sig = "+"
    # 输出算式
    print(numA,sig,numB,"=?")
    ansUser = int(input())
    # correctNum += match((计算的数),（得到的数）)

if questionNum == correctNum:
    print("Excellent! All right, that's great! Your score is 100")
elif correctNum == 0:
    print("Fail! All incorrect. Your score is 0")
else :
    print("Finish! Your score is ", int(correctNum/questionNum*100))