from random import choice, randint

letters =['a','b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m','n','o',
          'p','q','r','s','t','u','v','w','x','y','z']
numbers = [0,1,2,3,4,5,6,7,8,9]
characters=['!', '@', '#', '%','$', '+', '&', '.', '+', '?',  ]

symbols= [letters,numbers,characters]

while True: 
    print('Welcome again to one of my projects!')
    print('This one is to generate a password for you using the random library')
    ans = input('What is the length of your password? ')  
    password= ''
    try :
        length = int(ans)
        for x in range(length):
            a = randint(0,2)
            selected_list = symbols[a]
            symbol= choice(selected_list)
            password+=str(symbol)

    except ValueError:
        print('Invalid input!')
    print(f'And your password is : {password}')
    d=input('Do you wish to continue? y/n ').rstrip()
    if d != 'y':
        break
