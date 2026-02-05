# it is me again! with another mind blowing project.
# hopefully it is supposed to differentiate polynomials and equations
# other types of functions will be dealt with in the near future


def differentiate():
    print('If you are differentiating a polynomial equation, enter 1.')
    #print('If you are differentiating a equation with non-integer indices, enter 2.')
    #print('If you are differentiating a trig equation, enter 3.') COMING SOON....
    option=int(input(''))
    if option == 1:
        order=int(input('Enter the order of the polynomial.'))
        power=order
        xpowers_list=[]
        while power>=0:
         if power>1:
             term= f'x^{power}'
         elif power==1:
             term='x'
         elif power==0:
             term=''
         xpowers_list.append(term)
         power-=1
        print(xpowers_list)
        a,b,c,d,e,f,g,h,i,j='a','b','c','d','e','f','g','h','i','j'
        variables_list=[a, b, c, d, e, f, g, h, i, j]#you can add more variables. the highest degree it can currently handle is 9.
        variables= variables_list[:order+1]
        print(variables)
        realterms=[]
        for no in range(order+1):
            term= variables[no]+xpowers_list[no]
            realterms.append(term)
        for a in realterms:
            if a!= realterms[-1]:
                i = realterms.index(a)
                a+=' + '
                realterms[i]=a
        exp='y = ' 
        for x in realterms:
            exp+=x
        print(f'Your equation is in the format {exp}.')
        realterms=[]
        for x in variables:
            i = variables.index(x)
            print(f'Enter the value of {x}')
            x = int(input(''))
            variables[i]= x
        for no in range(order+1):
            if variables[no] != 1:
                term= str(variables[no])+xpowers_list[no]
            elif no!= order and variables[no] == 1:
                term= xpowers_list[no]
            elif no==order and variables[no]==1:
                term='1'
            realterms.append(term)
        for a in realterms:
            if a[0]=='0':
                realterms.remove(a)
        for a in realterms:
            if a!= realterms[-1]:
                i = realterms.index(a)
                a+=' + '
                realterms[i]=a            
        exp='y = ' 
        for x in realterms:
            exp+=x
        x= exp.count('+ -')
        for a in range(x):
            exp=exp.replace('+ -', '- ')        #I have to cover for the occurrence of negative numbers. 
        print(f'Your equation is {exp}.')  # To make the final equation look nice.
        var=order
        for x in variables:
            i = variables.index(x)
            x*=var
            variables[i]=x
            var-=1
        del variables[-1]
        del xpowers_list[0]
        realterms=[]
        for no in range(order):
            if variables[no] != 1:
                term= str(variables[no])+xpowers_list[no]
            else:
                term= xpowers_list[no]
            realterms.append(term)
        for a in realterms:
            if a[0]=='0':
                realterms.remove(a)
        for a in realterms:
            if a!= realterms[-1]:
                i = realterms.index(a)
                a+=' + '
                realterms[i]=a
        exp='dy/dx = '
        for x in realterms:
            exp+=x
        x= exp.count('+ -')
        for a in range(x):
            exp=exp.replace('+ -', '- ')
        print(f'The derivative of your equation is {exp}.')        
differentiate()       # done and dusted. was incredibly hard but fun.
