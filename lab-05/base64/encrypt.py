# Nhập thư viện base64 để sử dụng các hàm mã hóa/giải mã Base64
import base64

def main():
    # Nhận chuỗi cần mã hóa từ người dùng
    input_string = input("Nhap thong tin can ma hoa: ")

    # Mã hóa chuỗi đầu vào sang bytes, sau đó mã hóa Base64
    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))  # Chuyển chuỗi sang bytes rồi mã hóa base64

    # Chuyển kết quả mã hóa từ bytes về chuỗi (để ghi ra file)
    encoded_string = encoded_bytes.decode("utf-8")

    # Ghi chuỗi đã mã hóa vào file "data.txt"
    with open("data.txt", "w") as file:
        file.write(encoded_string)

    # Thông báo hoàn tất
    print("Đã mã hóa và ghi vào tệp data.txt")

# Hàm main sẽ chạy khi chương trình được thực thi trực tiếp
if __name__ == "__main__":
    main()
