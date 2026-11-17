from tu_dien_tang_san import (
    c01_cau_tai, c02_cong_danh, c03_hon_nhan, c04_xuat_hanh,
    c05_benh_tat, c06_thua_kien, c07_duong_trach, c08_am_trach,
    c09_gia_dao, c10_thi_cu
)

UNG_KY_QUY_TAC = """
CHƯƠNG 11: KHẨU QUYẾT ĐỊNH ỨNG KỲ (TĂNG SAN BỐC DỊCH):
- Dụng Thần lâm Nguyệt Kiến hoặc Nhật Thần: Ứng ngay trong tháng/ngày hiện tại hoặc ngày Địa Chi của Dụng Thần.
- Hào động Hóa Tiến Thần: Lực tăng mạnh, ứng vào ngày/tháng Tiến Thần.
- Hào động Hóa Thoái Thần: Lực rút lui giảm dần, ứng vào ngày Thoái Thần hoặc ngày xung hào động.
- Dụng Thần lâm Tuần Không: Đợi ngày Xuất Không hoặc Xung Không mới thành.
- Dụng Thần gặp Nhị Hợp: Đợi ngày Xung Hợp mới khởi sự hoặc thành công.
"""

def tra_cuu_tu_dien(cau_hoi):
    ql = cau_hoi.lower()
    if any(w in ql for w in ["kiện", "thưa", "tranh chấp", "tòa", "pháp luật"]): return c06_thua_kien.INFO
    if any(w in ql for w in ["bệnh", "ốm", "đau", "thuốc", "sức khỏe"]): return c05_benh_tat.INFO
    if any(w in ql for w in ["xuất hành", "đi xa", "du lịch", "chuyển đi", "lên đường"]): return c04_xuat_hanh.INFO
    if any(w in ql for w in ["vợ", "chồng", "hôn nhân", "tình duyên", "tình cảm", "yêu", "cưới"]): return c03_hon_nhan.INFO
    if any(w in ql for w in ["danh", "chức", "thăng", "tiến", "xin việc", "quan"]): return c02_cong_danh.INFO
    if any(w in ql for w in ["mộ phần", "phần mộ", "mộ tổ", "mộ ông", "mộ bà", "mả", "âm trạch", "sang cát", "bốc mộ", "tảo mộ"]): return c08_am_trach.INFO
    if any(w in ql for w in ["nhà", "đất", "gia trạch", "xây", "sửa", "căn hộ"]): return c07_duong_trach.INFO
    if any(w in ql for w in ["gia đạo", "gia đình", "người nhà", "trong nhà"]): return c09_gia_dao.INFO
    if any(w in ql for w in ["thi", "học", "đỗ", "trượt", "bằng cấp"]): return c10_thi_cu.INFO
    return c01_cau_tai.INFO
