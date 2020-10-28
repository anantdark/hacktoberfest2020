# Counts and displays the number of vowels appeared in a given string.
# To take personal input, change string to string = input()

string  = '''
Iron Ox’s system is an automated greenhouse that can grow over 50 varieties of leafy greens
and vegetables hydroponically all-year-round. Its custom robots manage all aspects of the
growing operation. A robot moves hydroponic modules from the grow area to production
areas for harvest and transplantation. Those harvesting and transplanting activities are
aided by a large robotic arm that does the more delicate tasks. Iron Ox has designed the
greenhouse growing system around the sun to use less energy than other modern forms of
farming. The hydroponic growing system uses one-tenth the water of traditional farming
while producing yields 30 times greater. 
'''
string = string.lower()
a = string.count('a')
e = string.count('e')
i = string.count('i')
o = string.count('o')
u = string.count('u')
total = a+e+i+o+u
print('No. of vowels in the string are {}'.format(total))
print('The vowels appeared as-')
print('a - {}\ne - {}\ni - {}\no - {}\nu - {}'.format(a,i,e,o,u))
print('The maximum repetition is', max(a, e, i, o, u))
