x=input('Enter your username\n')
c=input('Enter your password\n')
if x=='liro55' and c=='12345678':
    print('Username is correct\nPassword is correct')
elif x !='liro55' and c !='12345678':
    print('Username is wrong\nPassword is wrong')
elif x=='liro55' and c != '12345678':
    print('Password is wrong')
elif x !='liro55' and c=='12345678':
    print('Username is wrong')