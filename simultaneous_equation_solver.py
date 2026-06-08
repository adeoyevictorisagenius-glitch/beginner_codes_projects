import numpy as np

print('This is a python program for solving simultaneous equations!')
print("I used Cramer's rule implemented in python")
print('Simultaneous equations are the the form :')
print('ax + by = c\ndx + ey = f')

var = ['a', 'b', 'c', 'd', 'e', 'f']
while True:
    var_values=[]
    for s in var:
        try :
            var_values.append(int(input(f'Enter the value for {s} : ')))
        except ValueError:
            print('Invalid input!')
    a,b,c,d,e,f = var_values

    print(f'The simultaneous equations are :')
    print(f'{a}x + {b}y= {c}\n{d}x + {e}y = {f}')
    ans = input('Is this correct? y/n : ').lower()
    if ans == 'y':
        det_matrix= np.array([[a,b], [d,e]])
        x_matrix = np.array([[b,-c],[e,-f]])
        y_matrix= np.array([[a,-c], [d,-f]])

        det = float(np.linalg.det(det_matrix))
        det_x = float(np.linalg.det(x_matrix))
        det_y = float(-np.linalg.det(y_matrix))
        if det ==0 :
            print("This equation can't be computed!")
            continue
        x = det_x/ det

        y = det_y/det
        for s in [x,y]:
            if s == "nan":
                print(f'{s} cannot be computed')
        print(f'x and y are {x} and {y}')
    else: 
        continue


        
