# my maths teacher asked me to do this
# write a program that can calculate the spearman rank correlation coefficients between two sets of numbers


def spearman_coefficient_calculator():
    print('Enter the number of values in both sets of numbers.')
    num= int(input(''))
    set1=[]
    set2=[]
    for no in range(num):
        value=float(input('Enter the values for the first set of numbers. '))
        print('')
        set1.append(value)
    for no in range(num):
        value=float(input('Enter the values for the second set of numbers. '))
        print('')
        set2.append(value)
    repeated_values1 ={}
    repeated_values2 ={}    
    for no in set1:
        count= set1.count(no)
        if count>1:
            repeated_values1[no]=count
    for no in set2:
        count= set2.count(no)
        if count>1:
            repeated_values2[no]=count
    no1=1
    rank_dict1f={}
    set1c=[]
    no_dev1=[]
    for a in repeated_values1.values():
        a-=1
        no_dev1.append(a)
    sum1=sum(no_dev1) 
    for a in set1:
        set1c.append(a)
    print(set1c)
    for no in range(num-sum1):
        minimum= min(set1c)
        rank_dict1f[minimum]=no1
        if set1.count(minimum)>1:
            for a in range(repeated_values1[minimum]):
                set1c.remove(minimum)
                no1+=a
        else:
            set1c.remove(minimum)
        no1+=1
    no1=1
    for a in set1:
        set1c.append(a)        
    rank_dict1={}
    for no in range(num-sum1):
        minimum= min(set1c)
        if minimum in repeated_values1.keys():
            rank_s = rank_dict1f[minimum]
            for b in range(repeated_values1[minimum]-1):               
                rank_s+=(rank_s +1)
            rank_s/=repeated_values1[minimum]
            rank_dict1[minimum]=rank_s
            for a in range(repeated_values1[minimum]):
                set1c.remove(minimum)            
        else:
            rank_dict1[minimum]=no1
            set1c.remove(minimum)

        no1+=set1.count(minimum)
    no2=1
    rank_dict2f={}
    set2c=[]
    no_dev2=[]
    for a in repeated_values2.values():
        a-=1
        no_dev2.append(a)
    sum2=sum(no_dev2)    
    for a in set2:
        set2c.append(a)
    for no in range(num-sum2):
        minimum= min(set2c)
        rank_dict2f[minimum]=no2
        if set2.count(minimum)>1:
            for a in range(repeated_values2[minimum]):
                set2c.remove(minimum)
                no2+=a
        else:
            set2c.remove(minimum)
        no2+=1
    no2=1
    rank_dict2={}
    for a in set2:
        set2c.append(a)    
    for no in range(num-sum2):
        minimum= min(set2c)
        if minimum in repeated_values2.keys():
            rank_s = rank_dict2f[minimum]
            for b in range(repeated_values2[minimum]-1):               
                rank_s+=(rank_s +1)
            rank_s/=repeated_values2[minimum]
            rank_dict2[minimum]=rank_s
            for a in range(repeated_values2[minimum]):
                set2c.remove(minimum)               
        else:
            rank_dict2[minimum]=no2
            set2c.remove(minimum)
        no2+=set2.count(minimum)
    deviations=[]
    for no in range(num):
        r1 = rank_dict1[set1[no]]
        r2 = rank_dict2[set2[no]]
        d=r1-r2
        d= d**2
        deviations.append(d)
    summation=sum(deviations)
    coefficient= 1- 6*summation/(num**3 -num)
    print(f'The Spearman rank correlation coefficient of {set1} and {set2} is {coefficient}.')
    print(rank_dict1)
    print(rank_dict2)
            
spearman_coefficient_calculator()
# i cant belive i did this. one of the hardest thing i have ever done.
