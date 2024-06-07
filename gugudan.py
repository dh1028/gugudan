import time, random

def gugudan():
    
    life_dic = {"상" : 3, "중" : 2, "하" : 1}
    time_dic = {"상" : 20, "중" : 7, "하" : 2}
    
    print("구구단을 맞춰보세요!\n")
    
    level = input("난이도를 입력하세요 (상/중/하) : ")
    while not (level in life_dic.keys()):
        level = input("(상/중/하) 중 한 글자만 입력해주세요 : ")
    life = life_dic[level]
    time_limit = time_dic[level]
        
    question = input("문제 수를 입력하세요 (3~5) : ")
    while not ("3" <= question <= "5"):
        question = input("3~5의 숫자만 입력해주세요 : ")
    question = int(question)
    question2 = question
    
    print("\n한 문제당 제한 시간은", str(time_limit)+"초이고, 기회는", str(life)+"번입니다.")
    input("시작하려면 엔터 키를 누르세요.")
    print("===========================================")
    
    if level=="상":
        q, w, e, r = 10, 99, 10, 99
    elif level=="중":
        q, w, e, r = 1, 9, 10, 99
    else:    # level=="하"
        q, w, e, r = 1, 9, 1, 9
    
    cnt = 0
    
    while life!=0 and question2!=0:
        a = random.randint(q, w)
        b = random.randint(e, r)
        
        print(a, "x", b, "=", end=" ")
        
        start = time.perf_counter()
        
        ans = input()
        while ans.isdigit()==False:
            ans = input()
        ans = int(ans)
        
        end = time.perf_counter()
        
        Time = end-start
        
        if ans==a*b and Time<time_limit:
            cnt+=1
            print("정답입니다!", end=' ')
        elif ans!=a*b:
            life-=1
            print("틀렸어요...", end=' ')
        else:    #제한 시간 초과
            life-=1
            print("타임 오버!", end=' ')
        print("(남은 기회:", str(life)+")\n")
        
        question2-=1         
        
    if cnt==question:    # 만점
        print("축하합니다. 만점입니다!")
        addition = input("추가 문제에 도전하시겠습니까? (Y/N) : ")
        while addition!="Y" and addition!="N":
            addition = input("(Y/N) 중 한 글자만 입력해주세요 : ")
            
        if addition=="Y":
            addition_f()            
    
    else:
        if life==0:
            print("기회 소진으로 게임이 종료되었습니다.")
        print(str(question)+"문제 중에", str(cnt)+"개 맞췄습니다.")
    print("\n====== 구구단게임을 종료합니다 ======")
    

def addition_f():
    print("\n문제는 빈칸채우기와 연속곱셈 중 랜덤으로 제공됩니다.")
    print("3문제이며, 한 문제당 제한 시간은 5초이고, 기회는 1번입니다.")
    input("시작하려면 엔터 키를 누르세요.")
    print("===========================================")
    
    cnt = 0
    
    for _ in range(3):
        a = random.randint(1, 2)
        if a==1:    #빈칸채우기
            x = random.randint(10, 99)
            y = random.randint(1, 9)
            
            print(x, "x _ =", x*y)
            
            start = time.perf_counter()
            
            ans = input()
            while ans.isdigit()==False:
                ans = input()
            ans = int(ans)
            
            end = time.perf_counter()
            
            Time = end - start
            
            if ans==y and Time<5:
                cnt += 1
                print("정답입니다!\n")
            elif ans!=y:
                print("틀렸어요...\n")
                break
            else:    #제한 시간 초과
                print("타임 오버!\n")
                break
        
        else:    #연속곱셈
            x = random.randint(1, 9)
            y = random.randint(1, 9)
            z = random.randint(1, 9)
            
            print(x, "x", y, "x", z, "=", end=" ")
            
            start = time.perf_counter()
            
            ans = input()
            while ans.isdigit()==False:
                ans = input()
            ans = int(ans)
            
            end = time.perf_counter()
            
            Time = end - start
            
            if ans==x*y*z and Time<5:
                cnt += 1
                print("정답입니다!\n")
            elif ans!=x*y*z:
                print("틀렸어요...\n")
                break
            else:    #제한 시간 초과
                print("타임 오버!\n")
                break
    if cnt==3:
        print("축하합니다. 만점입니다!")
    else:
        print("기회 소진으로 게임이 종료되었습니다.")
        print("3문제 중에", str(cnt)+"개 맞췄습니다.")
    
    
gugudan()
