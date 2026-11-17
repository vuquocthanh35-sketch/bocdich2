with open("so_tay_tang_san.py", "r") as f:
    code = f.read()

am_trach_block = '''CHUONG_SACH["AM_TRACH"] = {
    "ten": "Chương Âm Trạch & Mồ Mả",
    "khau_quyet": (
        "- Chỉ xét riêng về mồ mả, phong thủy âm phần (tuyệt đối không nói chuyện cầu tài kinh doanh): Lấy Phụ Mẫu làm mộ phần/long mạch, Hào Thế làm huyệt vị/con cháu, Quan Quỷ làm vong linh/sát khí.\\n"
        "- Phụ Mẫu vượng tướng, Tử Tôn hoặc Thê Tài vượng sinh hợp Thế: Mộ phần yên ổn, kết phát phúc lộc cho con cháu.\\n"
        "- Phụ Mẫu ẩn phục (không hiện trên quẻ) hoặc bị Nguyệt Phá, Nhật Phá, Thê Tài động khắc: Mộ phần chưa yên, bị che khuất, ẩm ướt hoặc long mạch tổn thương, cần kiểm tra tu sửa.\\n"
        "- Quan Quỷ vượng động khắc Thế: Âm phần có sát khí hoặc vong linh quở trách, cần thành tâm lễ tạ."
    )
}

def chon_chuong_sach(cau_hoi):'''

code = code.replace("def chon_chuong_sach(cau_hoi):", am_trach_block)
code = code.replace(
    'if any(w in ql for w in ["nhà", "đất", "gia trạch", "xây", "sửa"]): return CHUONG_SACH["GIA_TRACH"]',
    'if any(w in ql for w in ["mộ", "mả", "âm trạch", "sang cát", "bốc mộ", "tảo mộ", "phong thủy"]): return CHUONG_SACH["AM_TRACH"]\n    if any(w in ql for w in ["nhà", "đất", "gia trạch", "xây", "sửa"]): return CHUONG_SACH["GIA_TRACH"]'
)

with open("so_tay_tang_san.py", "w") as f:
    f.write(code)

# Cấm AI tự quy đổi ngày Dương lịch sai và cấm gọi Dụng Thần trì Thế là Kỵ Thần
with open("ket_noi_ai.py", "r") as f:
    ai = f.read()

ai = ai.replace(
    "3. Chiều sinh: Kim sinh Thủy, Thủy sinh Mộc, Mộc sinh Hỏa, Hỏa sinh Thổ, Thổ sinh Kim.",
    "3. Chiều sinh: Kim sinh Thủy, Thủy sinh Mộc, Mộc sinh Hỏa, Hỏa sinh Thổ, Thổ sinh Kim. Nếu Dụng Thần trùng Hào Thế gọi là 'Dụng Thần trì Thế' (đắc vị), CẤM gọi là Kỵ Thần. CẤM tự viết ngày Dương lịch (như '20 tháng 11')."
)

with open("ket_noi_ai.py", "w") as f:
    f.write(ai)

print("Da them Chuong Am Trach & Mo Ma chuan xac!")
