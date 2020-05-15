'''كتبي لعبة تطبع اسم اللعبة أولاً
Numbers from 1 to 10
ثم تطلب من المستخدم أن يحزر الرقم
"Guess the number: "
إذا المستخدم لم يدخل الرقم الصحيح ستبقى اللعبة تسأله للأبد، إذا قام بإدخال الرقم الصحيح، يظهر للمستخدم:
"Great! You did it!" '''


print('Numbers from 1 to 10')
num=int(input('Guess the number:'))
my_num = 7
good="Great! You did it!"
while 1==1 :
    if my_num != num :
        print(input('Guess the number:'))
    
    
        
    else:
        print(good)
         