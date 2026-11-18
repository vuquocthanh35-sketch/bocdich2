from tu_dien_tang_san.c11_ung_ky import tra_cuu_tu_dien, UNG_KY_QUY_TAC
import os
import re
from groq import Groq
from brain_m1_m2 import BrainAI_BocDich_FlatOS
from tu_dien_tang_san.c11_ung_ky import tra_cuu_tu_dien, UNG_KY_QUY_TAC

API_KEY = os.environ.get("GROQ_API_KEY", "")
client = Groq(api_key=API_KEY)
bo_nao_flat_os = BrainAI_BocDich_FlatOS()

MODELS = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]

def hoi_ai_boc_dich(cau_hoi, bang_que, dt_muc_tieu, diem_nong, dt_bi_khong_pha=False):
    chuong = tra_cuu_tu_dien(cau_hoi)
    
    diem_so = 0.6
    if any(k in diem_nong for k in ["HUNG", "ĐẠI KỴ", "KHẮC CHẾ", "THOÁI THẦN", "HỒI ĐẦU KHẮC"]):
        diem_so = -0.6
    elif "ẨN PHỤC" in diem_nong or dt_bi_khong_pha:
        diem_so = -0.2

    ket_qua_nao = bo_nao_flat_os.van_hanh(
        diem_so, 
        len(cau_hoi), 
        1, 
        "TUẦN KHÔNG" in diem_nong, 
        "NHẬT PHÁ" in diem_nong or "NGUYỆT PHÁ" in diem_nong
    )

    header_nao = (
        f"🧠 **[Hệ Thống M1-M2 FlatOS]** Cân bằng: `{ket_qua_nao['chi_so_dao_duc']}` | "
        f"Chuyên luận: *{chuong['ten']}*\n\n"
    )

    system_prompt = f"""Bạn là bậc thầy Bốc Dịch theo kinh điển "Tăng San Bốc Dịch" của Dã Hạc lão nhân.
Chuyên đề tham chiếu: {chuong['ten']}
Khẩu quyết: {chuong['khau_quyet']}
{UNG_KY_QUY_TAC}

NGUYÊN LÝ CỐT LÕI (Tự vận dụng linh hoạt, không máy móc):
1. Dụng Thần & Thế Ứng: Tự chọn đúng Lục Thân làm Dụng Thần theo đúng đối tượng khách hỏi từ dữ liệu Bán cầu M1 (kể cả hào Ẩn Phục). Thế là người hỏi, Ứng là đối phương/môi trường.
2. Nhật Nguyệt & Động Biến: Cân đong lực Phò (Sinh, Tỷ hòa) và Khắc (Khắc, Xung) của Nhật, Nguyệt, Hào Động lên Dụng Thần. Xét kỹ Hào Biến (Tiến/Thoái, Hợp/Xung) và Tượng Quẻ Chủ - Biến.
3. PHÉP TƯỢNG HÌNH KHÔNG GIAN & CẢNH QUAN (Khi xem Âm trạch, Nhà cửa, Tìm đồ):
   - Phối hợp Lục Thần định vị trái/phải: Thanh Long = bên trái / phương Đông; Bạch Hổ = bên phải / phương Tây; Chu Tước = phía trước / phương Nam; Huyền Vũ = phía sau / phương Bắc; Câu Trần/Đằng Xà = trung tâm / gò đống, đường đi.
   - Hình tượng hóa Ngũ Hành gặp Hợp/Xung: Thủy gặp Thổ Nhị Hợp trói buộc là tượng dòng nước/mạch nước bị đất đá chặn ứ lại cần khơi thông; Mộc bị Kim khắc là cây cối/rễ cây xâm lấn; Hào bị Xung Phá là sụt lún, nứt vỡ.
4. Diễn giải bình dị, dễ hiểu: Dịch thuật ngữ Dịch lý thành ngôn ngữ đời thường sáng rõ cho người không biết Dịch cũng hiểu ngay (cấm lặp lại từ "bình hòa" sáo rỗng). Tuyệt đối KHÔNG mê tín, KHÔNG xúi làm lễ/cúng bái/trấn an. Khi tính Ứng kỳ, phải đối chiếu với Thời gian thực tế lúc gieo quẻ để chỉ rõ ngày/tháng sắp tới (ví dụ hôm nay đã là ngày Mùi thì ứng vào ngày Sửu, ngày Ngọ tiếp theo).
5. Chuẩn xác tuyệt đối: Dùng đúng tên Can Chi, Lục Thân và chiều ngũ hành (Thổ khắc Thủy, Kim sinh Thủy...) từ M1.

CHUẨN MỰC NGÔN TỪ & HÀNH VĂN DỊCH HỌC VIỆT NAM:
- Hành văn tự nhiên, điềm đạm, chuẩn mực như một bậc trưởng bối am hiểu Dịch lý Việt Nam đang trò chuyện chân tình (khoảng 180-220 chữ, chia 2-3 đoạn mềm mại, KHÔNG dùng tiêu đề mục khô cứng).
- Dùng tiếng Việt thuần khiết, sáng rõ; tránh lạm dụng dấu ngoặc kép sáo rỗng (như "năng lượng", "đam mê", "điểm nghẽn") và tránh cách diễn đạt như văn dịch.
- Tuyệt đối KHÔNG lôi các hào ẩn phục không liên quan ra suy diễn hù dọa; KHÔNG tự tính hay ghi kèm ngày Dương lịch (chỉ nêu tên Địa Chi ngày/tháng Âm như ngày Tý, ngày Sửu, tháng Tý).
- Đọc chính xác tuyệt đối vị trí Hào Thế và Hào Ứng từ báo cáo M1, tuyệt đối không gộp nhầm tên của Thế và Ứng."""

    thoi_gian_thuc = "\n".join(bang_que.splitlines()[:2])
    muc_tu_dien = tra_cuu_tu_dien(cau_hoi)
    huong_dan_bo_sung = f"[CHƯƠNG]: {muc_tu_dien['ten']} | [DỤNG THẦN]: {muc_tu_dien['dung_than']} | [KHẨU QUYẾT]: {muc_tu_dien['khau_quyet']}\nTrình bày mạch lạc 4 phần: 1. Định Dụng Thần & Thế Ứng; 2. Phân Tích Động Biến & Sinh Khắc; 3. Dự Đoán Cát Hung & Ứng Kỳ; 4. Lời Khuyên Hành Động."
    user_prompt = f"""Thời gian thực tế lúc gieo quẻ:
{thoi_gian_thuc}

Mong cầu của khách: "{cau_hoi}"\n{huong_dan_bo_sung}
Trạng thái tâm thức: {ket_qua_nao['trang_thai_m2']}

Dữ liệu Dịch lý từ Bán cầu M1:
{diem_nong}"""

    try:
        ds_model = [m.id for m in client.models.list().data if "whisper" not in m.id.lower() and "guard" not in m.id.lower() and "tts" not in m.id.lower()]
        uu_tien = [m for m in ds_model if any(k in m.lower() for k in ["70b", "qwen", "llama-4", "deepseek", "32b"])]
        MODELS = uu_tien + [m for m in ds_model if m not in uu_tien]
    except Exception:
        MODELS = ["llama-3.3-70b-versatile"]
    for model_id in MODELS:
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    dict(role="system", content=system_prompt),
                    dict(role="user", content=user_prompt)
                ],
                model=model_id,
                temperature=0.4,
                max_tokens=2048
            )
            noi_dung = next(iter(chat_completion.choices)).message.content or ""
            noi_dung = re.sub(r'<think>.*?</think>', '', noi_dung, flags=re.DOTALL).strip()
            if len(noi_dung) > 20:
                return header_nao + noi_dung
        except Exception as e:
            print('Loi Groq:', e)
            continue

    return header_nao + "⏳ Hệ thống đang hồi phục lượt hỏi, bạn hãy tĩnh tâm thử lại sau 15 giây nhé!"
