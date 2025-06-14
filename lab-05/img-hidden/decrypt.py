import sys
from PIL import Image

# Hàm dùng để giải mã thông điệp từ ảnh đã được mã hóa
def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)  # Mở ảnh đầu vào
    width, height = img.size              # Lấy kích thước ảnh
    binary_message = ""                   # Chuỗi nhị phân chứa thông điệp ẩn

    # Duyệt từng pixel trong ảnh
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))  # Lấy giá trị pixel tại (col, row)

            # Duyệt từng kênh màu (R, G, B)
            for color_channel in range(3):
                # Lấy bit cuối cùng của mỗi kênh và nối vào chuỗi nhị phân
                binary_message += format(pixel[color_channel], '08b')[-1]

    message = ""  # Chuỗi thông điệp sau khi giải mã
    # Chuyển đổi mỗi 8 bit thành một ký tự ASCII
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))  # Chuyển từ nhị phân sang ký tự
        if char == '\x0e':  # Nếu gặp ký tự kết thúc (11111110)
            break
        message += char

    return message  # Trả về thông điệp đã giải mã

# Hàm main thực thi chương trình
def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]  # Đường dẫn ảnh từ tham số dòng lệnh
    decoded_message = decode_image(encoded_image_path)  # Giải mã ảnh
    print("Decoded message:", decoded_message)  # In ra thông điệp

if __name__ == "__main__":
    main()
