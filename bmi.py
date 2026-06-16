#BMIcalculator
w = float(input("ป้อนน้ำหนัก")) #ป้อนน้ำหนัก
h = float(input("ป้อนส่วนสูง")) #ป้อนส่วนสูง
bmi = w / h*h #คำนวณbmi
print("BMI =", round(bmi, 2)) #แสดงผลตามเงื่อนไขดังข้างล่าง
if bmi < 18.5:
    print("น้ำหนักต่ำกว่าเกณฑ์")
elif bmi < 23:
    print("น้ำหนักปกติ")
elif bmi < 25:
    print("น้ำหนักเกิน")
elif bmi < 30:
    print("โรคอ้วนระดับ 1")
else:
    print("โรคอ้วนระดับ 2")

