# Nhập thư viện base64 để thực hiện mã hóa/giải mã base64
import base64

def main():
    try:
        # Mở file "data.txt" ở chế độ đọc văn bản
        with open("data.txt", "r") as file:
            encoded_string = file.read().strip()  # Đọc toàn bộ nội dung và loại bỏ khoảng trắng thừa ở đầu/cuối

        # Giải mã chuỗi từ định dạng Base64 sang bytes
        decoded_bytes = base64.b64decode(encoded_string)

        # Chuyển đổi bytes thành chuỗi văn bản (UTF-8)
        decoded_string = decoded_bytes.decode("utf-8")

        # In kết quả ra màn hình
        print("chuoi sau khi giai ma: ", decoded_string)
    
    except Exception as e:
        # Bắt lỗi nếu có vấn đề xảy ra (ví dụ: file không tồn tại, định dạng sai, lỗi giải mã...)
        print("Loi: ", e)

# Điểm bắt đầu chương trình
if __name__ == "__main__":
    main()
