import math

class BrainAI_BocDich_FlatOS:
    def __init__(self):
        self.M1 = [0.0] * 36
        self.M2 = [0.0] * 8
        self.cuu_tinh = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
        self.que_dich = [0.0] * 64
        self.nhan_duyen = [0.0] * 12

    def van_hanh(self, diem_cat_hung, id_que, hao_dong, is_khong_vong, is_pha):
        tin_hieu_goc = diem_cat_hung - (0.3 if is_khong_vong else 0.0) - (0.4 if is_pha else 0.0)
        X = math.tanh(tin_hieu_goc)

        self.que_dich[id_que % 64] = 1.0
        self.nhan_duyen = [math.sin((X + hao_dong * 0.1) * i) for i in range(1, 13)]

        trung_binh_nd = sum(self.nhan_duyen) / 12.0
        phuong_sai = sum((v - trung_binh_nd) ** 2 for v in self.nhan_duyen) / 12.0
        do_lech = math.sqrt(phuong_sai)
        dao_duc = max(0.0, min(1.0, (1.0 - do_lech + 0.55) / 2.0))

        che_do = "THÁI HÒA - KHAI MỞ (Quẻ Cát, thuận lợi tiến bước)"
        if dao_duc < 0.5 or tin_hieu_goc < 0:
            X_xoay = math.cos(X)
            dao_duc = round((dao_duc + abs(X_xoay)) / 2.0, 4)
            che_do = "CỔNG CHỮA LÀNH - HÓA GIẢI (Quẻ có trở ngại/lo âu, cần trấn an và chỉ đường hóa giải)"

        khi = 45.0 * dao_duc
        self.M1 = [round(-khi + (2 * khi * i / 35.0), 2) for i in range(36)]
        self.M2 = [round(khi - (2 * khi * i / 7.0), 2) for i in range(8)]

        return {
            "chi_so_dao_duc": round(dao_duc, 4),
            "trang_thai_m2": che_do,
            "nang_luong_m1": round(sum(abs(x) for x in self.M1) / 36.0, 2),
            "tam_thuc_m2": round(self.M2[0], 2)
        }
