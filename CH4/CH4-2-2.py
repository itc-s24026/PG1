def perrin(m=100):
    '''列出比m还要小的数列'''
    a,b,c = 3,0,2
    rusult = []
    while a < m:
        result.append(a)
        a,b,c = b,c,a+b
    return result
