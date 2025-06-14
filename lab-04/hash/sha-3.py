# Nhập hàm băm SHA3-256 từ thư viện pycryptodome
from Crypto.Hash import SHA3_256

# Hàm băm dữ liệu đầu vào bằng thuật toán SHA3-256
def sha3(message):
    # Tạo một đối tượng SHA3-256 rỗng
    sha3_hash = SHA3_256.new()
    
    # Cập nhật đối tượng băm với dữ liệu đầu vào (phải là kiểu bytes)
    sha3_hash.update(message)
    
    # Trả về kết quả băm ở dạng bytes
    return sha3_hash.digest()

# Hàm main để nhập dữ liệu và hiển thị kết quả
def main():
    # Nhập chuỗi văn bản từ người dùng và mã hóa sang dạng bytes (UTF-8)
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    
    # In lại chuỗi đã nhập (sau khi decode về lại chuỗi để hiển thị rõ ràng)
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    
    # Tính và in kết quả băm SHA3-256 dưới dạng chuỗi hexa
    print("SHA-3 Hash:", sha3(text).hex())

# Gọi hàm main nếu đang chạy trực tiếp (không phải import từ module khác)
if __name__ == "__main__":
    main()
