import random

def randomjj():
    a = [random.randint(0, 9) for iter in range(12)]
    b = 13
    sum = 0
    chk = 0

    for x in range(12):
        num = a[x]*b
        sum = sum + num
        b-=1

    sum = sum%11
    chk = 11-sum
    chk = chk%10
    result = (str(a[0])+str(a[1])+str(a[2])+str(a[3])+str(a[4])+str(a[5])+str(a[6])+str(a[7])+str(a[8])+str(a[9])+str(a[10])+str(a[11])+str(chk))

    
    return result
