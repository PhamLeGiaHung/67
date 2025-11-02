from guizero import App, TextBox, PushButton, Box

# Tạo ứng dụng (cửa sổ chính)
ung_dung = App(title="Máy tính Casio", width=300, height=350)

# Ô hiển thị phép tính và kết quả
o_hien_thi = TextBox(ung_dung, text="", width=24)
o_hien_thi.text_size = 16  # Cỡ chữ to cho dễ nhìn

# Hàm xử lý khi người dùng bấm nút
def bam_phim(phim):
    if phim == "=":
        tinh_toan()  # Gọi hàm tính kết quả
    elif phim == "C":
        o_hien_thi.value = ""  # Xóa hết nội dung trong ô
    else:
        # Dấu ":" sẽ được hiểu là phép chia "/"
        o_hien_thi.value += "/" if phim == ":" else phim

# Hàm tính kết quả của phép tính
def tinh_toan():
    try:
        ket_qua = eval(o_hien_thi.value)
        # Nếu kết quả là số thập phân .0 thì đổi sang số nguyên
        if isinstance(ket_qua, float) and ket_qua.is_integer():
            ket_qua = int(ket_qua)
        o_hien_thi.value = str(ket_qua)
    except:
        o_hien_thi.value = "Lỗi!"  # Báo lỗi nếu nhập sai cú pháp

# Khung chứa các nút bấm (dạng lưới)
khung_nut = Box(ung_dung, layout="grid")

# Danh sách các nút bấm
cac_nut = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", ".", ":", "="],
    ["C"]  # Nút xóa
]

# Tạo các nút bấm trên giao diện
for hang, dong in enumerate(cac_nut):
    for cot, chu in enumerate(dong):
        PushButton(
            khung_nut,
            text=chu,         # Chữ hiển thị trên nút
            width=6,
            height=2,
            grid=[cot, hang], # Vị trí nút trên lưới
            command=bam_phim, # Khi bấm thì gọi hàm bam_phim
            args=[chu]        # Truyền ký tự của nút vào hàm
        )

# Hiển thị ứng dụng
ung_dung.display()
