import math

print("=== โปรแกรมคำนวณพื้นที่เรขาคณิต ===")
print("1. วงกลม")
print("2. สี่เหลี่ยมจัตุรัส")
print("3. สี่เหลี่ยมผืนผ้า")
print("4. สามเหลี่ยม")

choice = int(input("เลือกรูปที่ต้องการคำนวณ (1-4): "))

if choice == 1:
    radius = float(input("กรอกรัศมี: "))
    area = math.pi * radius ** 2
    print("พื้นที่วงกลม =", area)

elif choice == 2:
    side = float(input("กรอกความยาวด้าน: "))
    area = side ** 2
    print("พื้นที่สี่เหลี่ยมจัตุรัส =", area)

elif choice == 3:
    width = float(input("กรอกความกว้าง: "))
    length = float(input("กรอกความยาว: "))
    area = width * length
    print("พื้นที่สี่เหลี่ยมผืนผ้า =", area)

elif choice == 4:
    base = float(input("กรอกความยาวฐาน: "))
    height = float(input("กรอกความสูง: "))
    area = 0.5 * base * height
    print("พื้นที่สามเหลี่ยม =", area)

else:
    print("กรุณาเลือกหมายเลข 1-4")
