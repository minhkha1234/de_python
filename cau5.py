# CAU 5: Xay dung lop DienThoai

class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        print("Ma may:", self.MaMay)
        print("Ten may:", self.TenMay)
        print("Hang san xuat:", self.HangSanXuat)
        print("Dung luong pin:", self.DungLuongPin, "mAh")
        print("Gia ban:", self.GiaBan, "dong")
        print("-" * 35)


# Tao 2 doi tuong theo dung de bai
DT01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
DT02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

# Goi phuong thuc hien thi thong tin
DT01.thongtindienthoai()
DT02.thongtindienthoai()
