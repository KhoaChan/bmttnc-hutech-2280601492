import hashlib  # Thư viện cung cấp các hàm băm như MD5, SHA1, SHA256, v.v.

# Hàm tính giá trị băm MD5 từ một chuỗi đầu vào
def calculate_md5(input_string):
    md5_hash = hashlib.md5()  # Tạo một đối tượng MD5 mới
    md5_hash.update(input_string.encode('utf-8'))  # Cập nhật dữ liệu cần băm (chuyển thành bytes)
    return md5_hash.hexdigest()  # Trả về giá trị băm ở dạng chuỗi hex (thập lục phân)

# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi cần băm: ")  # Nhận đầu vào là chuỗi từ bàn phím

# Gọi hàm tính băm và lưu kết quả
md5_hash = calculate_md5(input_string)  # Tính mã băm MD5 của chuỗi

# In ra kết quả
print("Mã băm MD5 của chuỗi '{}': {}".format(input_string, md5_hash))  
