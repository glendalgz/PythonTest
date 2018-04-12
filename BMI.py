#python3.6
#learning from Liaoxuefeng

a = input("pls input your height:")
b = input("pls input your weight:")

height = float(a)
weight = float(b)

bmi = weight/(height*height)
print('Your BMI is：%.1f'%bmi)

if bmi < 18.5:
    print('a little thin')
elif 18.5 < bmi < 28:
    print('normal')
elif 28 < bmi <32:
    print('a little weight')
else:
    print('FAT')