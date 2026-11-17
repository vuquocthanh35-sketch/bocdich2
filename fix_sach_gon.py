with open("so_tay_tang_san.py", "r") as f:
    code = f.read()

# Tách riêng hoàn toàn Gia Trạch (nhà đất) khỏi Thi Cử, bỏ hết câu gộp chung
old_gt = code[code.find('CHUONG_SACH["GIA_TRACH"]'):code.find('def chon_chuong_sach')]
new_gt = '''CHUONG_SACH["GIA_TRACH"] = {
    "ten": "Chương Gia Trạch & Nhà Đất",
    "dung_than": "Phụ Mẫu",
    "khau_quyet": (
        "- Lấy Phụ Mẫu làm nhà cửa, đất đai; Hào Thế là gia chủ.\\n"
        "- Phụ Mẫu vượng tướng sinh hợp Hào Thế: Mua bán, xây sửa nhà đất thuận lợi, ở yên ổn.\\n"
        "- Nếu Phụ Mẫu ẩn phục (không hiện trên quẻ) hoặc bị Nguyệt Phá, Nhật Phá, Thê Tài động khắc: Nhà đất còn vướng mắc, che khuất, chưa nên giao dịch ngay."
    )
}

CHUONG_SACH["THI_CU"] = {
    "ten": "Chương Thi Cử & Học Hành",
    "dung_than": "Phụ Mẫu",
    "khau_quyet": (
        "- Lấy Phụ Mẫu làm bài thi, kết quả học tập; Quan Quỷ làm công danh, bảng vàng.\\n"
        "- Phụ Mẫu và Quan Quỷ đều vượng tướng, không bị Tuần Không hay Thê Tài khắc chế: Thi cử đỗ đạt cao."
    )
}

'''
code = code.replace(old_gt, new_gt)
code = code.replace('if any(w in ql for w in ["nhà", "đất", "gia trạch", "mua xe", "thi", "học", "xây", "sửa"]): return CHUONG_SACH["GIA_TRACH"]',
                    'if any(w in ql for w in ["thi", "học", "đỗ", "trượt", "bằng cấp"]): return CHUONG_SACH["THI_CU"]\n    if any(w in ql for w in ["nhà", "đất", "gia trạch", "xây", "sửa"]): return CHUONG_SACH["GIA_TRACH"]')

with open("so_tay_tang_san.py", "w") as f:
    f.write(code)

# Cấm AI nhắc đến các chủ đề khách không hỏi trong ket_noi_ai.py
with open("ket_noi_ai.py", "r") as f:
    ai_code = f.read()

ai_code = ai_code.replace(
    "4. Trình bày 2-3 đoạn văn ngắn gọn (khoảng 180 chữ), ngôn từ Dịch học tinh tế, đi thẳng vào trọng tâm câu hỏi của khách.",
    "4. CHỈ NÓI ĐÚNG CHỦ ĐỀ KHÁCH HỎI (Ví dụ: khách hỏi 'gia trạch' thì chỉ nói về nhà đất, CẤM nhắc thêm thi cử, xe cộ hay giấy tờ nếu khách không hỏi). Trình bày 2 đoạn văn ngắn gọn (khoảng 150 chữ)."
)
with open("ket_noi_ai.py", "w") as f:
    f.write(ai_code)
print("Da go bo cac cau gop chung thanh cong!")
