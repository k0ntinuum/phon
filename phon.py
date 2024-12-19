
import random
N = 5
K = 2**N
l = N
loud = True

k = random.choices([0,1], k = K )
x = random.choices([0,1], k = l)

def randbits(n):
    return random.choices([0,1], k = n)

def val(x,j):
    y = 0
    L = len(x)
    for i in range(0,N):
        y += x[(i + j) % L]*2**i
    return y

    
def advance(x,k):
    y = []
    L = len(x)
    for i in range(0,L):
        y += [k[val(x,i)]]
    return y



def apply(x,k):
    y = x
    for i in range(0,2):
        y = advance(y,k)
    return y



def encode_bit(b, k, L):
    m = -1
    while m != b:
        x = randbits(L)
        y = apply(x,k)
        m = y[0]
    return x



def encode(B, k):
    y = []
    l = N
    for i in range(len(B)):
        #print("len = ",l)
        e = encode_bit(B[i], k, l)
        d = apply(e,k)
        if loud == True:
            print("obscured bit         = ", B[i])
            print("ciphertext word      = ",  end = "")
            printv(e)
            
            print("test CA decode         ",  end = "")
            t = advance(e,k)
            printv(t)
            print("                       ",  end = "")
            t = advance(t,k)
            printv(t)
            #print("decoded word         = ",  end = "")
            #printv(d)
            print("found bit            = ",  d[0])
            print("found next len       = ", sum(d)%N + N )
            print()
        l = sum(d)%N + N
        y += e
    return y
        
        
def printv(v):
    for i in range(len(v)):
        if v[i] == 0:
            print("O", end ="")
        elif v[i] == 1:
            print("|", end="")
    print()
    

def decode(x,k):
    left = x
    y = []
    l = N
    while len(left) > 0:
        #printv(left)
        #print("len = ",l)
        word = left[:l]   
        left = left[l:]
        processed_word = apply(word, k)
        if loud == True:
            print("found word           = ",  end = "")
            printv(word)
            print("decode word            ",  end = "")
            t = advance(word,k)
            printv(t)
            print("                       ",  end = "")
            t = advance(t,k)
            printv(t)
            #print("decoded word         = ",  end = "")
            #printv(processed_word)
            print("found bit            = ",  processed_word[0])
            print("found next len       = ", sum(processed_word)%N + N )
            print()
        y += [processed_word[0]]
        
        l = sum(processed_word)%N + N
    return y


def demo():
    print(chr(27) + "[2J")
    print("key = ", end = "")
    printv(k)
    p = randbits(5)
    print("plain text : ", end ="")
    printv(p)
    print()
    y = encode(p, k)
    print("cipher text : ", end ="")
    printv(y)
    print()

    z = decode(y,k)
    print("SUMMARY")
    print("key = ", end = "")
    printv(k)
    print("plain   = ", end = "")
    printv(p)
    print("cipher  = ", end = "")
    printv(y)
    print("decoded = ", end = "")
    printv(z)
    print("success = ", z == p)

demo()




