def is_prime(a):
    dem=0
    for i in range(2,a):
        if a%i==0:
            dem+=1
    return dem==0
is_prime(s)
