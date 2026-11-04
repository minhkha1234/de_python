# CAU 3: Xu ly danh sach so nguyen

ds = []

# a. Nhap so nguyen, nhap 0 de ket thuc
while True:
    try:
        x = int(input("Nhap so nguyen (0 de ket thuc): "))
    except ValueError:
        print("Du lieu khong hop le. Hay nhap so nguyen!")
        continue

    if x == 0:
        break
    ds.append(x)

print("Danh sach vua nhap:", ds)

# b. Tinh tong cac so duong chan
tong = 0
for x in ds:
    if x > 0 and x % 2 == 0:
        tong += x
print("Tong cac so duong chan:", tong)

# c. Dem so lan xuat hien cua k
k = int(input("Nhap k can dem: "))
dem = 0
for x in ds:
    if x == k:
        dem += 1
print("So lan xuat hien cua", k, "la:", dem)
