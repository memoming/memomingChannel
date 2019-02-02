

# 안녕하세요, OOO 입니다.

def sayHello ( userName ) :
    myStr = "안녕하세요, " + userName + " 입니다."
    print(myStr)
    return myStr


# A = sayHello("메모밍채널")
# print(A + "<- 요아이가 변수에 담겨있어요")
# ----------------------------------------------------------------------


# return으로 함수를 종료하기

def myFunc ( number ) :
    i = 0
    while(True) :
        i += 1
        print("메롱")
        if( i == number ) :
            return


# A = myFunc(3)
# print(A)

myFunc(7)
