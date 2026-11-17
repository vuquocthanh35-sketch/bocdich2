with open("so_tay_tang_san.py", "r") as f:
    code = f.read()

gia_dao_block = '''CHUONG_SACH["GIA_DAO"] = {
    "ten": "Chương Gia Đạo & Hòa Khí Gia Đình",
    "dung_than": "Hào Thế",
    "khau_quyet": (
        "- Xem Gia Đạo (hòa khí, bình an của gia đình) lấy Hào Thế làm gia chủ; TUYỆT ĐỐI KHÔNG phán chuyện mua bán nhà đất (Gia Trạch) trừ khi khách hỏi rõ về nhà/đất.\\n"
        "- Tử Tôn là phúc thần: Tử Tôn vượng hoặc động là gia đạo bình an, con cái thuận hòa, có tin vui.\\n"
        "- Quan Quỷ là lo âu/tai họa: Quan Quỷ động hoặc khắc Thế là trong nhà có chuyện bất an, thị phi hoặc có người ốm đau.\\n"
        "- Huynh Đệ động: Cẩn thận anh em bất hòa hoặc hao tốn tiền của chung trong nhà.\\n"
        "- Quẻ Lục Hợp hoặc Thế Ứng tương sinh: Gia đình trên dưới thuận hòa, ấm êm."
    )
}

def chon_chuong_sach(cau_hoi):
    ql = cau_hoi.lower()
    if any(w in ql for w in ["kiện", "thưa", "tranh chấp", "tòa", "pháp luật"]): return CHUONG_SACH["THUA_KIEN"]
    if any(w in ql for w in ["bệnh", "ốm", "đau", "thuốc", "sức khỏe"]): return CHUONG_SACH["BENH_TAT"]
    if any(w in ql for w in ["xuất hành", "đi xa", "du lịch", "chuyển đi", "lên đường"]): return CHUONG_SACH["XUAT_HANH"]
    if any(w in ql for w in ["vợ", "chồng", "hôn nhân", "tình duyên", "tình cảm", "yêu", "cưới"]): return CHUONG_SACH["HON_NHAN"]
    if any(w in ql for w in ["danh", "chức", "thăng", "tiến", "xin việc", "quan"]): return CHUONG_SACH["CONG_DANH"]
    if any(w in ql for w in ["gia đạo", "gia đình", "người nhà", "trong nhà"]): return CHUONG_SACH["GIA_DAO"]
    if any(w in ql for w in ["nhà", "đất", "gia trạch", "mua xe", "thi", "học", "xây", "sửa"]): return CHUONG_SACH["GIA_TRACH"]
    return CHUONG_SACH["CAU_TAI"]'''

start = code.find("def chon_chuong_sach(cau_hoi):")
end = code.find("CHUONG_UNG_KY =")
if start != -1 and end != -1:
    code = code[:start] + gia_dao_block + "\n\n" + code[end:]

with open("so_tay_tang_san.py", "w") as f:
    f.write(code)

# Cập nhật cả bên engine_dich.py để gia đạo lấy Hào Thế thay vì Phụ Mẫu
with open("engine_dich.py", "r") as f:
    ed = f.read()

ed = ed.replace('["nhà", "đất", "gia trạch", "gia đạo", "xe", "giấy", "thi", "học", "hợp đồng"]', '["nhà", "đất", "gia trạch", "xe", "giấy", "thi", "học", "hợp đồng"]')
with open("engine_dich.py", "w") as f:
    f.write(ed)

print("Da tach rieng Chuong Gia Dao chuan xac!")
