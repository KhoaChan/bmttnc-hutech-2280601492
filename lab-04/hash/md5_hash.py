# Hàm xoay trái một số nguyên 32-bit
def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

# Hàm băm MD5 thủ công
def md5(message):
    # Khởi tạo các giá trị ban đầu (theo chuẩn MD5)
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Bước 1: Thêm bit '1' vào cuối chuỗi
    original_length = len(message)                     # Độ dài ban đầu (tính theo byte)
    message += b'\x80'                                 # Thêm bit 1 (10000000)

    # Bước 2: Thêm các bit 0 cho đến khi độ dài ≡ 56 (mod 64)
    while len(message) % 64 != 56:
        message += b'\x00'

    # Bước 3: Thêm độ dài ban đầu (tính bằng bit) vào cuối (8 byte, little endian)
    message += (original_length * 8).to_bytes(8, 'little')

    # Chia thông điệp thành các khối 512-bit (64 byte)
    for i in range(0, len(message), 64):
        block = message[i:i+64]

        # Chia khối thành 16 từ 32-bit (little endian)
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        # Lưu lại giá trị trước vòng lặp
        a0, b0, c0, d0 = a, b, c, d

        # 64 vòng lặp chính của thuật toán
        for j in range(64):
            if j < 16:
                f = (b & c) | (~b & d)