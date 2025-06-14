import hashlib

# Hàm tính giá trị băm (hash) sử dụng thuật toán BLAKE2b
def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)  # Khởi tạo đối tượng BLAKE2b với độ dài kết quả 64 byte
    blake2_hash.update(message)                    # Cập nhật nội dung cần băm
    return blake2_hash.digest()                    # Trả về kết quả băm dưới dạng bytes

def main():
    # Nhập chuỗi từ người dùng và chuyển thành bytes (UTF-8)
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    
    # In chuỗi vừa nhập lại (đã giải mã từ bytes về string)
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    
    # In ra chuỗi băm BLAKE2b dưới dạng hex (dễ đọc)
    print("BLAKE2 Hash:", blake2(text).hex())

if __name__ == "__main__":
    main()  # Chạy chương trình nếu thực thi trực tiếp
