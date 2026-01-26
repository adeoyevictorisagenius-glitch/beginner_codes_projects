
print('Hello there, it is vyral again with another small code i played with.')
print('')



def numberbase_checker(number, base):
    number= str(number)
    a=0
    for char in number:
        if int(char) >= base:
            a+=1
    if a!=0:
        print(f'Invalid input! A base {base} number cannot have a digit equal to or greater than {base}.')
        return False
    else :
        return True

def decimal_to_otherbase(number, base):
    changed_num=''
    otherbase=''
    while True:
        quotient= int(number/base)
        remainder= str(number%base)
        if quotient==0:
            changed_num+=remainder
            break
        else:            
            changed_num+=remainder
            number = quotient
    #print(changed_num)
    no=1
    length=len(changed_num)# i didn't know how to reverse strings at the time so i improvised. invented my own way of reversing the numbers
    for num in range(length):
        otherbase += changed_num[length-no]
        no+=1
    print(otherbase)



def otherbase_to_decimal(number,base):
    length = len(str(number))
    changed_num=''
    denary=0
    validity = numberbase_checker(number,base)
    if validity == True:
        number = str(number)
        p= 1
        denary=0
        for char in number:       
            power= length-p
            dec_digit= int(char)*(base**power)
            denary+=dec_digit
            p+=1       
    print(denary)



def numberbase_converter():
    print('To convert from decimal to another base, input 1.')
    print('To convert from another base to decimal, input 2.')

    option = int(input(''))
    number= int(input('Input your number. '))
    changed_num=''
    if option==1:
        base=int(input('Which base are you converting to? '))
        decimal_to_otherbase(number,base)
    elif option==2:     
        base=int(input('From which base do you wish to convert to denary? '))
        otherbase_to_decimal(number, base)
    



numberbase_converter()
