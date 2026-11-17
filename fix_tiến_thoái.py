with open("engine_dich.py", "r") as f:
    code = f.read()

# Bổ sung nhận diện Hóa Tiến, Hóa Thoái, Hồi đầu sinh, Hồi đầu khắc
old_hd_block = """    c_hd, h_hd, lt_hd = cc[hd-1], HANH[cc[hd-1]], luc_than(hc, HANH[cc[hd-1]]).strip()
    c_hb, h_hb, lt_hb = cb[hd-1], HANH[cb[hd-1]], luc_than(hc, HANH[cb[hd-1]]).strip()
    td_len_dt = tinh_sinh_khac_chi_tiet(h_hd, c_hd, h_dt, c_dt)
    uk_str = f" | Ứng kỳ phá hợp: Ngày {XUNG[c_hd]} hoặc ngày {XUNG[c_dt]}" if "NHỊ HỢP" in td_len_dt else ""
    y_nghia_bien = " (Hóa Huynh Đệ -> Cảnh báo vấn đề tiền bạc, chi tiêu hao tốn hoặc người ngoài can thiệp)" if lt_hb == "Huynh Đệ" else ""
    bao_cao.append(f"2. HÀO ĐỘNG: Hào {hd} ({lt_hd} {c_hd} {h_hd}) động hóa {lt_hb} {c_hb} ({h_hb}){y_nghia_bien} -> Tác động lên Dụng Thần: {td_len_dt}{uk_str}")"""

new_hd_block = """    c_hd, h_hd, lt_hd = cc[hd-1], HANH[cc[hd-1]], luc_than(hc, HANH[cc[hd-1]]).strip()
    c_hb, h_hb, lt_hb = cb[hd-1], HANH[cb[hd-1]], luc_than(hc, HANH[cb[hd-1]]).strip()
    sinh_map = {"Kim": "Thủy", "Thủy": "Mộc", "Mộc": "Hỏa", "Hỏa": "Thổ", "Thổ": "Kim"}
    khac_map = {"Kim": "Mộc", "Mộc": "Thổ", "Thổ": "Thủy", "Thủy": "Hỏa", "Hỏa": "Kim"}
    bien_chat = []
    if (c_hd, c_hb) in TIEN_THAN: bien_chat.append("HÓA TIẾN THẦN (Lực tăng tiến mạnh mẽ, càng về sau càng phát)")
    elif (c_hd, c_hb) in THOAI_THAN: bien_chat.append("HÓA THOÁI THẦN (Lực giảm dần, rút lui; ban đầu có nhưng sau yếu dần)")
    elif sinh_map[h_hb] == h_hd: bien_chat.append("HỒI ĐẦU SINH (Rất tốt, được trợ lực mạnh)")
    elif khac_map[h_hb] == h_hd: bien_chat.append("HỒI ĐẦU KHẮC (Bất lợi, tự gặp trở ngại)")
    elif XUNG[c_hd] == c_hb: bien_chat.append("HÓA PHẢN NGÂM (Biến động lặp đi lặp lại)")
    bc_str = f" [{' | '.join(bien_chat)}]" if bien_chat else ""

    td_len_dt = tinh_sinh_khac_chi_tiet(h_hd, c_hd, h_dt, c_dt)
    uk_str = f" | Ứng kỳ phá hợp: Ngày {XUNG[c_hd]} hoặc ngày {XUNG[c_dt]}" if "NHỊ HỢP" in td_len_dt else ""
    y_nghia_bien = " (Hóa Huynh Đệ -> Cảnh báo hao tốn tiền bạc)" if lt_hb == "Huynh Đệ" else ""
    bao_cao.append(f"2. DUY NHẤT HÀO ĐỘNG: Hào {hd} ({lt_hd} {c_hd} {h_hd}) động hóa {lt_hb} {c_hb} ({h_hb}){bc_str}{y_nghia_bien} -> Tác động lên Dụng Thần: {td_len_dt}{uk_str} (LƯU Ý: Tất cả các hào khác đều TĨNH, không được đem Kỵ Thần tĩnh ra dọa khách!)")"""

code = code.replace(old_hd_block, new_hd_block)
with open("engine_dich.py", "w") as f:
    f.write(code)
print("Da nang cap Hoa Tien/Thoai & Loc Hao Tinh thanh cong!")
