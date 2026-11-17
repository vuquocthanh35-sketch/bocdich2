CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
HANH = {
    "Tý": "Thủy", "Hợi": "Thủy", "Dần": "Mộc", "Mão": "Mộc",
    "Tỵ": "Hỏa", "Ngọ": "Hỏa", "Thân": "Kim", "Dậu": "Kim",
    "Thìn": "Thổ", "Tuất": "Thổ", "Sửu": "Thổ", "Mùi": "Thổ"
}
XUNG = {
    "Tý": "Ngọ", "Ngọ": "Tý", "Sửu": "Mùi", "Mùi": "Sửu",
    "Dần": "Thân", "Thân": "Dần", "Mão": "Dậu", "Dậu": "Mão",
    "Thìn": "Tuất", "Tuất": "Thìn", "Tỵ": "Hợi", "Hợi": "Tỵ"
}
TIEN_THAN = {("Hợi", "Tý"), ("Dần", "Mão"), ("Tỵ", "Ngọ"), ("Thân", "Dậu"), ("Sửu", "Thìn"), ("Thìn", "Mùi"), ("Mùi", "Tuất"), ("Tuất", "Sửu")}
THOAI_THAN = {(b, a) for (a, b) in TIEN_THAN}

QUAI_TEN = {1: "Càn", 2: "Đoài", 3: "Ly", 4: "Chấn", 5: "Tốn", 6: "Khảm", 7: "Cấn", 8: "Khôn"}
QUAI_HANH = {1: "Kim", 2: "Kim", 3: "Hỏa", 4: "Mộc", 5: "Mộc", 6: "Thủy", 7: "Thổ", 8: "Thổ"}
QUAI_BIN = {1: "111", 2: "110", 3: "101", 4: "100", 5: "011", 6: "010", 7: "001", 8: "000"}
BIN_QUAI = {v: k for k, v in QUAI_BIN.items()}

NOI_GIAP = {
    1: ["Tý", "Dần", "Thìn"], 2: ["Tỵ", "Mão", "Sửu"], 3: ["Mão", "Sửu", "Hợi"], 4: ["Tý", "Dần", "Thìn"],
    5: ["Sửu", "Hợi", "Dậu"], 6: ["Dần", "Thìn", "Ngọ"], 7: ["Thìn", "Ngọ", "Thân"], 8: ["Mùi", "Tỵ", "Mão"]
}
NGOAI_GIAP = {
    1: ["Ngọ", "Thân", "Tuất"], 2: ["Hợi", "Dậu", "Mùi"], 3: ["Dậu", "Mùi", "Tỵ"], 4: ["Ngọ", "Thân", "Tuất"],
    5: ["Mùi", "Tỵ", "Mão"], 6: ["Thân", "Tuất", "Tý"], 7: ["Tuất", "Tý", "Dần"], 8: ["Sửu", "Hợi", "Dậu"]
}
TIET_KHI_NGAY = [
    (2, 4, 2), (3, 6, 3), (4, 5, 4), (5, 6, 5), (6, 6, 6), (7, 7, 7),
    (8, 8, 8), (9, 8, 9), (10, 8, 10), (11, 7, 11), (12, 7, 0), (1, 6, 1)
]
