#Another method to print a pyramid in python

n = int(input('Enter the size of the triangle'))
for i in range(1, n+1):
    print((' '.join('#'*i)).center(2*n))
