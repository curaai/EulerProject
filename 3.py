import math

def prime_check(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        elif math.sqrt(n) < i:
            return True
        
if __name__ == '__main__':

    num = 600851475143

    big =0
    for i in range(1000, num):
        if num % i == 0 and prime_check(i):
            if big < i:
                big = i

        elif math.sqrt(num) < i:
            break

    print(big)

