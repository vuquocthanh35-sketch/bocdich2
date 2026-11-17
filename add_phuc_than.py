with open("engine_dich.py", "r") as f:
    code = f.read()

old_dt_search = """    # Tạo báo cáo chuẩn xác 100% cho AI
    bao_cao = [f"0. TƯỢNG QUẺ CHỦ - BIẾN: {danh_gia_tuong_que(th, ha, tb, hb, cau_hoi)}"]
    dt_idx = the - 1
    if dt_muc_tieu != "Hào Thế":
        for idx_h in range(6):
            if luc_than(hc, HANH[cc[idx_h]]).strip() == dt_muc_tieu:
                dt_idx = idx_h
                break
    c_dt, h_dt, lt_dt = cc[dt_idx], HANH[cc[dt_idx]], luc_than(hc, HANH[cc[dt_idx]]).strip()
    ts_dt = " (Gặp Trường Sinh tại Nguyệt Kiến)" if TRUONG_SINH_NGUYET[h_dt] == chi_nguyet else ""
    bao_cao.append(f"1. DỤNG THẦN CHÍNH: Hào {dt_idx+1} - {lt_dt} {c_dt} ({h_dt}){ts_dt} | Nguyệt {chi_nguyet}: {tinh_sinh_khac_chi_tiet(HANH[chi_nguyet], chi_nguyet, h_dt, c_dt)}")"""

new_dt_search = """    # Tạo báo cáo chuẩn xác 100% cho AI (Có hỗ trợ tìm Phục Thần khi Dụng Thần vắng mặt)
    bao_cao = [f"0. TƯỢNG QUẺ CHỦ - BIẾN: {danh_gia_tuong_que(th, ha, tb, hb, cau_hoi)}"]
    dt_idx = None
    if dt_muc_tieu == "Hào Thế":
        dt_idx = the - 1
    else:
        for idx_h in range(6):
            if luc_than(hc, HANH[cc[idx_h]]).strip() == dt_muc_tieu:
                dt_idx = idx_h
                break

    if dt_idx is not None:
        c_dt, h_dt, lt_dt = cc[dt_idx], HANH[cc[dt_idx]], luc_than(hc, HANH[cc[dt_idx]]).strip()
        ts_dt = " (Gặp Trường Sinh tại Nguyệt Kiến)" if TRUONG_SINH_NGUYET[h_dt] == chi_nguyet else ""
        bao_cao.append(f"1. DỤNG THẦN CHÍNH: Hào {dt_idx+1} - {lt_dt} {c_dt} ({h_dt}){ts_dt} | Nguyệt {chi_nguyet}: {tinh_sinh_khac_chi_tiet(HANH[chi_nguyet], chi_nguyet, h_dt, c_dt)}")
    else:
        # Dụng Thần không hiện trên quẻ -> Tra cứu Phục Thần từ quẻ Bát Thuần của Cung
        c_bat_thuan = NOI_GIAP[c_idx] + NGOAI_GIAP[c_idx]
        phuc_idx = 0
        for idx_bt in range(6):
            if luc_than(hc, HANH[c_bat_thuan[idx_bt]]).strip() == dt_muc_tieu:
                phuc_idx = idx_bt
                break
        c_dt, h_dt, lt_dt = c_bat_thuan[phuc_idx], HANH[c_bat_thuan[phuc_idx]], dt_muc_tieu
        c_phi, h_phi, lt_phi = cc[phuc_idx], HANH[cc[phuc_idx]], luc_than(hc, HANH[cc[phuc_idx]]).strip()
        qh_phi_phuc = tinh_sinh_khac_chi_tiet(h_phi, c_phi, h_dt, c_dt)
        qh_nguyet_phuc = tinh_sinh_khac_chi_tiet(HANH[chi_nguyet], chi_nguyet, h_dt, c_dt)
        bao_cao.append(
            f"1. DỤNG THẦN VẮNG MẶT (PHỤC THẦN): Dụng Thần {lt_dt} {c_dt} ({h_dt}) không hiện trên quẻ, đang ẨN PHỤC tại Hào {phuc_idx+1} dưới Phi Thần {lt_phi} {c_phi} ({h_phi}) [{qh_phi_phuc}]. "
            f"Quan hệ Nguyệt {chi_nguyet} với Phục Thần: {qh_nguyet_phuc}. (CẢNH BÁO: Dụng Thần ẩn phục là sự việc/nhà đất/giấy tờ đang bị che khuất, khó thành ngay!)"
        )"""

code = code.replace(old_dt_search, new_dt_search)
with open("engine_dich.py", "w") as f:
    f.write(code)
print("Da tich hop he thong tim Phuc Than - Phi Than chuan Tang San Boc Dich!")
