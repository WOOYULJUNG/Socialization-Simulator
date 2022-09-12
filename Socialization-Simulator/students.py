import random

myhurt=0

search=[]

class STUDENT:
    def __init__(self, stdname, idnum, a, b, c, d):
        self.name=stdname
        self.arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.parr=[0]
        self.idnum=idnum
        self.sum=0
        self.talking=[]
        self.answering=[]
        #self.arr[16]=0
        self.isfriend=False
        self.c1=a
        self.c2=b
        self.c3=c
        self.c4=d
        self.hurt=0
        self.retired=False
        self.searched=False
        self.angry=False
    def allowfriend(self):  #친구 수락 함수, 1이상만 가능하던 것에서 친밀도가 확률에 영향을 주는 걸로 바꿈
        if(self.angry==True): return False
        for i in range(0, 16):
            self.sum+=self.arr[i]
        total=self.c1*self.sum+self.c2*self.arr[16]
        for i in range(0, total):
            self.parr.append(0)
        for i in range(0, self.c2*self.arr[16]):
            self.parr[i]=1
        self.sum=0
        if(random.choice(self.parr)==1):
            self.isfriend=True
            return True
        else:
            return False
    def answer(self):  #답장  함수
        if(self.angry==True): return False
        total=self.c3+self.c4*self.arr[16]
        for i in range(0, total):
            self.parr.append(0)
        for i in range(0, self.c4*self.arr[16]):
            self.parr[i]=1
        self.sum=0
        if(random.choice(self.parr)==1):
            if(random.choice(self.parr)==1):
                if(self.arr[16]<3):
                    self.arr[16]+=1
                    return 1
            return 2
        else:
            return 3


KJS=STUDENT("김준섭",0,1,0,0,1)
JYH=STUDENT("정윤호",1,0,1,0,1)
JYH.arr[16]=3
JWY=STUDENT("정우열",2,5,5,5,5)
JDW=STUDENT("정다운",3,5,5,5,5)
LSJ=STUDENT("이상진",4,5,5,5,5)
MSM=STUDENT("문성민",5,5,5,5,5)
SJB=STUDENT("손주빈",6,5,5,5,5)
OKJ=STUDENT("오경준",7,100,1,100,1)
KMJ=STUDENT("권민재",8,1000,1,1000,5)
JIH=STUDENT("장인호",9,5,5,5,5)
LJS=STUDENT("임정섭",10,5,5,5,5)
YJH=STUDENT("양재혁",11,5,5,5,5)
JJJ=STUDENT("정재진",12,5,5,5,5)
KJH=STUDENT("김주호",13,3,5,3,5)
SYS=STUDENT("송용수",14,5,5,5,5)
KHJ=STUDENT("강현준",15,5,5,5,5)

YOU=STUDENT("당신", 16,0,0,0,0)

karr=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,2,2,2,0,2,0,2,0,0,0,0,0],
      [0,0,0,0,2,0,0,0,0,0,2,0,2,0,0,2,0],
      [0,0,0,2,0,2,0,0,0,2,2,2,2,2,0,2,0],
      [0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2,0],
      [0,0,2,0,0,0,0,0,2,0,0,2,2,0,0,0,0],
      [0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
      [0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,2,2,0,0,0,0,0,0,0,2,0,2,0,0],
      [0,0,2,0,2,0,0,2,0,0,0,0,0,0,0,0,0],
      [0,0,0,2,2,0,0,2,0,0,2,0,0,0,2,0,0],
      [0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0],
      [0,0,0,2,2,0,2,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


students=[KJS,JYH,JWY,JDW,LSJ,MSM,SJB,OKJ,KMJ,JIH,LJS,YJH,JJJ,KJH,SYS,KHJ,YOU]

for i in range(0,17):
    for j in range(0,17):
        students[i].arr[j]=karr[i][j]

KJS.talking+=["안녕하세요", "존경합니다", "외출 가능할까요", "여자 친구 있으세요", "저 솔직히 성실하죠", "연세가..?"]
KJS.answering+=["그래 안녕", "그래야지", "안된다", "모른다 마", "머라카노..", "알아서 뭐하게"]
JYH.talking+=["안녕", "내일 놀래?", "롤ㄱ?", "날씨가 좋다", "무슨 노래 들어?","급식 뭔지 알아?"]
JYH.answering+=["오하요우", "와따시랑 그렇게 놀고 싶은건가(킁)", "와따시 롤 못한다능..","마치 피의 축제가 벌어진 것 같군", "이 몸의 취향을 우민은 이해할 수 없다!", "헬 하운드의 머리..랄까? 큭"]
JWY.talking+=["헤이", "내일 외출 ㄱ?",  "롤ㄱ?", "날씨가 잦같은데", "노래 뭐 들음?", "급식 뭐임?"]
JWY.answering+=[] ##이건 니가 해
JDW.talking+=["안녕", "피방 갈래?", "롤ㄱ?", "내일 비오냐?", "노래 장르 뭐 들음?",  "오하요"]
JDW.answering+=["...", "학교에서 할거임", "탑가셈", "내가 어떻게 알아", "재밌는 거", "하지메마시테"]
LSJ.talking+=["안녕", "피방 ㄱ?", "롤ㄱ?", "대프리카 수준", "노래 추천좀", "급식 뭐임?"]
LSJ.answering+=["미친 놈인가", "가시죠", "우후~ 가시죠", "마치의 너의 어머니군", "포켓몬스터 브금 진짜 좋음", "? 2g폰인데?"]
MSM.talking+=["안녕", "내일 무단외출 ㄱ? ", "롤ㄱ?", "귀여운 성민이~~", "영화 추천 좀", "밥 먹을 거임?"]
MSM.answering+=["..?", "왜 시른데", "피파 해야댐", "ㅗㅗ", "몰라 안봐서", " ?? 안 먹을 거임??"]
SJB.talking+=["클로하냐", "칭짬 언제 해채해?", "엠생아", "오리가 얼면?", "니가 없는 거리에는~~", "잊어버리게~~~ 하지 않도록~~"]
SJB.answering+=["아 니 때문에 졌잖아", "안해", "아니거든!", "어떻게 나보다 재미가 없냐", "내가 할일이 없어서", "기억하도록~~~" ]
OKJ.talking+=["헤이 맨", "내일 피방 갈 거임?", "롤챔스 보냐", "여소좀", "노래 추천 좀", "체단실 갈 거임?"]
OKJ.answering+=["뭐", "뭐", "오늘은 꼭 봐야 되는 거임", "뭔 개소리임 갑자기", "ㅇㅇ"]
KMJ.talking+=["안녕", "내일 놀자", "롤ㄱ?", "날씨가 좋다", "노래 추천좀", "저녁 뭐임?"]
KMJ.answering+=["누구세요", "ㄴ ㅗ", "안함 ㅗ", "어쩌라는 거지", "몰라", "니가 찾아"]
JIH.talking+= ["헤이 로리콘!", "피방 ㄱ?", "내가 미드할거임", "노래 추천좀", "나 어때", "저녁 뭐임?"]
JIH.answering+=["아니라고 미친아", "ㅇㅇ", "ㅗㅗ", "태연 거 들으셈", "병신인가", "먹을 만 할걸?"]
LJS.talking+=["섭 섭 왓섭", "꽤 하잖아 너!", "우오오오오 믿고 있었다고 젠장", "절대로 최저군요~", "한대 두대 세대~", "위로 올라갑니다~~ 내려갑니다~~"]
LJS.answering+=["아니 그런 것 좀 하지만", "...", "거른다", "아아아아아아악", "? 이건 뭐임?", "응 졸업논문~~"]
YJH.talking+=["그녀가 준건 사랑 아닌 동정", "인정해 그년 널 사랑하지 않아!", "너무 감정 이입했나봐 이해되지?", "내가 아는 사람 얘기해 줄게", "며칠 전 사랑하는 그녀와 헤어진", "재혁이란 사람"]
YJH.answering+=["뭔데", "시발 닥쳐", "...?", "응 닥쳐~", "아니 정우열임?", "일로와 시발"]
JJJ.talking+=["벌레야", "물세 숙제 내놔", "헤에~ 야르쟈나이카!", "방송부 일 안하냐~`", "양재혁 어떻게 생각해?", "칭짬 존재 이유가?"]
JJJ.answering+=["(꿈틀꿈틀)", "와~~ 숙제 맡겨놨냐~", "우오오오 믿고있었다고 젠장!", "진짜 일안하냐~~", "(먼산)", "뚝배기 이분법 앵글?"]
KJH.talking+=["헤이 급식 뭐임?", "물세 숙제함?" , "롤ㄱ?", "주호 농사 좀 그만 지어~~", "어제 간식 몇번 받음?", "라면 ㄱ?"]
KJH.answering+=["먹을 만 할걸?", "했겠냐 ㅋㅋㅋ", "분토로 와", "ㅗㅗㅗ", "많이 한 8번?", "ㄱ"]
SYS.talking+=["오우 용수쿤 꽤 하자나!", "우열 컴퍼니 살아있음?", "수능 만점 가즈아~~", "의대 붙어도 안 감?", "설대 가즈아~~", "섭쿤 그만 괴롭혀"]
SYS.answering+=["ㅋㅋㅋ시발", "몰라" "가즈아~~", "ㅇ 안감", "가즈아~~~", "니가 못봐서 그러는건데, 걔도 나 괴롭히거든"]
KHJ.talking+=["사딱아", "축제의 꽃은 누구??", "롤ㄱ?", "모쏠은 닥쳐라~~", "Sweet Child", "피방 ㄱ??"]
KHJ.answering+=["ㅗㅗ", "인세인이 아니겠슴까 행님", "ㄱㄱㄱ", "닥쳐라~~`", "O' Mine", "ㅇㅇ"]


def allowfriend(a):
    return a.allowfriend()

def answer(a):
    r=a.answer()
    if(r==1):
        students[16].arr[a.idnum]+=1
        return True
    elif(r==2):
        return True
    else:
        return False

def checkfriend(a,b):   ##### 니가 그래프 그릴때 쓸 함수, 둘이 2이상의 친구인지 확인
    if(a.arr[b.idnum]>=2):
        return True
    else:
        return False

def sumofmyfnum():  ##내 친구 간선 수 
    sum=0
    for i in range(0, 16):
        sum+=students[i].arr[16]
    return sum

def checkallforretire():  ###하루에 끝마다 자퇴하는 학생 확인 후 자퇴시킴 
    for i in range(0,16):
        if(students[i].hurt>5):
            students[i].retired=True

def checkmyhurt():
    cnt=0
    for i in range(0,16):
        if(students[i].retired==False): cnt+=1
    if(cnt==0): return 1
    
    if(myhurt>10):
        return 2
    else:
        return 3
def resetanger():
    for i in range(0,16):
        students[i].isangry=False

def friendkill(): #하루마다 친밀도 0이 되는 친구는 차단됨
    for i in range(0,16):
        if(students[i].arr[16]==0):
            students[i].isfriend=False

def endoftheday():  #니가 하루 단위가 끝날때마다 써야되는 함수, 리턴값이 1이면 모두 자퇴, 리턴값이 2면 내가 자퇴 즉 게임오버, 리턴값이 3이면 걍 진행
    checkallforretire()
    friendkill()
    resetanger()
    return checkmyhurt() 

def canbefriends(a):
    if(a.arr[16]>=1): return True
    else: return False

def searchforfriends(a):
    for i in range(0, 17):
        if(a.arr[i]>=2): return True
    return False

def connectioncheck():
    for i in range(0,16):
        for j in range(0,17):
            if(students[i].arr[j]>=2): return True
    return False

def friendminus(a,b):  ## 친밀도 1 감소
    if(b.arr[a.idnum]!=0):
        a.arr[b.idnum]-=1
        b.arr[a.idnum]-=1

def friendplus(a,b):#친밀도 1 증가
    if(a==JYH or b==JYH or a==b): return
    if(b.arr[a.idnum]!=3):
        a.arr[b.idnum]+=1
        b.arr[a.idnum]+=1

def allfriendsminus(a): ##a의 모든 친밀도 1 감소
    for i in range(0,16):
        if(students[i].arr[a.idnum]!=0):
            students[i].arr[a.idnum]-=1
            a.arr[students[i].idnum]-=1
            
def allfriendsminus(a): ##a에 대한 친밀도 1 증가
    for i in range(0,16):
        friendminus(a,students[i])

def allfriendsplus(a):
    for i in range(0,17):
        friendplus(a,students[i])

def allhurtplus():
    for i in range(0,17):
        students[i].hurt+=1

def allhurtminus():
    for i in range(0, 17):
        if(students[i].hurt>0): students[i]-=1

def battle(a,b):  #싸우는 이벤트
    a.isangry=True
    b.isangry=True
    s=a.name+", "+b.name+" 둘이 싸웠습니다"
    friendminus(a,b)        
    return s

def copycat(a,b,c):  #베끼는 이벤트
    s=a.name+"이(가) "+ b.name + "의 "+c+"를 베꼈습니다"
    friendminus(a,b)
    return s


def weclasssweets(c): #위클레스 이벤트
    global myhurt
    s="위클래스가 "+c+" 를(을) 나눠주어 모두의 자퇴게이지가 감소합니다"
    for i in range(0, 16):
        if(students[i].hurt==0):
            continue
        else:
          students[i].hurt-=1
          
    if(sumofmyfnum()<5):
        s=s+"\n그런데 친구가 없어서 아무도 당신에게 알려주지 않았습니다"
        return s
    if(myhurt>0):
        myhurt-=1
    return s

def lie(a,b):  #허언 이벤트
    s=a.name+"(이)가 " +b+"를(을) 안한다고 허언을 합니다"
    allfriendsminus(a)
    return s
 
def restaurant(srr):
    global myhurt
    while(True):
        r=random.randrange(0,16)
        if(searchforfriends(students[r])):
            break
    s=[r,]
    sr=students[r].name
    for i in range(0, 17):
        if(students[r].arr[i]>=2):
            s.append(i)
            friendplus(students[r], students[i])
    for i in range(1, len(s)):
        sr=sr+', ' + students[s[i]].name
    if(YOU.idnum in s):
        if(myhurt>0):
            myhurt-=1
        return sr+", 오 당신도 "+srr+"에 회식을 하러 갔습니다"
    else:
        myhurt+=1
    return "당신을 빼고 "+sr+" 이상의 아이들이 "+srr+"에 회식을 하러 갔습니다"

def initializesearch():
    for i in range(0, 17):
        students[i].searched=False

def searchpath(s,r,n):
    s.append(students[r])
    students[r].searched=True
    for i in range(0, 17):
        if(students[r].arr[i]>=n and students[i].searched==False and students[i].retired==False):
            searchpath(s,i,n)
    return s

def group(n):
    s=[]
    initializesearch()
    while(True):
        r=random.randrange(0,16)
        if(searchforfriends(students[r])): break
    return searchpath(s,r,n)


def sleeptogether(a,b):
    s=""
    s=s+b.name+"이 "+a.name+"(와)과 잠자리를 같이 했습니다"
    friendplus(a,b)
    return s
            
def jubindrip():
    allfriendsminus(SJB)
    s=""
    r=random.randrange(1, 10)
    if(r==1):
        s=s+"손주빈: 세상에서 가장 가난한 왕은? 최저임금 ㅋㅋㅋ"
    elif(r==2):
        s=s+"손주빈: 세상에서 가장 뜨거운 전화는? 화상전화 ㅋㅋㅋ"
    elif(r==3):
        s=s+"손주빈: 주빈 올림....반올림? 내림? ㅋㅋㅋㅋㅋ"
    elif(r==4):
        s=s+"손주빈: 곰이 사과를 어떻게 먹나? '베어' 먹지 ㅋㅋㅋㅋ"
    elif(r==5):
        s=s+"손주빈: 우열이는 우열을 가리지 않아!! ㅋㅋㅋ"
    elif(r==6):
        s=s+"손주빈: 혼자 다니는 곤충은? '아싸' 호랑나비! ㅋㅋㅋ"
    elif(r==7):
        s=s+"손주빈: 재선이가 재선을 막는다! ㅋㅋㅋ"
    elif(r==8):
        s=s+"손주빈: 회 잘뜨는 곳은? 회전문 ㅋㅋㅋ"
    elif(r==9):
        s=s+"정창훈 파이어뱃: Ah~ Yeah!" 
    return s

def talkwithJWY(a):
    a.retired=True
    s=""
    s="정우열이 " +a.name+ "와(과) 대화를 해 "+a.name+"이 자퇴하였습니다"
    return s

def inhotakesock(a):
    friendminus(JIH,a)
    s="장인호가 "+a.name+"의 양말을 신었습니다"
    return s

def lolcarry(a): #a의 자퇴여부 확인
    allfriendsplus(a)
    s=a.name+"가(이) 롤을 캐리했습니다"
    return s

def dfJYH(): #정윤호 자퇴 여부 확인 필요, 정윤호와의 친밀도 1 유지 안할 시 발생 가능
    JYH.hurt+=1
    s="정윤호가 혼자서 던파를 해 마음의 상처를 받았습니다"
    return s

def solrank(a): #a의 자퇴여부 확인 필요
    a.isangry=True
    a.hurt+=1
    s=a.name+"이(가) 솔랭이 망해 화가 났습니다"
    return s

def testdate():
    for i in range(0,16):
        students[i].isangry=True
    s="시험기간이라 모두가 화가 나있습니다"
    return s

def weclass(): #위클래스 질문: 주인공과 친하다고 생각하는 사람?
    global myhurt
    s=""
    cnt=0
    for i in range(0,16):
        if(students[i].retired==False and students[i].arr[16]>=1):
            s=s+students[i].name +  ' '
            if(myhurt>0):
                myhurt-=1
            cnt+=1
    if(cnt>0): s=s+": 저요!"
    if(cnt==0):
        s=s+"아무도 당신을 지목하지 않았습니다"
        myhurt+=1
    return s

def laundry(a):#빨래가 안오면 당연히 화가 나지, 자퇴 여부 확인 필요
    s=a.name+"의 빨래가 오지 않아 화가 난 상태입니다"
    a.isangry=True
    a.hurt+=1
    return s

def laundryall():
    s="모두 빨래가 오지 않아 화가 난 상태입니다"
    for i in range(1,17):
        students[i].isangry=True
    allhurtplus()
    return s

def molphone(a): #몰폰하다 뺐김 김준섭, a 자퇴여부 확인 필요
    s=a.name+"이(가) 자습 중 몰폰을 하다 걸렸습니다"
    a.isangry=True
    KJS.isangry=True
    return s

def goback(a,b): #a, b 모두 자퇴 여부 확인 필요
    s=a.name+"이 "+b.name+"에게 숨겨둔 마음을 고백했습니다..!"
    if(a.arr[b.idnum]!=3):
        s=s+"\n"+a.name+"이(가) 자퇴합니다"
        a.retired=True
    else:
        s=s+"\n"+"둘은 사랑의 도피를 합니다"
        a.retired=True
        b.retired=True
    return s

def getclassseat(): #수업시간 13자리 채우기... 그래프 기반 이 중 없는 숫자가 앉을 수 있는 자리 나머지는 니가 구현 가능할거라 본다
    s=[]
    initializesearch()
    while(True):
        while(True):
            r=random.randrange(1,16)
            if(students[r].retired==False and students[r].searched==False): break
        if(len(s)>=13): return s
        s.append(r)
        students[r].searched=True
        for i in range(1, 17):
            if(students[r].arr[i]>=2 and students[i].searched==False):
                students[i].searched=True
                if(len(s)>=13): return s
                s.append(i)            
    return s
        
        
        
def randomevents():
    while(True):
        c=random.randrange(1, 101)
        if(1<=c<5): #싸움 이벤트
            d=random.randrange(1,10)
            if(d<=4 and LJS.retired==False and SYS.retired==False):
                return battle(LJS, SYS)
            elif(d==5 and SYS.retired==False and JJJ.retired==False):
                return battle(SYS, JJJ)
            elif(6<=d and d<8 and LSJ.retired==False and JJJ.retired==False):
                return battle(LSJ, JJJ)
            if(8<=d and LJS.retired==False and JYH.retired==False):
                return battle(LJS, JYH)
        elif(5<=c<=8): #숙제 베끼기 이벤트
            d=random.randrange(1,4)
            if(d==1):
                return copycat(JIH, JYH, "자구숙제")
            if(d==2):
                return copycat(LSJ, JJJ, "알고리즘 숙제")
            else:
                return copycat(JYH, JJJ, "물리 세미나 숙제")
        elif(9<=c<=14): #위클래스 간식 이벤트
            d=random.randrange(1,4)
            if(d==1):
                return weclasssweets("뻥이요")
            elif(d==2):
                return weclasssweets("초콜릿")
            else:
                return weclasssweets("96년산 와인")
        elif(15<=c<=25): #허언 이벤트
            d=random.randrange(1,3)
            if(d==1 and JWY.retired==False):
                return lie(JWY, '롤')
            elif(d==2 and JYH.retired==False):
                return lie(JYH, '던파')
        elif(26<=c<=30 and connectioncheck()): #회식 이벤트
            d=random.randrange(1,15)
            if(d==1): return restaurant("김스타치킨")
            elif(d==2): return restaurant("인생치킨")
            elif(d==3 or d==4): return restaurant("푸주옥")
            elif(d>=5 and d<=12): return restaurant("피씨방")
            elif(d==13): return restaurant("국밥집")
            elif(d==14): return restaurant("미스터피자")
        elif(31<=c<=38): #같이 자는 이벤트
            d=random.randrange(1,3)
            if(d==1 and SYS.retired==False and JWY.retired==False): return sleeptogether(SYS, JWY)
            elif(d==2 and JJJ.retired==False and LSJ.retired==False): return sleeptogether(JJJ, LSJ)
        elif(39<=c<=50 and SJB.retired==False): #주빈이 개드립 이벤트
            return jubindrip()
        elif(50<=c<=50): #정우열의 자퇴시키기 이벤트
            while(True):
                r=random.randrange(0,16)
                if(r!=1): break
            if(students[r].retired==False):
                return talkwithJWY(students[r]) #정우열이나 김준섭 선생님도 가능한 형태
        elif(51<=c<=59 and JIH.retired==False): #장인호 양말 가져가는 이벤트
            while(True):
                r=random.randrange(0,16)
                if(students[r].retired==False and students[r]!=JIH and students[r]!=KJS): break
            return inhotakesock(students[r])
        elif(60<=c<=67):#lolcarry 이벤트
            while(True):
                r=random.randrange(0,16)
                if(students[r].retired==False and students[r]!=SJB and students[r]!=SYS and students[r]!=JYH): break
            return lolcarry(students[r])
        elif(68<=c<=75 and JYH.retired==False and JYH.arr[16]<1): #던파혼자하는 이벤트
            return dfJYH()
        elif(76<=c<=80):#솔랭 망함
            while(True):
                r=random.randrange(0,16)
                if(students[r].retired==False and students[r]!=SJB and students[r]!=SYS and students[r]!=JYH): break
            return solrank(students[r])
        elif(81<=c<=83):#시험기간
            return testdate()
        elif(83<=c<=84):#위클친한친구는?
            s="위클: 주인공과 친한 사람?"
            s=s+"\n"+weclass()
            return s
        elif(85<=c<=88):
            while(True):
                r=random.randrange(1,17)
                if(students[r].retired==False): break
            return laundry(students[r])
        elif(88<=c<=90):
            return laundryall()
        elif(91<=c<=99 and KJS.retired==False):
            while(True):
                r=random.randrange(1,17)
                if(students[r].retired==False): break
            return molphone(students[r])
        elif(c==100):
            c=random.randrange(1,3)
            if(c==1 and SYS.retired==False and JJJ.retired==False):
                return goback(SYS, JJJ)
            if(c==2 and OKJ.retired==False and KWY.retired==False):
                return goback(OKJ, JWY)
            


    
    

if __name__ == "__main__":
    #print(SJB.name)
    #if(checkfriend(LSJ, SJB)):
    #    print(True)
    #else:
     #   print(False)
     print(SYS.talking[1])
     #print(SJB.retired)
     #talkwithJWY(SJB)
     #print(getclassseat())
     #print(weclass())
    

 
            
