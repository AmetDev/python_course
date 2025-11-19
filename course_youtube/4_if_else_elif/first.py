if True:
    print('hello world')

if False:
    print('hi')

x = 0
if x > 0:
    print('x positive_0')

#проверить несколько условий
if x > 0:
    print('x positive')
elif x < 0:
    print('x is negative')
else:
    print('x is zero')

#если оба условия верны выполнится тот кто выше
x2 = 3
if x2 > 0:
    print('is positive')
elif x2 > 2:
    print('is positive')

#вложеный if elif
if x2 > 0:
    print("x2 positive > 0")
    if (x2 > 1):
        print('x2 positive > 1')
# но не совсем хорошая практика

if x2 > 0 and x2 > 1:
    print('best practis')

message = ""
if message:
    print('message is not empty')
else:
    print('message is empty')

