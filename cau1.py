# CAU 1: Xu ly so nguyen duong n

def dem_chu_so_le(n):
    dem = 0
    while n > 0:
        chu_so = n % 10
        if chu_so % 2 != 0:
            dem += 1
        n //= 10
    return dem


def tinh_tong(n):
    tong = 0
    for i in range(1, n + 1):
        tong += 1 / (2 * i)
    return tong


n = int(input("Nhap n (1..1500): "))
while n < 1 or n > 1500:
    print("Gia tri khong hop le. Vui long nhap lai!")
    n = int(input("Nhap n (1..1500): "))

print("So luong chu so le:", dem_chu_so_le(n))
print("Tong S =", tinh_tong(n))
