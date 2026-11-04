# CAU 2: Xu ly chuoi

s = input("Nhap chuoi s: ")

# a. Dem so ky tu chu hoa
dem_hoa = 0
for ch in s:
    if ch.isupper():
        dem_hoa += 1
print("So ky tu chu hoa:", dem_hoa)

# b. Kiem tra chuoi doi xung
if s == s[::-1]:
    print("Chuoi doi xung")
else:
    print("Chuoi khong doi xung")

# c. Tinh tong cac chu so trong chuoi
tong = 0
for ch in s:
    if ch.isdigit():
        tong += int(ch)
print("Tong cac chu so:", tong)
