import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor




def makeTriangle(s):
    #print("S is %d" % s)
    triangle = 0
    for a in range(1,s):
        #print("a is: %d " % a)
        triangle = triangle + a
        #print("Triangle: %d " % triangle)
    return triangle



def checkTriangle():
    count = 1
    n = 3
    x = False
    while x!=True:
        x = makeTriangle(n)
        divisorList = list(divisorGenerator(x))
        if len(divisorList)>500:
            print ("The largest is %d " % x)
            break
        n+=1
    return x


checkTriangle()

