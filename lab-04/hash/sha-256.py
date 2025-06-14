# Nhập thư viện hashlib để sử dụng các thuật toán băm như SHA-256
import hashlib

# Hàm tính giá trị hash bằng thuật toán SHA-256
def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()             # Tạo một đối tượng hash SHA-256 rỗng
    sha256_hash.update(data.encode('utf-8'))   # Cập nhật dữ liệu cần hash (phải chuyển về bytes)
    return sha256_hash.hexdigest()             # Trả về giá trị băm ở dạng chuỗi hex (thập lục phân)

# Nhận dữ liệu đầu vào từ người dùng
data_to_hash = input("Nhập dữ liệu để hash bằng SHA-256: ")  # Nhập chuỗi văn bản từ bàn phím

# Gọi hàm để tính giá trị hash
hash_value = calculate_sha256_hash(data_to_hash)

# In kết quả ra màn hình
print("GIÁ TRỊ HASH SHA-256:", hash_value)  # Xuất kết quả hash ở dạng hex
