import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    ans=''
    for i in range(0,100):
        ans+=str(random.choice([0,1]))
    numberOfStreaks+=ans.count('111111')
    numberOfStreaks+=ans.count('000000')

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
