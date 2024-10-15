def BMI(height, weight): return weight / (height ** 2)

def PhanLoaiVaNguyCo(bmi):
    if bmi < 18.5: return "Gầy", "Thấp"
    elif bmi <= 24.9: return "Bình thường", "Trung Bình"
    elif bmi <= 29.9: return "Hơi Béo", "Cao"
    elif bmi <= 34.9: return "Béo Phì Cấp Độ 1", "Cao"
    elif bmi <= 39.9: return "Béo Phì Cấp Độ 2", "Rất cao"
    else: return "Béo Phì Cấp độ 3", "Nguy Hiểm"

height = float(input("Nhập vào chiều cao: "))
weight = float(input("Nhập vào cân nặng: "))
bmi = BMI(height, weight)
phanloai, nguycobenh = PhanLoaiVaNguyCo(bmi)
print(f"BMI của bạn: {bmi}\nPhân loại bạn: {phanloai}\nNguy cơ bệnh của Thím: {nguycobenh}")
