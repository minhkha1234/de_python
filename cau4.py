# CAU 4: Quan ly sach bang tu dien

sach = {}
so_luong = int(input("Nhap so luong sach: "))

# a. Nhap thong tin sach va luu vao tu dien
for i in range(so_luong):
    print("\nNhap thong tin sach thu", i + 1)
    ma_sach = input("Ma so sach: ")
    ten_sach = input("Ten sach: ")
    tac_gia = input("Ten tac gia: ")
    nha_xuat_ban = input("Nha xuat ban: ")
    nam_xuat_ban = input("Nam xuat ban: ")

    sach[ma_sach] = {
        "Ten sach": ten_sach,
        "Ten tac gia": tac_gia,
        "Nha xuat ban": nha_xuat_ban,
        "Nam xuat ban": nam_xuat_ban
    }

# In danh sach sach
print("\nDANH SACH SACH TRONG THU VIEN")
for ma_sach, thong_tin in sach.items():
    print("\nMa so sach:", ma_sach)
    print("Ten sach:", thong_tin["Ten sach"])
    print("Ten tac gia:", thong_tin["Ten tac gia"])
    print("Nha xuat ban:", thong_tin["Nha xuat ban"])
    print("Nam xuat ban:", thong_tin["Nam xuat ban"])

# b. Tim ma sach va xoa neu ton tai
ma_can_xoa = input("\nNhap ma so sach can tim va xoa: ")
if ma_can_xoa in sach:
    del sach[ma_can_xoa]
    print("Da xoa cuon sach co ma:", ma_can_xoa)
else:
    print("Khong tim thay cuon sach can xoa")

print("\nDANH SACH SACH SAU KHI XOA")
for ma_sach, thong_tin in sach.items():
    print(ma_sach, "-", thong_tin)
