name=input("Enter student's name : ")
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]           

if name == 'Ahmad'  :
    print ('Ahmad',sum(s1[1:6]))
elif name == 'Sami'  :
    print ('Sami', sum(s2[1:6]))
elif name == 'Faris'  :
    print ('Faris',sum(s3[1:6]))
else :
    print('Student is not recorded 0')
        
    