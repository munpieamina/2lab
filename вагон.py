n=int(input('Введите номер места(от 1 до 54): '))
if n in range(1,55):
    if n%2==0:
        s='верхнее '
    else:
        s='нижнее '
    if n in range(37, 55):
        s=s+'боковое'
    else:
        s=s+'плацкарт'
    print('Ваше место - ', s)
else:
    print('такого места нет')