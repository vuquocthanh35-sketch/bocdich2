UNG_KY_QUY_TAC = """
BẢNG QUY TẮC ỨNG KỲ CHUẨN TĂNG SAN BỐC DỊCH (DÃ HẠC LÃO NHÂN):
1. Nguyên lý chung: Dụng Thần vượng tướng thì ứng vào ngày/tháng xung phá hoặc khắc xuất; Dụng Thần hưu tù suy yếu thì ứng vào ngày/tháng sinh phù hoặc lâm trị.
2. Tuần Không (Không Vong):
   - Dụng Thần hữu khí (vượng) gặp Tuần Không: Ứng vào ngày/tháng Xuất Không (hết tuần) hoặc Xung Không (xung thực).
   - Dụng Thần vô khí (hưu tù) gặp Tuần Không: Là Chân Không, khó thành sự, nếu thành chỉ ứng nhẹ lúc xuất không nhưng dễ tan.
3. Nhị Hợp & Tam Hợp:
   - Dụng Thần tĩnh gặp Nhật/Nguyệt hợp hoặc hào động hợp trói (Hợp Trụ): Phải đợi đến ngày/tháng Xung phá hợp mới ứng nghiệm.
   - Dụng Thần động hóa hợp: Gọi là Hóa Hợp, việc bị trì hoãn, đợi ngày xung khai mới xong.
4. Nguyệt Phá & Nhật Xung:
   - Dụng Thần bị Nguyệt Phá: Đợi ngày/tháng Điền Thực (lâm trị) hoặc Hợp phá mới có chuyển biến.
   - Hào tĩnh vượng gặp Nhật Xung gọi là Ám Động: Sự việc diễn ra gấp gáp, ứng ngay trong ngày hoặc trong tuần.
5. Tiến Thần & Thoái Thần:
   - Động hóa Tiến Thần (Hợi->Tý, Dần->Mão, Tỵ->Ngọ, Thân->Dậu, Sửu->Thìn, Thìn->Mùi, Mùi->Tuất, Tuất->Sửu): Thế lực đang tăng tiến, việc càng về sau càng thuận.
   - Động hóa Thoái Thần (ngược lại): Thế lực rút lui, nên thu quân hoặc giữ nguyên hiện trạng.
"""

TU_DIEN_12_CHUONG = [
    {
        "tu_khoa": ["bố", "cha", "mẹ", "má", "ông", "bà", "phụ huynh"],
        "ten": "Chương 5 (Mở rộng): Hỏi Việc / Sức Khỏe Của Bậc Trưởng Bối (Cha Mẹ)",
        "dung_than": "Phụ Mẫu",
        "khau_quyet": "Hỏi cho cha mẹ lấy Phụ Mẫu làm Dụng Thần. Quan Quỷ sinh Phụ Mẫu là tốt (có quý nhân/thầy thuốc giúp); Thê Tài khắc Phụ Mẫu là kỵ thần gây bất lợi. Nếu hỏi bệnh cha mẹ mà Tử Tôn động khắc Quan Quỷ thì bệnh mau khỏi, nhưng nếu Thê Tài động khắc Phụ Mẫu thì sức khỏe suy giảm."
    },
    {
        "tu_khoa": ["con", "bé", "cháu", "thai", "sinh nở", "bầu"],
        "ten": "Chương 4 & 5: Hỏi Việc Con Cái & Sinh Nở",
        "dung_than": "Tử Tôn",
        "khau_quyet": "Hỏi cho con cái lấy Tử Tôn làm Dụng Thần. Huynh Đệ sinh Tử Tôn là trợ lực tốt; Phụ Mẫu động khắc Tử Tôn là kỵ thần gây trở ngại hoặc lo âu cho con."
    },
    {
        "tu_khoa": ["anh", "em", "chị", "bạn", "đồng nghiệp", "đối tác"],
        "ten": "Luận Lục Thân: Hỏi Việc Anh Em / Bạn Bè",
        "dung_than": "Huynh Đệ",
        "khau_quyet": "Hỏi cho anh em bạn bè đồng trang lứa lấy Huynh Đệ làm Dụng Thần. Phụ Mẫu sinh Huynh Đệ là có người nâng đỡ; Quan Quỷ khắc Huynh Đệ là gặp áp lực, rắc rối."
    },
    {
        "tu_khoa": ["nợ", "đòi", "mượn", "vay", "trả"],
        "ten": "Chương 1: Đòi Nợ & Vay Mượn Tiền Bạc",
        "dung_than": "Thê Tài",
        "khau_quyet": "Đòi nợ lấy Thê Tài làm Dụng Thần, Hào Ứng là người nợ. Tài vượng sinh hợp Thế thì đòi được; Tài hưu tù không vong hoặc Ứng sinh hợp Huynh Đệ là người nợ khất lần chưa trả. Vay tiền cần Ứng sinh hợp Thế và Tài vượng."
    },
    {
        "tu_khoa": ["tiền", "tài", "buôn", "bán", "kinh doanh", "lãi", "vốn", "đầu tư", "chứng khoán", "lộc", "thu nhập"],
        "ten": "Chương 1: Cầu Tài, Kinh Doanh & Đầu Tư",
        "dung_than": "Thê Tài",
        "khau_quyet": "Cầu tài lấy Thê Tài làm gốc, Tử Tôn là phúc thần sinh tài, Huynh Đệ là kỵ thần đoạt tài. Tài vượng mà Tử Tôn động thì nguồn lợi dồi dào bền vững. Tài vượng nhưng Huynh Đệ cũng động thì có tiền vào nhưng dễ hao tán, bị chia phần. Tuyệt đối kỵ Phụ Mẫu động khắc Tử Tôn làm đứt nguồn sinh tài."
    },
    {
        "tu_khoa": ["thi", "học", "đỗ", "trượt", "bài", "điểm", "tuyển", "trường"],
        "ten": "Chương 10: Thi Cử & Học Hành",
        "dung_than": "Quan Quỷ & Phụ Mẫu",
        "khau_quyet": "Thi cử xem cả Quan Quỷ (danh vị) và Phụ Mẫu (bài vở, văn thư). Cả hai đều vượng tướng, không bị Tuần Không hay Nguyệt Phá, lại sinh hợp Hào Thế thì đỗ đạt cao. Kỵ nhất Thê Tài động khắc Phụ Mẫu (bài làm sai sót) hoặc Tử Tôn động khắc Quan Quỷ (trượt danh)."
    },
    {
        "tu_khoa": ["chức", "công danh", "việc làm", "thăng", "xin việc", "phỏng vấn", "sếp", "công ty", "nghề"],
        "ten": "Chương 2: Công Danh, Xin Việc & Thăng Tiến",
        "dung_than": "Quan Quỷ",
        "khau_quyet": "Cầu danh xin việc lấy Quan Quỷ làm Dụng Thần, Phụ Mẫu là giấy tờ quyết định, Thê Tài là nguồn sinh Quan (tiền lương, hậu thuẫn). Quan Quỷ vượng sinh hợp Thế thì đắc chức toại nguyện. Kỵ Tử Tôn động khắc Quan Quỷ (mất chức, trượt phỏng vấn) hoặc Huynh Đệ động tranh đoạt."
    },
    {
        "tu_khoa": ["vợ", "chồng", "yêu", "tình cảm", "hôn nhân", "cưới", "ly hôn", "người yêu", "chia tay"],
        "ten": "Chương 3: Hôn Nhân & Tình Cảm",
        "dung_than": "Thê Tài (Nam hỏi) / Quan Quỷ (Nữ hỏi)",
        "khau_quyet": "Nam hỏi tình duyên lấy Thê Tài làm Dụng Thần, nữ hỏi lấy Quan Quỷ làm Dụng Thần. Hào Thế là bản thân, Hào Ứng là đối phương. Thế Ứng tương sinh tương hợp, Dụng Thần vượng tướng thì tình cảm bền chặt. Quẻ biến Lục Xung hoặc Thế Ứng tương khắc dễ xảy ra mâu thuẫn chia ly."
    },
    {
        "tu_khoa": ["bệnh", "đau", "thuốc", "thầy", "khỏe", "tuổi thọ", "mổ", "viện"],
        "ten": "Chương 5: Bệnh Tật & Cầu Y Trị Bệnh",
        "dung_than": "Hào Thế (Tự hỏi bệnh)",
        "khau_quyet": "Tự xem bệnh của mình lấy Hào Thế làm Dụng Thần, Quan Quỷ là mầm bệnh, Tử Tôn là thuốc hay thầy giỏi. Tử Tôn vượng động khắc Quan Quỷ thì gặp đúng thầy đúng thuốc mà khỏi. Hào Thế vượng tướng không bị khắc là có sức đề kháng tốt; Quan Quỷ trì Thế hoặc hóa Tiến Thần là bệnh còn dai dẳng."
    },
    {
        "tu_khoa": ["mất", "tìm", "trộm", "rơi", "đồ", "xe", "ví", "điện thoại"],
        "ten": "Chương 6: Mất Của & Tìm Đồ Thất Lạc",
        "dung_than": "Thê Tài",
        "khau_quyet": "Tìm đồ lấy Thê Tài làm Dụng Thần. Tài vượng không bị không vong là đồ còn tìm lại được. Hào Tài tĩnh thì đồ đang nằm yên một chỗ quanh nhà; Tài gặp Nhị Hợp là bị vật khác che khuất; Tài động thì đồ đã bị di chuyển sang vị trí khác."
    },
    {
        "tu_khoa": ["đi", "xuất hành", "chuyến", "đường", "xa", "du lịch", "công tác", "về"],
        "ten": "Chương 7: Xuất Hành & Người Đi Xa",
        "dung_than": "Hào Thế (Tự đi) / Lục Thân tương ứng (Hỏi người đi)",
        "khau_quyet": "Tự xuất hành lấy Hào Thế làm chủ, Hào Ứng là nơi đến. Ứng sinh hợp Thế là chuyến đi thuận lợi, có người đón tiếp; Ứng khắc Thế hoặc Quan Quỷ động khắc Thế là đường đi trở ngại, nên hoãn hoặc cẩn trọng. Hỏi người đi xa bao giờ về: Dụng Thần động là đang trên đường về, Dụng Thần tĩnh thì chưa khởi hành."
    },
    {
        "tu_khoa": ["gia đạo", "nhà", "đất", "trạch", "mua nhà", "bán nhà", "thuê", "phong thủy", "xây"],
        "ten": "Chương 8: Gia Trạch & Mua Bán Nhà Đất",
        "dung_than": "Phụ Mẫu (Nhà đất) & Thê Tài (Giá cả/Lợi nhuận)",
        "khau_quyet": "Xem nhà cửa đất đai lấy Phụ Mẫu làm Dụng Thần, Hào 2 là trạch (ngôi nhà), Hào 5 là nhân (gia chủ). Phụ Mẫu vượng sinh hợp Thế là nhà đất tốt lành, mua bán thuận lợi. Kết hợp Lục Thần để định vị phương hướng trong nhà (Thanh Long bên trái, Bạch Hổ bên phải, Chu Tước phía trước, Huyền Vũ phía sau)."
    },
    {
        "tu_khoa": ["mộ", "mả", "âm phần", "mồ", "tổ tiên", "bốc mộ", "sang cát"],
        "ten": "Chương 9: Âm Phần & Mồ Mả Tổ Tiên",
        "dung_than": "Phụ Mẫu & Hào Thế",
        "khau_quyet": "Xem âm phần lấy Phụ Mẫu làm mộ phần, Hào Thế làm con cháu. Phụ Mẫu vượng tướng không bị Tuần Không, Nguyệt Phá hay xung khắc là long mạch yên ổn, phúc ấm cho con cháu. Kỵ Thê Tài động khắc Phụ Mẫu hoặc Hào 2/Hào 5 bị xung phá."
    },
    {
        "tu_khoa": ["kiện", "cãi", "tranh", "thị phi", "mâu thuẫn", "tòa", "đơn", "công an"],
        "ten": "Chương 12: Kiện Tụng & Tranh Chấp Thị Phi",
        "dung_than": "Hào Thế & Hào Ứng",
        "khau_quyet": "Tranh tụng lấy Hào Thế là mình, Hào Ứng là đối phương, Quan Quỷ là cơ quan xét xử. Thế vượng khắc Ứng là phần thắng nghiêng về mình; Ứng vượng khắc Thế là bất lợi nên hòa giải. Nếu quẻ chính hóa thành quẻ Lục Xung thì tranh chấp sẽ sớm giải tán, không kéo dài."
    }
]

def tra_cuu_tu_dien(cau_hoi):
    q = cau_hoi.lower()
    for muc in TU_DIEN_12_CHUONG:
        if any(w in q for w in muc["tu_khoa"]):
            return muc
    return {
        "ten": "Luận Giải Tổng Hợp Vạn Sự (Tăng San Bốc Dịch)",
        "dung_than": "Hào Thế & Dụng Thần theo sự việc",
        "khau_quyet": "Phàm xem vạn sự lấy Hào Thế làm chủ thể bản thân, tìm đúng Lục Thân đại diện cho việc cần hỏi làm Dụng Thần. Dụng Thần vượng tướng sinh hợp Hào Thế là cát tường thành sự; hưu tù, Tuần Không, Nguyệt Phá hoặc bị Kỵ Thần động khắc là hung trở."
    }
