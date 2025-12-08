integers=[]
prime_num=[]
# i started from 2 because 1 is not prime
for num in range(2,1001):# you can adjust the value of the upper limit i.e. 1001 to maybe 10001. it just takes a bit longer.
    integers.append(num)

def prime_num_finder():
    print('This program will help you find the nth prime number of your choice')
    n=int(input('Enter the value of n: '))
    trials=0
    while len(prime_num)==0:     
        for num in integers:
            num_of_times_div=0
            for no in range(2,num):
                # result= num%no
                # if result ==0:
                #     num_of_times_div+=1
                if no!=num and no!=1:
                    result=num%no
                    if result ==0:
                        num_of_times_div+=1
                else:
                    continue        
            if num_of_times_div==0:
                prime_num.append(num) 
                # print(f'{num}, -> {trials}')       
                trials+=1    
                # print(trials) 
        trials+=1
        
    index=n-1
    num_required=prime_num[index]                
    print(f'The prime number you are looking for is {num_required}.')
    print(prime_num)
    print(len(prime_num))

prime_num_finder()                

