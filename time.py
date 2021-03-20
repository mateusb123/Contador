### contador ###
from time import sleep
import os

n = 0
i = 0

### declarando funções ###
value=int(input('value-max: '))
d = input('(desc),(crec): ')

## formatando o numero ##
n=value

### reniciando o valor do numero decrecente ###
if d == 'desc':
    n = value+1

while i < n:
    ### forma decrecente ###
    if d == 'desc':
        if n == 1:
            break
        else:
            n-=1
            os.system('cls')
            print(n)
            sleep(1)
    ### forma crecente ###
    else:
        i+=1
        os.system('cls')
        print(i)
        sleep(1)

### LIMPAR CONSOLE ###
os.system('cls')