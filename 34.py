fac_dict = {0:1}

def factorial(num):
    res = 1
    
    for i in range(1, num+1):
        res *= i

    return res

for i in range(1, 10):
    fac_dict[i] = factorial(i)

def main():
    num_list = []
    
    for i in range(3, 2540160):
        sum = 0
        
        for num in str(i):
            num = int(num)
                        
            sum += fac_dict[num]

        if sum == i:
            print(sum)
            num_list.append(i)
    sum = 0
    for i in num_list:
        sum += i
        
    print(sum)
    
    
main()


