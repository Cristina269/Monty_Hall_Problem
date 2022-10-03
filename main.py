import random



ball_located=[]          #所有球的编号

Number_of_Statistics={}     #计数君专属


def counter(list):  #计数君
    for i in ball_located:
        Number_of_Statistics[i] = ball_located.count(i)
    return Number_of_Statistics 


def Generation_number():         #生成球 没用了   
    for i in range(10):
        ball = random.randint(1,3)
        ball_located.append(ball)
    

def choice():           #生成一个选择
    choice = random.randint(1,3)
    return choice


def kill_blank_door(i,choice):  #随机开一个空门,即排除一个错误选项 
    choice_door=choice
    old=[1,2,3]         #三个门的编号123    
    choice_local=old.index(choice_door)       #选择的门的位置 012
    right_local=old.index(i)
    if int(right_local)==int(choice_local): #第一次选择正确
        right_or_left=random.randint(0,1)   
        right_or_left=random.randint(0,1)       #选择kill左边的还是右边的门
        if int(right_or_left)==0:   #kill左边的
            if int(choice_local)==0: #正确的是第一个,就kill最后一个 即2
                old.pop(2)
            else:
                old.pop(int(choice_local)-1)
        elif int(right_or_left)==1:         #kill右边的
            if int(choice_local)==2: #正确的是最后一个,就kill第一个 即0
                old.pop(0)
            else:
                old.pop(int(choice_local)+1)
    else:           #第一次选择错误
        old=[]
        old.append(int(right_local+1))
        old.append(int(choice_local+1))
    remainder=old
    return remainder

        
def change(choice,remainder):           #改变选择  ,接受的是选择的门和剩余的门
    choice_local=remainder.index(choice) #选择的门的位置 01   此时remainder为两个 13 12 23
    if len(remainder)==1:
        choice_2=choice
    else:
        if choice_local==0:
            choice_2=remainder[1]
        elif choice_local==1:
            choice_2=remainder[0]
    return choice_2


def test_guess(choice,choice_2,i):       #检测选择是否正确   
    right_choice=i
    if int(choice_2)==int(right_choice):
        return 1
    else:
        return 0
    
    
    

def main():
    Generation_number()
    n=0
    all_try=0
    for u in range(122222222222222222):
        i = random.randint(1,3)
        choice_1=choice()
        remainder=kill_blank_door(i,choice_1)
        choice_2=change(choice_1,remainder)
        n2=test_guess(choice,choice_2,i)
        all_try=all_try+1
        n=n+n2
        Success_rate=float(n/all_try)
        print('\r','正确的门:',i,'  排除后的门:',remainder,'  第二次选择:',choice_2,'   正确选择次数',n,'  正确率:',Success_rate,end='', flush=True)
        
        
        
main()
