
TIEN_THAN = {("Hợi","Tý"), ("Dần","Mão"), ("Tỵ","Ngọ"), ("Thân","Dậu"), ("Sửu","Thìn"), ("Thìn","Mùi"), ("Mùi","Tuất"), ("Tuất","Sửu")}
THOAI_THAN = {(b, a) for (a, b) in TIEN_THAN}
NHI_HOP = {("Tý","Sửu"), ("Sửu","Tý"), ("Dần","Hợi"), ("Hợi","Dần"), ("Mão","Tuất"), ("Tuất","Mão"), ("Thìn","Dậu"), ("Dậu","Thìn"), ("Tỵ","Thân"), ("Thân","Tỵ"), ("Ngọ","Mùi"), ("Mùi","Ngọ")}
TAM_HOP_CUC = [
    ({"Hợi", "Mão", "Mùi"}, "Mộc cục"),
    ({"Dần", "Ngọ", "Tuất"}, "Hỏa cục"),
    ({"Tỵ", "Dậu", "Sửu"}, "Kim cục"),
    ({"Thân", "Tý", "Thìn"}, "Thủy cục")
]
NGU_HANH_SINH = {"Kim": "Thủy", "Thủy": "Mộc", "Mộc": "Hỏa", "Hỏa": "Thổ", "Thổ": "Kim"}
NGU_HANH_KHAC = {"Kim": "Mộc", "Mộc": "Thổ", "Thổ": "Thủy", "Thủy": "Hỏa", "Hỏa": "Kim"}

def xet_vuong_suy_nguyet(h_hao, h_nguyet):
    if h_hao == h_nguyet: return "Vượng (Lâm Nguyệt)"
    if NGU_HANH_SINH.get(h_nguyet) == h_hao: return "Tướng (Nguyệt sinh)"
    if NGU_HANH_SINH.get(h_hao) == h_nguyet: return "Hưu (Sinh Nguyệt)"
    if NGU_HANH_KHAC.get(h_nguyet) == h_hao: return "Tử (Bị Nguyệt khắc)"
    return "Tù (Khắc Nguyệt)"

def phan_tich_nang_cao_tang_san(hc, cc, cb, hd, chi_ngay, chi_nguyet, HANH, XUNG, luc_than):
    ket_qua = []
    h_nguyet = HANH[chi_nguyet]
    chi_tap_hop = {chi_ngay, chi_nguyet}
    for i in range(6):
        c1 = cc[i]
        h1 = HANH[c1]
        lt_name = luc_than(hc, h1).strip()
        vs = xet_vuong_suy_nguyet(h1, h_nguyet)
        ghi_chu = [vs]
        if (c1, chi_ngay) in NHI_HOP: ghi_chu.append("Nhật Hợp")
        if (c1, chi_nguyet) in NHI_HOP: ghi_chu.append("Nguyệt Hợp")
        if XUNG.get(chi_ngay) == c1 and (i + 1) != hd:
            if "Vượng" in vs or "Tướng" in vs: ghi_chu.append("Ám Động")
        if (i + 1) == hd:
            c2 = cb[i]
            h2 = HANH[c2]
            chi_tap_hop.update([c1, c2])
            if (c1, c2) in TIEN_THAN: ghi_chu.append("Hóa Tiến Thần")
            elif (c1, c2) in THOAI_THAN: ghi_chu.append("Hóa Thoái Thần")
            elif (c1, c2) in NHI_HOP: ghi_chu.append("Động Hóa Hợp")
            elif XUNG.get(c1) == c2: ghi_chu.append("Hóa Phản Ngâm")
            if NGU_HANH_SINH.get(h2) == h1: ghi_chu.append("Hồi Đầu Sinh")
            elif NGU_HANH_KHAC.get(h2) == h1: ghi_chu.append("Hồi Đầu Khắc")
        ket_qua.append(f"   - Hào {i+1} ({lt_name} {c1}-{h1}): {', '.join(ghi_chu)}")
    for bo_tam_hop, ten_cuc in TAM_HOP_CUC:
        if bo_tam_hop.issubset(chi_tap_hop):
            ket_qua.append(f"1C. TAM HỢP CỤC: Hợp thành {ten_cuc} ({', '.join(bo_tam_hop)})!")
    return ket_qua

LUC_VI_MAP = {1: "Hào 1 (Nền móng, nhà trọ, cấp dưới)", 2: "Hào 2 (Gia đình, nội bộ, thân cận)", 3: "Hào 3 (Cửa ngõ, đồng nghiệp, đi lại)", 4: "Hào 4 (Cơ quan, quản lý trực tiếp)", 5: "Hào 5 (Lãnh đạo, vị trí trung tâm)", 6: "Hào 6 (Nơi phương xa, kết cục)"}
from datetime import timezone, timedelta, datetime, date
from lunardate import LunarDate
from data_dich import *

BAT_CUNG_CHUAN = {}
_QUAI_BITS = {
    "Càn": (1,1,1), "Đoài": (1,1,0), "Ly": (1,0,1), "Chấn": (1,0,0),
    "Tốn": (0,1,1), "Khảm": (0,1,0), "Cấn": (0,0,1), "Khôn": (0,0,0)
}
_BITS_QUAI = {v: k for k, v in _QUAI_BITS.items()}
for _cung, _b3 in _QUAI_BITS.items():
    _b = list(_b3 + _b3) # Bát Thuần: Hạ + Thượng
    BAT_CUNG_CHUAN[(_cung, _cung)] = (_cung, 6)
    for _step in range(5): # Nhất Thế -> Ngũ Thế (biến H1 -> H5)
        _b[_step] = 1 - _b[_step]
        _ha, _thuong = _BITS_QUAI[tuple(_b[:3])], _BITS_QUAI[tuple(_b[3:])]
        BAT_CUNG_CHUAN[(_thuong, _ha)] = (_cung, _step + 1)
    # Du Hồn: từ Ngũ Thế biến ngược Hào 4 (index 3)
    _b[3] = 1 - _b[3]
    BAT_CUNG_CHUAN[(_BITS_QUAI[tuple(_b[3:])], _BITS_QUAI[tuple(_b[:3])])] = (_cung, 4)
    # Quy Hồn: từ Du Hồn biến toàn bộ Hạ Quái (H1, H2, H3)
    for _i in range(3): _b[_i] = 1 - _b[_i]
    BAT_CUNG_CHUAN[(_BITS_QUAI[tuple(_b[3:])], _BITS_QUAI[tuple(_b[:3])])] = (_cung, 3)

from tu_dien_tang_san.c11_ung_ky import tra_cuu_tu_dien

QUE_LUC_XUNG = {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (1,4), (4,1)}
QUE_LUC_HOP = {(1,8), (8,1), (2,6), (6,2), (7,3), (3,7), (4,8), (8,4)}
LUC_HOP = {
    "Tý": "Sửu", "Sửu": "Tý", "Dần": "Hợi", "Hợi": "Dần",
    "Mão": "Tuất", "Tuất": "Mão", "Thìn": "Dậu", "Dậu": "Thìn",
    "Tỵ": "Thân", "Thân": "Tỵ", "Ngọ": "Mùi", "Mùi": "Ngọ"
}
TRUONG_SINH_NGUYET = {"Mộc": "Hợi", "Hỏa": "Dần", "Kim": "Tỵ", "Thủy": "Thân", "Thổ": "Thân"}
KY_THAN_MAP = {"Quan Quỷ": "Tử Tôn", "Thê Tài": "Huynh Đệ", "Phụ Mẫu": "Thê Tài", "Tử Tôn": "Phụ Mẫu", "Huynh Đệ": "Quan Quỷ"}

def danh_gia_tuong_que(th_c, ha_c, tb_c, hb_c, cau_hoi=""):
    ql = cau_hoi.lower()
    nhom_tan = any(w in ql for w in ["kiện", "thưa", "tranh chấp", "tranh cãi", "cãi", "thị phi", "xích mích", "mâu thuẫn", "bệnh", "họa", "tai", "ly hôn", "chia tay", "giải", "thoát", "tù"])
    cx, ch = (th_c, ha_c) in QUE_LUC_XUNG, (th_c, ha_c) in QUE_LUC_HOP
    bx, bh = (tb_c, hb_c) in QUE_LUC_XUNG, (tb_c, hb_c) in QUE_LUC_HOP
    if nhom_tan:
        if cx and bh: return "VIỆC CẦN GIẢI TÁN GẶP LỤC XUNG BIẾN LỤC HỢP (HUNG / DÂY DƯA): Mới đầu tưởng hòa giải êm đẹp, nhưng biến Lục Hợp là bị trói buộc kéo dài không dứt, về sau dễ sinh hận thù dai dẳng!"
        if ch and bx: return "VIỆC CẦN GIẢI TÁN GẶP LỤC HỢP BIẾN LỤC XUNG (CÁT / THOÁT NẠN): Ban đầu vướng mắc trói buộc, nhưng biến Lục Xung là tự động giải tán, thoát rắc rối nhanh chóng!"
        if cx: return "VIỆC CẦN GIẢI TÁN GẶP QUẺ LỤC XUNG (CÁT): Sự việc/kiện tụng/bệnh tật nhanh chóng giải tán, sớm dứt điểm!"
        if ch: return "VIỆC CẦN GIẢI TÁN GẶP QUẺ LỤC HỢP (HUNG): Sự việc bị trói buộc, dây dưa kéo dài khó dứt!"
    else:
        if cx and bh: return "VIỆC CẦN GẮN KẾT GẶP LỤC XUNG BIẾN LỤC HỢP (TRƯỚC DỮ SAU LÀNH): Ban đầu mâu thuẫn căng thẳng, tưởng chừng đổ vỡ, nhưng về sau sẽ hòa giải, gương vỡ lại lành!"
        if ch and bx: return "VIỆC CẦN GẮN KẾT GẶP LỤC HỢP BIẾN LỤC XUNG (TRƯỚC ẤM SAU TAN): Ban đầu êm đẹp thuận lợi, nhưng đề phòng rạn nứt, tan vỡ phút chót!"
        if bx: return "QUẺ BIẾN LỤC XUNG (ĐẠI CẢNH BÁO - TRƯỚC HỢP SAU TAN): Dù Dụng Thần vượng nhưng quẻ biến thành Lục Xung là tượng hợp tác không được lâu dài, dễ mâu thuẫn và chia tay giữa chừng!"
        if bh: return "QUẺ BIẾN LỤC HỢP (CÁT - BỀN CHẶT): Ban đầu có thể còn thăm dò nhưng kết quả cuối cùng sẽ gắn kết lâu dài, bền vững!"
        if cx: return "QUẺ LỤC XUNG (Chủ về mâu thuẫn, xung đột, phân ly hoặc khó bền)"
        if ch: return "QUẺ LỤC HỢP (Chủ về hòa hợp, gắn kết, dễ đồng thuận và bền vững)"
    return "Quẻ thông thường (Luận cát hung theo Dụng Thần và Hào Động)"

def tinh_sinh_khac_chi_tiet(h_nguon, c_nguon, h_dich, c_dich):
    sinh = {"Kim": "Thủy", "Thủy": "Mộc", "Mộc": "Hỏa", "Hỏa": "Thổ", "Thổ": "Kim"}
    khac = {"Kim": "Mộc", "Mộc": "Thổ", "Thổ": "Thủy", "Thủy": "Hỏa", "Hỏa": "Kim"}
    kq = []
    if sinh[h_nguon] == h_dich: kq.append("SINH PHÙ (Tốt)")
    elif khac[h_nguon] == h_dich: kq.append("KHẮC CHẾ (Xấu)")
    elif h_nguon == h_dich: kq.append("TỶ HÒA (Trợ giúp)")
    if LUC_HOP[c_nguon] == c_dich: kq.append("NHỊ HỢP (Gắn kết/Ràng buộc)")
    if XUNG[c_nguon] == c_dich: kq.append("LỤC XUNG (Xung đột/Phá bỏ)")
    return " + ".join(kq) if kq else "Không sinh khắc trực tiếp"

def kiem_tra_giao_thoi(dt):
    h, m = dt.hour, dt.minute
    if h % 2 == 0 and m >= 55: return True, (60 - m) + 5
    if h % 2 == 1 and m <= 5: return True, (5 - m) + 1
    return False, 0

def tim_cung_the(bc):
    h1, h2, h3, h4, h5, h6 = [int(x) for x in bc]
    noi, ngoai = f"{h1}{h2}{h3}", f"{h4}{h5}{h6}"
    ngu_the_cung = f"{1-h4}{1-h5}{h6}"
    doi_noi = f"{1-h1}{1-h2}{1-h3}"
    if h1 == h4 and h2 == h5 and h3 == h6: return BIN_QUAI[ngoai], 6, 3
    if h1 != h4 and h2 == h5 and h3 == h6: return BIN_QUAI[ngoai], 1, 4
    if h1 != h4 and h2 != h5 and h3 == h6: return BIN_QUAI[ngoai], 2, 5
    if h1 != h4 and h2 != h5 and h3 != h6: return BIN_QUAI[ngoai], 3, 6
    if h1 == h4 and h2 != h5 and h3 != h6: return BIN_QUAI[ngu_the_cung], 4, 1
    if h1 == h4 and h2 == h5 and h3 != h6: return BIN_QUAI[ngu_the_cung], 5, 2
    if h1 != h4 and h2 == h5 and h3 != h6: return BIN_QUAI[doi_noi], 4, 1
    return BIN_QUAI[noi], 3, 6

def luc_than(hc, hh):
    s = {"Kim": "Thủy", "Thủy": "Mộc", "Mộc": "Hỏa", "Hỏa": "Thổ", "Thổ": "Kim"}
    k = {"Kim": "Mộc", "Mộc": "Thổ", "Thổ": "Thủy", "Thủy": "Hỏa", "Hỏa": "Kim"}
    if hc == hh: return "Huynh Đệ"
    if s[hc] == hh: return "Tử Tôn  "
    if s[hh] == hc: return "Phụ Mẫu "
    if k[hc] == hh: return "Thê Tài "
    return "Quan Quỷ"

def lap_que_tang_san(cau_hoi):
    dt = datetime.now(timezone(timedelta(hours=7)))
    is_gt, phut_cho = kiem_tra_giao_thoi(dt)
    if is_gt:
        return "", f"⏳ **Giờ giao quẻ ({dt.strftime('%H:%M')} - Giờ VN)**\n\nHiện tại đang là khoảng giao thời giữa hai canh giờ. **Bạn hãy thành tâm hỏi lại sau khoảng {phut_cho} phút nữa** nhé!"

    chgio = ((dt.hour + 1) // 2) % 12
    dt_tinh = dt + timedelta(days=1) if dt.hour >= 23 else dt
    al = LunarDate.fromSolarDate(dt_tinh.year, dt_tinh.month, dt_tinh.day)
    sn = (dt_tinh.date() - date(2000, 1, 1)).days
    cn, chn = (4 + sn) % 10, (6 + sn) % 12
    chnam, chth = (al.year - 4) % 12, (al.month + 1) % 12
    canth = CAN[(((al.year - 4) % 5 * 2 + 2) + al.month - 1) % 10]
    cangio = CAN[((cn % 5) * 2 + chgio) % 10]
    chi_ngay, chi_nguyet = CHI[chn], CHI[chth]

    t1 = (chnam + 1) + al.month + al.day
    th = t1 % 8 or 8
    t2 = t1 + (chgio + 1)
    ha, hd = t2 % 8 or 8, t2 % 6 or 6

    bc = QUAI_BIN[ha] + QUAI_BIN[th]
    c_idx, the, ung = tim_cung_the(bc)
    tc, hc = QUAI_TEN[c_idx], QUAI_HANH[c_idx]
    cc = NOI_GIAP[ha] + NGOAI_GIAP[th]

    thu = ["Thanh Long", "Chu Tước ", "Câu Trần  ", "Đằng Xà   ", "Bạch Hổ   ", "Huyền Vũ  "]
    st = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 3, 6: 4, 7: 4, 8: 5, 9: 5}[cn]
    lt = [thu[(st + i) % 6] for i in range(6)]
    df = (chn - cn) % 12
    tk1, tk2 = CHI[(df - 2) % 12], CHI[(df - 1) % 12]

    bl = list(bc)
    bl[hd - 1] = '0' if bl[hd - 1] == '1' else '1'
    bb = "".join(bl)
    hb, tb = BIN_QUAI[bb[:3]], BIN_QUAI[bb[3:]]
    cb = NOI_GIAP[hb] + NGOAI_GIAP[tb]

    chuong = tra_cuu_tu_dien(cau_hoi)
    dt_muc_tieu = chuong["dung_than"]
    if any(w in cau_hoi.lower() for w in ["chồng", "bạn trai", "người yêu nam"]): dt_muc_tieu = "Quan Quỷ"
    elif any(w in cau_hoi.lower() for w in ["con", "cháu"]): dt_muc_tieu = "Tử Tôn"

    lines = [
        f"GIỜ VN (UTC+7): {dt.strftime('%H:%M - %d/%m/%Y')} | ÂM LỊCH: {al.day:02d}/{al.month:02d} ({CHI[chnam]})",
        f"GIỜ: {cangio} {CHI[chgio]} | NGÀY: {CAN[cn]} {chi_ngay} | THÁNG: {canth} {chi_nguyet} | KHÔNG: {tk1}-{tk2}",
        f"CUNG: {tc} ({hc}) | CHỦ: {QUAI_TEN[th]}-{QUAI_TEN[ha]} ➔ BIẾN: {QUAI_TEN[tb]}-{QUAI_TEN[hb]} (Động H{hd})",
        "-" * 68
    ]

    for i in range(5, -1, -1):
        n = i + 1
        c1, h1 = cc[i], HANH[cc[i]]
        mark = "Thế" if n == the else ("Ứng" if n == ung else "   ")
        tt = [t for t, cond in [("Tuần Không", c1 in [tk1, tk2]), ("Nhật Phá", XUNG[chi_ngay] == c1), ("Nguyệt Phá", XUNG[chi_nguyet] == c1)] if cond]
        tt_str = f"[{','.join(tt)}]" if tt else ""
        b_s = f"O-> {luc_than(hc, HANH[cb[i]]).strip()} {cb[i]}({HANH[cb[i]]})" if n == hd else ""
        lines.append(f"{lt[i]} | {luc_than(hc,h1)} {c1:<3}({h1:<4}) | {mark} | {b_s} {tt_str}")

    bao_cao = [f"0. TƯỢNG QUẺ CHỦ - BIẾN: {danh_gia_tuong_que(th, ha, tb, hb, cau_hoi)}"]
    dt_idx = the - 1 if dt_muc_tieu == "Hào Thế" else next((i for i in range(6) if luc_than(hc, HANH[cc[i]]).strip() == dt_muc_tieu), None)

    dt_bi_khong_pha = False
    if dt_idx is not None:
        c_dt, h_dt, lt_dt = cc[dt_idx], HANH[cc[dt_idx]], luc_than(hc, HANH[cc[dt_idx]]).strip()
        thu_dt = lt[dt_idx].strip()
        ts_dt = " (Gặp Trường Sinh tại Nguyệt)" if TRUONG_SINH_NGUYET[h_dt] == chi_nguyet else ""
        qh_nguyet = tinh_sinh_khac_chi_tiet(HANH[chi_nguyet], chi_nguyet, h_dt, c_dt)
        qh_nhat = tinh_sinh_khac_chi_tiet(HANH[chi_ngay], chi_ngay, h_dt, c_dt)

        tinh_trang_dt = []
        if c_dt in [tk1, tk2]: tinh_trang_dt.append(f"ĐANG TUẦN KHÔNG (Ứng kỳ bắt buộc: Xuất Không vào ngày {c_dt} hoặc Xung Không vào ngày {XUNG[c_dt]})")
        if XUNG[chi_ngay] == c_dt: tinh_trang_dt.append("BỊ NHẬT PHÁ (Nếu vượng là Ám Động)")
        if XUNG[chi_nguyet] == c_dt: tinh_trang_dt.append("BỊ NGUYỆT PHÁ")
        if tinh_trang_dt: dt_bi_khong_pha = True
        tt_dt_str = f" | Trạng thái đặc biệt: {', '.join(tinh_trang_dt)}" if tinh_trang_dt else ""

        bao_cao.append(
            f"1. DỤNG THẦN CHÍNH: Hào {dt_idx+1} - {lt_dt} {c_dt} ({h_dt}) lâm {thu_dt}{ts_dt} | "
            f"Nguyệt {chi_nguyet}: {qh_nguyet} | Nhật {chi_ngay}: {qh_nhat}{tt_dt_str}"
        )
    else:
        c_bat_thuan = NOI_GIAP[c_idx] + NGOAI_GIAP[c_idx]
        phuc_idx = next((i for i in range(6) if luc_than(hc, HANH[c_bat_thuan[i]]).strip() == dt_muc_tieu), 0)
        c_dt, h_dt, lt_dt = c_bat_thuan[phuc_idx], HANH[c_bat_thuan[phuc_idx]], dt_muc_tieu
        c_phi, h_phi, lt_phi = cc[phuc_idx], HANH[cc[phuc_idx]], luc_than(hc, HANH[cc[phuc_idx]]).strip()
        qh_nguyet = tinh_sinh_khac_chi_tiet(HANH[chi_nguyet], chi_nguyet, h_dt, c_dt)
        qh_nhat = tinh_sinh_khac_chi_tiet(HANH[chi_ngay], chi_ngay, h_dt, c_dt)
        dt_bi_khong_pha = True
        bao_cao.append(
            f"1. DỤNG THẦN ẨN PHỤC: Dụng Thần {lt_dt} {c_dt} ({h_dt}) không hiện trên quẻ, đang ẨN PHỤC tại Hào {phuc_idx+1} "
            f"dưới Phi Thần {lt_phi} {c_phi} ({h_phi}) [{tinh_sinh_khac_chi_tiet(h_phi, c_phi, h_dt, c_dt)}]. "
            f"Nguyệt {chi_nguyet}: {qh_nguyet} | Nhật {chi_ngay}: {qh_nhat}."
        )

    c_hd, h_hd, lt_hd = cc[hd-1], HANH[cc[hd-1]], luc_than(hc, HANH[cc[hd-1]]).strip()
    c_hb, h_hb, lt_hb = cb[hd-1], HANH[cb[hd-1]], luc_than(hc, HANH[cb[hd-1]]).strip()
    sinh_map = {"Kim": "Thủy", "Thủy": "Mộc", "Mộc": "Hỏa", "Hỏa": "Thổ", "Thổ": "Kim"}
    khac_map = {"Kim": "Mộc", "Mộc": "Thổ", "Thổ": "Thủy", "Thủy": "Hỏa", "Hỏa": "Kim"}
    bien_chat = []
    if (c_hd, c_hb) in TIEN_THAN: bien_chat.append("HÓA TIẾN THẦN (Lực tăng tiến mạnh)")
    elif (c_hd, c_hb) in THOAI_THAN: bien_chat.append("HÓA THOÁI THẦN (Lực giảm dần)")
    elif sinh_map[h_hb] == h_hd: bien_chat.append("HỒI ĐẦU SINH (Tốt, tự được trợ lực)")
    elif khac_map[h_hb] == h_hd: bien_chat.append("HỒI ĐẦU KHẮC (Xấu, tự chuốc bất lợi)")
    bc_str = f" [{' | '.join(bien_chat)}]" if bien_chat else ""

    td_len_dt = tinh_sinh_khac_chi_tiet(h_hd, c_hd, h_dt, c_dt)
    hb_len_hd = tinh_sinh_khac_chi_tiet(h_hb, c_hb, h_hd, c_hd)
    hb_len_dt = tinh_sinh_khac_chi_tiet(h_hb, c_hb, h_dt, c_dt)
    chi_tiet_bien = f" | Hào biến ({lt_hb} {c_hb}) quay lại với Hào động: {hb_len_hd}"
    if (hd - 1) != dt_idx:
        chi_tiet_bien += f" & với Dụng thần: {hb_len_dt}"
    td_len_dt += chi_tiet_bien
    if "NHỊ HỢP" in chi_tiet_bien:
        cac_chi_hop = {c_hd, c_hb}
        pha_hop = []
        if XUNG[chi_ngay] in cac_chi_hop: pha_hop.append(f"Nhật {chi_ngay} xung phá thế Hợp (Hợp xứ phùng xung -> Giải tỏa ràng buộc)")
        if XUNG[chi_nguyet] in cac_chi_hop: pha_hop.append(f"Nguyệt {chi_nguyet} xung phá thế Hợp (Hợp xứ phùng xung -> Giải tỏa ràng buộc)")
        if pha_hop:
            td_len_dt += " | ĐẶC BIỆT: " + " & ".join(pha_hop)
    uk_str = ""
    if "NHỊ HỢP" in td_len_dt:
        uk_str = f" | Ứng kỳ phá hợp: Ngày {XUNG[c_hd]} hoặc ngày {XUNG[c_dt]}"
    elif "LỤC XUNG" in td_len_dt:
        uk_str = f" | Ứng kỳ xung khởi/phá: Ngày {c_hd} hoặc ngày {LUC_HOP[c_dt]}"

    bao_cao.append(
        f"2. DUY NHẤT HÀO ĐỘNG: Hào {hd} ({lt_hd} {c_hd} {h_hd}) động BIẾN THÀNH {lt_hb} {c_hb} ({h_hb}){bc_str} "
        f"-> Tác động lên Dụng Thần: {td_len_dt}{uk_str} (Các hào khác đều TĨNH)."
    )

    c_the, h_the, lt_the = cc[the-1], HANH[cc[the-1]], luc_than(hc, HANH[cc[the-1]]).strip()
    thu_the = lt[the-1].strip()
    ky_than = KY_THAN_MAP.get(dt_muc_tieu, "")
    canh_bao_ky = f" -> ĐẠI KỴ: Hào Thế là KỴ THẦN ({ky_than}) khắc Dụng Thần ({dt_muc_tieu})!" if (ky_than and lt_the == ky_than) else ""
    bao_cao.append(f"3. HÀO THẾ (Người hỏi): Hào {the} - {lt_the} {c_the} ({h_the}) lâm {thu_the}{canh_bao_ky}")

    c_ung, h_ung, lt_ung = cc[ung-1], HANH[cc[ung-1]], luc_than(hc, HANH[cc[ung-1]]).strip()
    qh_tu = tinh_sinh_khac_chi_tiet(h_the, c_the, h_ung, c_ung)
    ts_ung = " -> ĐANG GẶP TRƯỜNG SINH TẠI NGUYỆT" if TRUONG_SINH_NGUYET[h_ung] == chi_nguyet else ""
    bao_cao.append(f"4. HÀO ỨNG (Đối phương/Môi trường): Hào {ung} ({lt_ung} {c_ung} {h_ung}) lâm {lt[ung-1].strip()}{ts_ung} | Thế-Ứng: {qh_tu}")

    toan_canh = ["5. DỮ LIỆU SINH KHẮC TỪNG HÀO (Dùng để AI tự xác định Dụng Thần bất kỳ):"]
    for i in range(6):
        c_i, h_i, lt_i = cc[i], HANH[cc[i]], luc_than(hc, HANH[cc[i]]).strip()
        thu_i = lt[i].strip()
        qh_ng = tinh_sinh_khac_chi_tiet(HANH[chi_nguyet], chi_nguyet, h_i, c_i)
        qh_nh = tinh_sinh_khac_chi_tiet(HANH[chi_ngay], chi_ngay, h_i, c_i)
        qh_hd = tinh_sinh_khac_chi_tiet(h_hd, c_hd, h_i, c_i) if (i + 1) != hd else "CHÍNH LÀ HÀO ĐỘNG"
        toan_canh.append(f"   - {LUC_VI_MAP[i+1]} | {lt_i} {c_i} ({h_i}) lâm {thu_i} | Nguyệt {chi_nguyet}: {qh_ng} | Nhật {chi_ngay}: {qh_nh} | Hào động {c_hd}: {qh_hd}")
    c_bt = NOI_GIAP[c_idx] + NGOAI_GIAP[c_idx]
    hien_co = {luc_than(hc, HANH[cc[i]]).strip() for i in range(6)}
    for idx_bt in range(6):
        lt_bt = luc_than(hc, HANH[c_bt[idx_bt]]).strip()
        if lt_bt not in hien_co:
            toan_canh.append(f"   - [ẨN PHỤC TẠI HÀO {idx_bt+1}]: {lt_bt} {c_bt[idx_bt]} ({HANH[c_bt[idx_bt]]}) ẩn dưới Phi Thần {luc_than(hc, HANH[cc[idx_bt]]).strip()} {cc[idx_bt]} ({HANH[cc[idx_bt]]})")
    bao_cao.extend(toan_canh)

    try:
        bao_cao.extend(phan_tich_nang_cao_tang_san(hc, cc, cb, hd, chi_ngay, chi_nguyet, HANH, XUNG, luc_than))
    except Exception:
        pass
    from ket_noi_ai import hoi_ai_boc_dich
    bang_que_str = "\n".join(lines)
    return bang_que_str, hoi_ai_boc_dich(cau_hoi, bang_que_str, dt_muc_tieu, "\n".join(bao_cao), dt_bi_khong_pha)
