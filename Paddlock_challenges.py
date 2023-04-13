#Padlock Challenge 1:
def challenge_1():
    code = 0

    for i in range(1,41):
        print(i)
        code = code + i

    print ("Code:"+ str(code))
    


#Padlock Challenge 2:
def challenge_2():
    code = 0

    for digit1 in range(0,10):
        for digit2 in range(0,10):
            for digit3 in range(0,10):
                if digit1<digit2<digit3:
                    print(str(digit1)+str(digit2)+str(digit3))
                    code = code + 1
    print("Code:"+str(code))
    


#Padlock Challenge 3:
def challenge_3():
    code = 0

    for digit1 in range(0,10):
        for digit2 in range(0,10):
            for digit3 in range(0,10):
                if digit1%2==0 and digit2%2==0 and digit3%2==0:
                    print(str(digit1)+str(digit2)+str(digit3))
                    code = code + 1
    print("Code:"+str(code))  


#Calling the three padlock challenges defined above
challenge_1()
challenge_2()
challenge_3()
