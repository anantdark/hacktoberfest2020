#Program to print pyramid of size n

n = int(input('Enter the size of the triangle'))
for i in range(1, n+1):
    for j in range(n-i):
        print(end = ' ')
    for k in range(i):
        print('#', end = ' ')
    print('\n')
    
    
#CoDeD By AnAnT
