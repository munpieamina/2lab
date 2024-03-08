import random
c1=int(input('Выберите цвет(1-красный, 2-синий, 3-жёлтый):'))
clrs=[1, 2, 3]
if c1 in clrs:
    c2=random.choice(clrs)
    while c2==c1:
        c2 = random.choice(clrs)
    if (c1==1 and c2==2) or (c1==2 and c2==1):
        print('красный + синий = фиолетовый')
    elif (c1==1 and c2==3) or (c1==3 and c2==1):
        print('красный + жёлтый = оранжевый')
    elif (c1==2 and c2==3) or (c1==3 and c2==2):
        print('синий + жёлтый = зелёный')
else:
    print('ОШИБКА ВВОДА')