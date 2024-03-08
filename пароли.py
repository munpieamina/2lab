p1=input('Введите пароль:')
a=any(c.isupper() for c in p1)
b=any(c.isdigit() for c in p1)
c=any(c.islower() for c in p1)
if len(p1)<8:
    print('пароль должен содержать минимум 8 символов')
elif a==False:
    print('пароль должен содержать хотя бы одну большую букву')
elif b==False:
    print('пароль должен содержать хотя бы одну цифру')
elif c==False:
    print('пароль должен содержать хотя бы одну маленькую букву')
else:
    p2=input('Подтвердите пароль:')
    if p1==p2:
        print('Пароль принят!')
    else:
        print('Пароль не принят((')