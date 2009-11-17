#!/usr/bin/python
"""
project euler
http://projecteuler.net
"""
import sys
import time
import math
import copy
import random
import bisect
def Permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
def TestPermutations():
    l = '9876543210'
    for i in Permutations(l[2:-1]):
        print i
#TestPermutations()

def BinSearch(arr,x,low,high):
    if high < low:return -1
    m = (low+high)//2
    if arr[m] == x:return m
    elif arr[m] > x:high = m-1
    else: low = m + 1 
    return  BinSearch(arr,x,low,high)
def PrimeSieve_o(n):
    lf = [0]*n
    res = []
    for i in xrange(2,n):
        if lf[i] == 0:
            res.append(i)
            j = i+i
            while j<n:
                lf[j] = 1
                j+=i
    return res

def PrimeSieve(n):
    if n < 2:return []
    sb = ((n-1)>>1)+1
    l = [0]*sb
    cn = (int(math.floor(math.sqrt(n))-1)>>1)
    for i in xrange(1,cn+1):
        if l[i] == 0:
            for j in xrange(2*i*(i+1),sb,2*i+1):
                l[j] = 1
    res = [2]
    for i in xrange(1,sb):
        if l[i] == 0:
            res.append(2*i+1)
    return res
def TestPrimeSieve():
    N = 1000000
    s = time.time()
    l = PrimeSieve_o(N)
    e = time.time()
    print len(l),sum(l), e-s

    s = time.time()
    l = PrimeSieve(N)
    e = time.time()
    print len(l),sum(l),e-s
#TestPrimeSieve()

def IsPrime(n):
    if n == 1:return False
    elif n < 4: return True
    elif (n&1) == 0: return False
    elif n < 9 : return True
    elif (n%3) == 0: return False
    else:
        r = int(math.floor(math.sqrt(n)))
        f = 5
        while f <= r:
            if (n%f)==0:return False
            if (n%(f+2)) == 0:return False
            f+=6
    return True
def isp(n):
    if (n&1) == 0:return False
    for i in range(3,int(math.sqrt(n)+1),2):
        if (n%i) == 0:return False
    return True
def GCD(a,b):
    if b==0:return a
    return GCD(b,a%b)

def p1(n):
    sum(n for i in range(n) if i%3==0 or i%5==0)

def p2():
    a = 1
    b = 2
    sum = 0
    while b < 4000000:
        if (b&1) == 0:
            sum += b
        a += b
        a,b = b,a
    return sum

def p3():
    N = 600851475143
    sq = int(math.sqrt(N)+1)
    while sq > 2:
        if (N%sq)!=0:
            sq-=2
            continue
        if isp(sq):
            break;
        sq-=2
    return sq

def p4():
    max_v = 0
    for i in xrange(100,1000):
        for j in xrange(i,1000):
            s = str(i*j)
            if s == s[::-1]:
                if max_v < i*j: max_v = i*j
    return max_v

def p5():
    l = [2,3,5,7,11,13,17,19]
    ca = [0]*21
    for i in range(1,21):
        for j in l:
            ca[j] = max(ca[i],int(math.floor(math.log(i)/math.log(j))))
    res =1
    for i,v in enumerate(ca):
        res*=i**v
    return res

def p6(n):
    return ((1+n)*n/2)**2-n*(n+1)*(2*n+1)/6

def p7(n):
    l = [2]
    c = 3
    while len(l) < n:
        f = True
        m = int(math.sqrt(c)+1)
        for j in l:
            if j > m: 
                break
            if (c%j) == 0:
                f = False
                break
        if f:
            l.append(c)
        c+=2
    return l[-1]

def p8():            
    str='\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

    max_v = 0
    l = [int(s) for s in str]
    for x in range(len(l)-5):
        v = reduce(lambda x,y:x*y,[l[x + i] for i in range(5)])
        if max_v < v:max_v = v
    return max_v

def p9(n):
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            k = n - i - j
            if k < j: break
            if i**2 + j**2 == k**2:
                print i,j,k,i*j*k


def p10():
    sum = 2+3
    f =	5 
    while f < 2000000:
        if IsPrime(f):
            sum += f
        f+=2
        if IsPrime(f):
            sum += f
        f+=4
    return sum	
def p11():
    ll =[ 
        [ 8 , 2 , 22 , 97 , 38 , 15 , 0 , 40 , 0 , 75 , 4 , 5 , 7 , 78 , 52 , 12 , 50 , 77 , 91 , 8 ],
        [ 49 , 49 , 99 , 40 , 17 , 81 , 18 , 57 , 60 , 87 , 17 , 40 , 98 , 43 , 69 , 48 , 4 , 56 , 62 , 0 ],
        [ 81 , 49 , 31 , 73 , 55 , 79 , 14 , 29 , 93 , 71 , 40 , 67 , 53 , 88 , 30 , 3 , 49 , 13 , 36 , 65 ],
        [ 52 , 70 , 95 , 23 , 4 , 60 , 11 , 42 , 69 , 24 , 68 , 56 , 1 , 32 , 56 , 71 , 37 , 2 , 36 , 91 ],
        [ 22 , 31 , 16 , 71 , 51 , 67 , 63 , 89 , 41 , 92 , 36 , 54 , 22 , 40 , 40 , 28 , 66 , 33 , 13 , 80 ],
        [ 24 , 47 , 32 , 60 , 99 , 3 , 45 , 2 , 44 , 75 , 33 , 53 , 78 , 36 , 84 , 20 , 35 , 17 , 12 , 50 ],
        [ 32 , 98 , 81 , 28 , 64 , 23 , 67 , 10 , 26 , 38 , 40 , 67 , 59 , 54 , 70 , 66 , 18 , 38 , 64 , 70 ],
        [ 67 , 26 , 20 , 68 , 2 , 62 , 12 , 20 , 95 , 63 , 94 , 39 , 63 , 8 , 40 , 91 , 66 , 49 , 94 , 21 ],
        [ 24 , 55 , 58 , 5 , 66 , 73 , 99 , 26 , 97 , 17 , 78 , 78 , 96 , 83 , 14 , 88 , 34 , 89 , 63 , 72 ],
        [ 21 , 36 , 23 , 9 , 75 , 0 , 76 , 44 , 20 , 45 , 35 , 14 , 0 , 61 , 33 , 97 , 34 , 31 , 33 , 95 ],
        [ 78 , 17 , 53 , 28 , 22 , 75 , 31 , 67 , 15 , 94 , 3 , 80 , 4 , 62 , 16 , 14 , 9 , 53 , 56 , 92 ],
        [ 16 , 39 , 5 , 42 , 96 , 35 , 31 , 47 , 55 , 58 , 88 , 24 , 0 , 17 , 54 , 24 , 36 , 29 , 85 , 57 ],
        [ 86 , 56 , 0 , 48 , 35 , 71 , 89 , 7 , 5 , 44 , 44 , 37 , 44 , 60 , 21 , 58 , 51 , 54 , 17 , 58 ],
        [ 19 , 80 , 81 , 68 , 5 , 94 , 47 , 69 , 28 , 73 , 92 , 13 , 86 , 52 , 17 , 77 , 4 , 89 , 55 , 40 ],
        [ 4 , 52 , 8 , 83 , 97 , 35 , 99 , 16 , 7 , 97 , 57 , 32 , 16 , 26 , 26 , 79 , 33 , 27 , 98 , 66 ],
        [ 88 , 36 , 68 , 87 , 57 , 62 , 20 , 72 , 3 , 46 , 33 , 67 , 46 , 55 , 12 , 32 , 63 , 93 , 53 , 69 ],
        [ 4 , 42 , 16 , 73 , 38 , 25 , 39 , 11 , 24 , 94 , 72 , 18 , 8 , 46 , 29 , 32 , 40 , 62 , 76 , 36 ],
        [ 20 , 69 , 36 , 41 , 72 , 30 , 23 , 88 , 34 , 62 , 99 , 69 , 82 , 67 , 59 , 85 , 74 , 4 , 36 , 16 ],
        [ 20 , 73 , 35 , 29 , 78 , 31 , 90 , 1 , 74 , 31 , 49 , 71 , 48 , 86 , 81 , 16 , 23 , 57 , 5 , 54 ],
        [ 1 , 70 , 54 , 71 , 83 , 51 , 54 , 69 , 16 , 92 , 33 , 48 , 61 , 43 , 52 , 1 , 89 , 19 , 67 , 48 ]]
    r = len(ll)
    c = len(ll[0])
    dr = (0,1,1,-1,-1,1)
    dc = (1,0,1,-1,1,-1)
    max_v = 0
    for i in range(r):
        for j in range(c):
            for k in range(len(dc)):
                u = i
                v = j
                st = max_v
                try:
                    s_t = reduce( lambda x,y:x*y,[ll[u+dr[k]*kk][v+dc[k]*kk] for kk in range(4)])
                except:
                    pass
                if max_v < s_t:max_v = s_t
    return max_v

def p12():
    def	CountOfDivisors(n):
        s = 1
        p = 2
        while p**2 <= n and n > 1:
            cc = 0
            if (n%p)==0:
                cc+=1
                n/=p
                while (n%p)==0:
                    cc+=1
                    n/=p
            if p == 2:p=3
            else: p+=2
            s*=(cc+1)
        if n > 1:s*=2
        return s
    #print CountOfDivisors(28)
    i = 8
    while True:
        n = (((1+i)*i)>>1)
        if CountOfDivisors(n) > 500:
            return n
        i+=1



def p13():	
    ss = """37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690"""

    return str(sum([int(s) for s in ss.split('\n')]))[:10]


def p14 ():	
    d = {1:1}
    def f(n):
        if n in d:
            return d[n]
        else:
            if (n&1)==0:
                t = 1+f(n>>1)
            else:
                t = 1+f(3*n+1)
            d[n] = t
            return t

    for x in xrange(2,1000000):
        if x in d:
            continue
        else:
            f(x)
            continue
        #else:
            k = x
            cc = 0
            flag = True
            while k != 1:
                if (k&1) == 0:
                    k>>=1
                else:
                    k = (k<<1)+k+1
                cc+=1
                if k in d:
                    d[x] = cc + d[k]
                    flag = False
                    break
            if flag:d[x] = cc
    max_v = 0
    res = -1
    for k,v in d.iteritems():
        if v > max_v:
            max_v = v
            res = k
    return res

def p15():
    N = 20 + 1
    mp = [[0]*N for i in range(N)]
    for i in range(N):
        mp[i][0] = mp[0][i] = 1
    for i in range(1,N):
        for j in range(1,N):
            mp[i][j] = mp[i-1][j]+mp[i][j-1]
    return mp[N-1][N-1]

def p16():
    return sum(int(s) for s in str(2**1000))

def p17():
    def gl(n):
        l = ([0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8],[6, 6, 5, 5, 5, 7, 6, 6, 7])
        if n == 1000:return 11
        elif n%100 == 0:return l[0][n/100]+7
        elif n > 100:return l[0][n/100]+10+gl(n%100)
        elif n < 20:return l[0][n]
        else: return l[1][n/10-2]+l[0][n%10]
    return sum(gl(i) for i in range(1,1001))

#print p17()

def p18():
    f = open('triangle.txt','r')
    d = [] 
    for l in f.readlines(): 
        d.append(map(lambda c:int(c), [c for c in l.strip().split(' ')]) )
    ld = len(d)
    for i in range(ld-1,0,-1):
        for j in range(i):
            d[i-1][j] = max(d[i][j]+d[i-1][j],d[i][j+1]+d[i-1][j])
    return d[0][0]

#print p18()	

def p19():
    def day_of_week(y,m,d):
        # 0 == Sunday,y>1752
        offset = (0,3,2,5,0,3,5,1,4,6,2,4)
        if m < 3:y-=1
        return (y+y/4-y/100+y/400+offset[m-1]+d)%7
    #print day_of_week(1900,1,1),day_of_week(2009,10,28)
    return sum(1 for i in range(1901,2001) for j in range(1,13) if day_of_week(i,j,1) == 0)

#print p19()

def p20():
    return sum(int(c) for c in str(reduce(lambda x,y:x*y,[i for i in range(1,101)])))

#print p20()

def SumOfProperDivisors(n):
    def SumOfDivisors(n):
        sum = 1
        p = 2
        while p*p<=n and n>1:
            if (n%p)==0:
                j = p**2
                n /= p
                while (n%p)==0:
                    j*=p
                    n/=p
                sum*=(j-1)
                sum/=(p-1)
            if p == 2:
                p=3
            else:
                p+=2
        if n>1 :sum*=(n+1)
        return sum
    return SumOfDivisors(n) - n 

#print ' SumOfProperDivisors -->>', SumOfProperDivisors(72)
def p21 ():	
    N = 10000
    d = {}
    for i in range(1,N):
        d[i] = [1]
    for i in range(2,N):
        j = i+i
        while j < N:				
            d[j].append(i)
            j+=i
        d[i] = sum(d[i])
    d[1] = 1
    #print d[220],d[284]
    s = set()
    res = 0
    for i in range(1,N):
        #if i in s:continue		
        su = d[i]
        if su <= i or su >= N:continue		
        if i == d[su]:
            s.add(i)
            s.add(su)
            res += (i + su)
    return res

def p21_2():
    sum = 0
    for x in range(1,10000):
        y = SumOfProperDivisors(x)
        if y > x:
            if x == SumOfProperDivisors(y):
                sum += x+y
    return sum
#print p21()
#print p21_2()		

def p22():
    f = open('names.txt','r')
    l = map(lambda s:s.strip('"'),f.readlines()[0].split(','))
    l.sort()
    su = 0
    for i,v in enumerate(l):
        su += sum(ord(s)-ord('A')+1 for s in v) * (i+1)
    return su
#print p22()

#4179871
def p23():
    magic_num = 28123 + 1
    la = [i for i in range(magic_num) if SumOfProperDivisors(i) > i]
    la.remove(0)
    res = magic_num*(magic_num-1)/2
    lf = [0] * magic_num
    le = len(la)
    for i in range(le):
        for j in range(i,le):
            t = la[i] + la[j]
            if t < magic_num:
                lf[t] = 1
            else: break
    return res - sum(i for i,v in enumerate(lf) if v == 1)

#print p23()

def p24():
    def Factorial(n):
        return reduce(lambda x,y:x*y,[i for i in range(1,n+1)],1)
    N = 10 
    M = 1000000
    fact = [Factorial(i) for i in range(N)]
    l = [i for i in range(N)]
    k = M - 1
    ll = []
    for i in range(N):
        if fact[N-1-i] > k:
            ll.append(l[i])
        else:
            break
    l = [ x for x in l if x not in ll]
    while k > 0:
        if fact[len(l)-1] <= k:
            t = k/fact[len(l)-1]
            ll.append(l[t])
            k%=fact[len(l)-1];
        else:
            ll.append(l[0])
        l = [ x for x in l if x not in ll]
    ll += l
    #print ll
    return reduce(lambda x,y:x*10+y,ll,0)

#print p24()

def p25():
    a = 1
    b = 2
    cc = 4
    while True:
        a += b
        if len(str(a)) >= 1000:
            return cc
        a,b = b,a
        cc+=1

#print p25()


def p26():
    def CycleL(n):
        l = []
        x = 1
        while x > 0:
            while x<n:
                x*=10
            if x not in l:l.append(x)
            else: return len(l) - l.index(x)
            x%=n
        return 0 
    #print CycleL(6),CycleL(7),CycleL(8),CycleL(9),CycleL(2)
    m_v = 0
    r = 0
    for x in range(1,1000):
        t = CycleL(x)
        if t > m_v:
            m_v = t
            r = x
    #print r,x
    return r



#print p26()

def p27():
    max_v = 0
    ab = 0
    lb = [ i for i in range(2,1000) if IsPrime(i)]
    for a in range(-999,1000):
        for b in lb:
            cc = 0
            n = 0
            while True:
                t = n*(n+a)+b
                if t > 0 and IsPrime(t):
                    cc+=1
                else:
                    break
                n+=1
            if max_v < cc:
                max_v = cc
                ab = a*b
    return ab


#print p27()

def p28():
    N = 1001+1
    sum = 1
    t = 1
    for n in range(3,N,2):
        sum+=(t<<2)+(n-1)*10
        t+=4*(n-1)
    return sum
    for n in range(3,N,2):
        for i in range(4):
            t+=(n-1)
            sum+=t
    return sum

#print p28()

def p29():
    s = set()
    for a in range(2,101):
        for b in range(2,101):
            s.add(a**b)
    return len(s)
#print p29()

def p30():
    sum = 0
    for n in range(2,295245):
        s_t = 0
        for i in [ord(c)-ord('0') for c in str(n)]:
            s_t += i**5
        if n==s_t:
            sum+=n
    return sum
#print p30()
def p31():
    coin = (1,2,5,10,20,50,100,200)    
    l = [0]*201
    l[0] = 1
    for c in coin:
        for i in range(c,201):
            l[i] += l[i-c]
    return l[200]

#print p31()

def p32():
    sum = 0
    for x in range(1234,9876):
        ce = int(math.ceil(math.sqrt(x)))
        for i in range(2,ce):
            if x %i ==0:
                st = str(x)+str(i)+str(x/i)
                s = set(st)
                if len(st) == 9 and ('0' not in s) and len(s) == 9:
                    sum += x
                    break
    return sum
#print p32()

def p33():
    def GCD(a,b):
        if b==0:return a
        return GCD(b,a%b)
    def tf(i,j,u,v,x,y):
        return (j*10+v > i*10+u) and (x*(j*10+v) == y*(i*10+u))
    x,y = 1,1
    for i in range(1,10):
        for j in range(i,10):
            for u in range(1,10):
                for v in range(1,10):
                    if u == j and tf(i,j,u,v,i,v):
                        x,y = i*x,v*y
                    elif v == i and tf(i,j,u,v,u,j):
                        x,y = x*u,y*j
                    elif u == v and tf(i,j,u,v,i,j):
                        x,y = x*i,y*j

    return y/GCD(x,y)


#print p33()


def p34():
    fact = [reduce(lambda x,y:x*y,[j for j in range(1,i+1)],1) for i in range(10)]
    ss = sum(fact)
    res = 0
    for x in range(145,ss/10):
        v = 0
        for c in [ord(c)-ord('0') for c in str(x)]:
            v+=fact[c]
        if v == x:
            res += x
    return res
#print p34()

def p35():
    N = 1000000
    l = PrimeSieve(N)
    cc = 0
    for x in l:
        s = str(x)
        le = len(s)-1
        if le < 1:
            cc+=1
            continue
        s+=s
        f = True
        for i in range(le):
            if IsPrime(int(s[i+1:i+2+le])) is False:
                f = False
                break
        if f:
            cc+=1
    return cc

#print p35()

def p36():
    def BinPTest(n):
        s=''
        while n>0:
            if (n&1) == 0:
                s+='0'
            else:
                s+='1'
            n>>=1
        return (s[::-1] == s)
    print BinPTest(585),BinPTest(6)
    res = 0
    for x in xrange(1,1000000,2):
        s = str(x)
        if s == s[::-1] and BinPTest(x):
            res += x
    return res

#print p36()

def p37():
    def Check(n):
        s = str(n)
        for i in range(1,len(s)):
            if IsPrime(int(s[i:])) is False or IsPrime(int(s[:-i])) is False:
                return False
        return True
    cc = 0
    res = 0
    l = PrimeSieve(1000000)
    for x in l:
        if x > 10 and Check(x):
            cc+=1
            res+=x
            if cc == 11:
                break
    return res

#print p37()

def p38():
    res = 0
    for i in xrange(9999,0,-1):
        s = ''
        for j in range(1,10):
            s+=str(i*j)
            if len(s) > 9:break
            if len(s) == 9 and '0' not in s and len(set(s)) == 9:
                res = max(res, int(s))
    return res
#print p38()

def p39():
    def sol(s):
        cc = set()
        s2 = s/2
        mlimit = int(math.ceil(math.sqrt(s2)))
        for m in range(2,mlimit):
            if s2%m == 0:
                sm = s2/m
                while (sm&1) ==0:
                    sm>>=1
                if (m&1)==1:
                    k = m+2
                else:
                    k = m+1
                while k < (m<<1) and k <= sm:
                    if (sm%k)==0 and GCD(k,m)==1:
                        d = s2/(k*m)
                        n = k-m
                        a = d*(m*m-n*n)
                        b = 2*d*m*n
                        c = d*(m*m+n*n)
                        if a>b:a,b=b,a
                        if abs(a-b) < c and abs(a-c)<b and abs(b-c) < a and a+b>c and a+c >b and b+c>a:
                            cc.add((a,b,c))
                    k+=2
        return len(cc)

    l = [sol(i) for i in range(1001)]
    return l.index(max(l))

#print p39()


def p40():
    l = [0] + [i*(10**i-10**(i-1)) for i in range(1,10)]
    def DD(n):
        if n < 10: return n
        d = 0
        for i in range(10):
            if n > l[i]:
                n-=l[i]
            else:
                d = i
                break
        i = n/d
        if n%d == 0:i-=1
        return int(str(10**(d-1)+i)[n%d-1])
    return reduce(lambda x,y:x*y,[DD(10**i) for i in range(7)])
    s = '0123456789101112131415161718192021'
    for i in range(len(s)):
        print DD(i),s[i],i


#print p40()

def p41():
    # no 8/9 -digit
    l = '987654321'
    for i in range(7,0,-1):
        for j in Permutations(l[9-i:]):
            s = reduce(lambda x,y:x+y,j,'')
            if IsPrime(int(s)):
                return s
#print p41()

def p42():
    res = 0
    for w in [w.strip('"') for w in open('words.txt','r').readlines()[0].split(',')]:
        ct = 0
        for c in w:
            ct+=ord(c)-ord('A')+1
        ct<<=1
        q = int(math.floor(math.sqrt(ct)))
        if q*(q+1) == ct:
            res+=1
    return res

#print p42()

def p43():
    def R(t,s,l,lf,pl,resl):
        for i,v in enumerate(l):
            if lf[i]:
                ss=s*10+v
                st = ss%1000
                if t > 2 and (st%pl[t-3]) != 0:
                    continue
                if t == 9:
                    resl.append(ss)
                    continue
                lf[i] = False
                R(t+1,ss,l,lf,pl,resl)
                lf[i] = True

    l = [i for i in range(10)]
    lf = [True]*10
    pl = (2,3,5,7,11,13,17)
    resl = []
    for i in range(1,10):
        lf[i] = False
        R(1,i,l,lf,pl,resl)
        lf[i] = True
    return sum(resl)

#print p43()

def p44():
    def Check(n):
        fl = int(math.floor(math.sqrt(n*6)))
        return  (fl%3 == 2) and (fl*(fl+1) == 6*n)
    i,j = 1,2
    while True:
        i = 1
        while i < j:
            u,v = (i*((i<<1)+i-1)>>1),(j*((j<<1)+j-1)>>1)
            if Check(u+v) and Check(v-u):
                return v-u
            i+=1
        j+=1

#print p44()

def p45():
    i = 166
    while True:
        t = i*(3*i-1)
        fl = int(math.floor(math.sqrt(t)))
        if (fl&1) == 1 and fl*(fl+1) == t:
            #print fl,i,(fl+1)/2
            return ((fl*(fl+1))>>1)
        i+=1

#print p45()

def p46():
    ls = set(PrimeSieve(10000))
    x = 9
    while True:
        while x in ls:
            x+=2
        fl = int(math.floor(math.sqrt(x/2)))+1
        f = True
        for i in range(1,fl):
            if (x-2*i*i) in ls:
                f = False
                break
        if f:return x
        x+=2 

#print p46()

def p47():
    N = 200000#evil
    l = [0]*N
    size = 4
    for i in xrange(2,N):
        if i > 1004:
            f = True
            for o in range(4):
                if size != l[i-o]:
                    f = False
                    break
            if f:return i-size+1
        if l[i] == 0:
            j = i+i
            while j<N:
                l[j]+=1
                j+=i
#print p47()


def p48():
    return str(sum(i**i for i in xrange(1,1001)))[-10:]
#print p48()

def p49():
    def Check(a,b):
        return (set(str(a)) == set(str(b)))
    l = [i for i in range(1487+1,9999) if IsPrime(i)]
    for i,v in enumerate(l):
        for j in range(i+1,len(l)):
            if Check(v,l[j]):
                c = l[j]*2-v
                if c in l and Check(c,v):
                    return str(v)+str(l[j])+str(c)

#print p49()

def p50():
    N = 1000000
    l = PrimeSieve(N)
    le = len(l)
    ls = set(l)
    max_v = 1
    res = 0
    for i in xrange(le):
        j = i+1
        ln = 1
        cc = l[i]
        while j < le:
            cc+=l[j]
            ln += 1
            if cc >= N:break
            if cc in ls:
                if max_v < ln:
                    max_v = ln
                    res = cc
            j+=1
    return res

#print p50()

def p51():
    l = PrimeSieve(1000000)
    ls,le = set(l),len(l)
    def GBP(n):
        ll,p = [],0
        while n>0:
            if (n&1)==1:ll.append(p)
            n >>= 1
            p+=1
        return ll
    def Check(n):
        sli = list(str(n))
        sl = len(sli)
        for i in xrange(3,(1<<sl)):
            pl = GBP(i)
            b,cc = 1 if (sl-1) in l else 0,0
            for j in range(b,10):
                slit = sli[:]
                for index in pl:
                    slit[sl-1-index] = str(j)
                st = reduce(lambda x,y:x+y,slit,'')
                if int(st) in ls:
                    cc+=1
                if cc + 10-j < 8:break
            if cc == 8:
                return True
        return False

    for i in xrange(l.index(120383)+1,le):
        if Check(l[i]):
            return l[i]
    return -1
    i = l[-1] + 2
    while True:
        if IsPrime(i) and Chedk(i):
            return n
        i+=2
#print p51()

def p52():
    def Check(n):
        s = set(str(n))
        for i in range(2,7):
            if s != set(str(n*i)):
                return False
        return True

    x = 125875
    while True:
        if Check(x):
            return x
        x+=1
#print p52()

def p53():
    res = 0
    N = 1000000
    fact = {0:1}
    fx = 1
    for n in range(1,101):
        fx*=n
        fact[n] = fx
        for r in range(1,n+1):
            t = fx/(fact[r]*fact[n-r])
            if t > N:
                res+=1
    return res

#print p53()

#376
def p54():
    def RF(ll,ls):
        return (len(set(ls)) == 1 and len(set(ll)) == 5 and ll[0] == 10 and ll[-1] == 14)
    def SF(ll,ls):
        return (len(set(ls)) == 1 and len(set(ll)) == 5 and ll[-1] - ll[0] == 4)
    def FK(ll,ls):
        return (len(set(ll)) == 2 and (ll.count(ll[0]) > 3 or ll.count(ll[-1]) > 3))
    def FH(ll,ls):
        return (len(set(ll)) == 2 and ll.count(ll[0]) * ll.count(ll[-1]) == 6)
    def F(ll,ls):
        return (len(set(ls)) == 1)
    def S(ll,ls):
        return (len(set(ll)) == 5 and ll[-1] - ll[0] == 4)
    def TK(ll,ls):
        return (len(set(ll)) == 3 and len([i for i in ll if ll.count(i) == 3]) > 0)
    def TP(ll,ls):
        return (len(set(ll)) == 3 and len(set([i for i in ll if ll.count(i) == 2])) == 2)
    def OP(ll,ls):
        return (len(set(ll)) == 4)
    mp={'T':10,'J':11,'Q':12,'K':13,'A':14}
    for i in range(1,11):
        mp[str(i)] = i
    def ParseCard(l):
        ll = [mp[c[0]] for c in l]
        ls = [c[1] for c in l]
        ll.sort()
        if RF(ll,ls):return [(9,-1)]
        elif SF(ll,ls):return [(8,ll[-1])]
        elif FK(ll,ls):return [(7,ll[0] if ll.count(ll[0]) == 4 else ll[-1])]
        elif FH(ll,ls):return [(6,ll[0] if ll.count(ll[0]) == 3 else ll[-1])]
        elif F(ll,ls): return [(5,ll[-i]) for i in range(0,5)]
        elif S(ll,ls): return [(4,ll[-1])]
        elif TK(ll,ls):return [(3,[i for i in ll if ll.count(i) == 3][0])]
        rank = 0
        if TP(ll,ls):
            rank = 2
        elif OP(ll,ls):
            rank = 1
        l = [(rank,i) for i in set(ll) if ll.count(i) == 2]
        for i in ll:
            if ll.count(i) == 1:
                l.append((0,i))
        l.sort(reverse=True)
        return l
    res = 0
    for l in open('poker.txt','r').readlines():
        s1 = l[:15]
        s2 = l[-16:]
        l1 = s1.split()
        r1 = ParseCard(l1)
        if 'A' in s1:
            r12 = ParseCard(s1.replace('A','1').split())
            if r12 > r1: r1 = r12
        l2 = s2.split()
        r2 = ParseCard(l2)
        if 'A' in s2:
            r22 = ParseCard(s2.replace('A','1').split())
            if r22 > r2: r2 = r22
        if r1 > r2:
            res += 1
    return res
#print p54()

def p55():
    def Check(n):
        r = n
        sr = str(r)[::-1]
        for i in range(50):
            r += int(sr) 
            s = str(r)
            sr = s[::-1]
            if s == sr:return False
        return True
    res = 0
    for x in range(1,10000):
        if Check(x):res+=1
    return res

#print p55()

def p56():
    res = 0
    for a in range(1,100):
        for b in range(1,100):
            r = sum(int(c) for c in str(a**b))
            res = r if r > res else res
    return res
#print p56()

def p57():
    res,a,b = 0,1,2
    for i in range(1000):
        a,b = b,a + (b<<1)
        res += 1 if len(str(a+b)) > len(str(b)) else 0
    return res
#print p57()

def p58():
    a,sl,pc,dpc = 1,1,0,1
    while True:
        sl,dpc = sl+2,dpc+4
        for i in range(4):
            a+=sl-1
            if IsPrime(a):pc+=1
        if pc*10 < dpc:break
    return sl
#print p58()

def p59():
    strl = " !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    l = [int(c) for c in open('cipher1.txt','r').readlines()[0].strip('\r\n').split(',')]
    for a in range(97,123):
        for b in range(97,123):
            for c in range(97,123):
                s,k = '',(a,b,c)
                for i,v in enumerate(l):
                    ch=chr(v^k[i%3])
                    if ch not in strl:break
                    s+=ch
                if len(s) == len(l): 
                    return sum(ord(c) for c in s)
                
#print p59()

def p60():
    d,l = {},PrimeSieve(10000)
    for p in l:d[p] = set()
    for i,v in enumerate(l):
        for j in xrange(0,i):
            if IsPrime(int("%s%s"%(l[j],v))) and IsPrime(int("%s%s"%(v,l[j]))):
                d[l[j]].add(v)
                d[v].add(l[j])
    resl = []
    def R(kk,vv,resl):
        if len(kk) == 5:
            resl.append(kk)
            return
        for v in vv:
            if all(v > it for it in kk) and kk.issubset(d[v]):
                k = kk|set([v])
                R(k,vv&d[v],resl)
    for k,v in d.iteritems():
        R(set([k]),v,resl)
    return min(sum(rl) for rl in resl)
#print p60()

def p61():
    funcl =[lambda n:n*(n+1)//2,
            lambda n:n*n,
            lambda n:n*(3*n-1)//2,
            lambda n:n*(2*n-1),
            lambda n:n*(5*n-3)//2,
            lambda n:n*(3*n-2),]

    lr = []
    for j in range(len(funcl)):
        i,k = 1,1
        while funcl[j](k) < 1000:
            k+=1
        while funcl[j](i) < 10000:
            i+=1
        lr.append((k,i))
    pn = [[funcl[i](j) for j in xrange(lr[i][0],lr[i][1])] for i in range(6)]

    def R(t,l,pni):
        if t == 6:
            if (l[-1] % 100) == (l[0]/100):
                yield l
        if t == 0:
            for v in pn[0]:
                for r in R(1,[v],set([0])):
                    yield r
        else:
            for i in xrange(6):
                if i not in pni:
                    for j in pn[i]:
                        if j/100 == l[-1]%100:
                            for r in R(t+1,l[:]+[j],set([i])|pni):
                                yield r

    return sum([r for r in R(0,[],set())][0])
#print p61()

def p62():
    x,d = 2,{}
    while True:
        y = ''.join(sorted(str(x*x*x)))
        c = d.get(y,[])
        c.append(x)
        if len(c) >= 5:
            return min(c)**3
        d[y] = c
        x+=1

#print p62()

def p63():
    res = 0
    for i in range(1,10):
        for j in range(1,100):
            k = len(str(i**j))
            if j == k:
                res +=1
            elif k > j:break
    return res
#print p63()

def p64():
    def CountOfContinuedFractions(n):
        x = int(math.floor(math.sqrt(n)))
        l,a,b,res = [x],1,x,1
        while b*b < n:
            r = (x+b)*a/(n-b*b)
            a = (n-b*b)/a 
            b = r*a-b
            res += 1
            #l.append(r)
            if a == 1 and b == x:
                break
        return res - 1 #,l 
    res = 0
    for i in xrange(2,10001):
        if (CountOfContinuedFractions(i)&1) == 1:
            res += 1
    return res
#print p64()

def p65():
    l = [2] + reduce(lambda x,y:x+y,[[1,i+i,1] for i in range(1,34)],[])
    N = 99
    a,b = 1,l[N]
    for i in range(N-1,0,-1):
        a,b = b,l[i]*b+a
    return sum(int(c) for c in str(b*2+a))

#print p65()

"""
more detail in
http://www.ams.org/notices/200202/fea-lenstra.pdf
http://mathworld.wolfram.com/PellEquation.html
"""
def p66():
    def ContinuedFractions(n,term = -1):
        x = int(math.floor(math.sqrt(n)))
        l,a,b,term = [x],1,x,term+term
        while b*b < n:
            r = (x+b)*a/(n-b*b)
            a = (n-b*b)/a 
            b = r*a-b
            l.append(r)
            if term > 0:
                if r == term:
                    l.pop()
                    break
            elif b == x:
                break
        return l 
    def Cal(d,l):
        a,b = 1,l[-1]
        for i in range(len(l)-2,-1,-1):
            a,b = b,l[i]*b+a
        return a,b,b*b-d*a*a
    res,rd = 2,2
    for i in range(2,1001):
        l = ContinuedFractions(i)
        a,b,t = Cal(i,l)
        if t == 0:continue
        elif t == 1:pass
        elif t != -1:
            l = ContinuedFractions(i,l[0])
            a,b,t = Cal(i,l)
        if t == -1:
            b,a = b*b+a*a*i,2*b*a
        if b > res:
            res,rd = b,i
    return rd

#print p66()

def p67():
    return p18()

def p68():
    l1,l2 = [1,2,3,4,5],[6,7,8,9,10]
    res,rs = 6,''
    for i in Permutations(l2):
        for j in Permutations(l1):
            if len(set([i[k] + j[k] + j[(k+1)%5] for k in range(5)])) == 1:
                t = ''.join([str(i[k])+str(j[k])+str(j[(k+1)%5]) for k in range(5)])
                if len(rs) == 0:
                    res,rs = i[0],t
                elif i[0] == res:
                    if t > rs:rs = t
                elif i[0] < res:
                    res,rs = i[0],t
    return rs
#print p68()

def p69():
    N = 1000000
    l,d = PrimeSieve(N+1),{}
    for p in l:d[p] = p-1
    def Cal(n):
        if n in d:return d[n]
        for p in l:
            if n%p == 0:
                nt = n/p
                d[n] = Cal(nt)*(p if nt%p == 0 else p-1)
                return d[n]
    rt,res = 0,2
    for i in xrange(2,N+1):
        t = i*1.0/Cal(i)
        if rt < t:
            rt,res = t,i
    return res

def p69_2():
    l = PrimeSieve(100)
    res = 1
    for p in l:
        res *= p
        if res >= 1000000:
            return res/p

#print p69()

def p70():
    N = 10000000
    l,d = PrimeSieve(N+1),{}
    for p in l:d[p] = p-1
    def Cal(n):
        if n in d:return d[n]
        for p in l:
            if n%p == 0:
                nt = n/p
                d[n] = Cal(nt)*(p if nt%p == 0 else p-1)
                return d[n]
    rt,res = N,2
    for i in xrange(1000000,N):
        t = Cal(i)
        if sorted(str(t)) == sorted(str(i)):
            #print i,t
            t = i*1.0/t
            if rt > t:
                rt,res = t,i
    return res
#print p70()












def main(arg):
    if len(arg) > 1:
        pass


if __name__ == '__main__':main(sys.argv)



