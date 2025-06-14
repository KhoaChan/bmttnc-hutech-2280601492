import sys
from PIL import Image

# Hàm để giấu thông điệp vào ảnh
def encode_image(image_path, message):
    img = Image.open(image_path)          # Mở ảnh đầu vào
    width, height = img.size              # Lấy kích thước ảnh
    pixel_index = 0                       # Vị trí pixel hiện tại

    # Chuyển thông điệp sang dạng nhị phân (8 bit cho mỗi ký tự)
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Thêm chuỗi kết thúc (dấu hiệu dừng khi giải mã)

    data_index = 0  # Vị trí đang xử lý trong chuỗi nhị phân
    # Duyệt qua từng pixel trong ảnh
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))  # Lấy giá trị màu (R, G, B) của pixel

            # Gắn từng bit của thông điệp vào bit cuối của từng kênh màu
            for color_channel in range(3):
                if data_index < len(binary_message):
                    # Đổi bit cuối của kênh màu thành bit thông điệp tương ứng
                    pixel[color_channel] = int(
                        format(pixel[color_channel], '08b')[:-1] + binary_message[data_index],
                        2
                    )
                    data_index += 1
                else:
                    break  # Dừng nếu đã giấu hết dữ liệu

            img.putpixel((col, row), tuple(pixel))  # Cập nhật pixel đã chỉnh sửa vào ảnh

            if data_index >= len(binary_message):
                break  # Dừng nếu đã giấu hết dữ liệu
        if data_index >= len(binary_message):
            break

    encoded_image_path = 'encoded_image.png'  # Tên ảnh đầu ra
    img.save(encoded_image_path)              # Lưu ảnh đã mã hóa
    print("Steganography complete. Encoded image saved as", encoded_image_path)

# Hàm main dùng để chạy chương trình
def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return

    image_path = sys.argv[1]  # Đường dẫn tới ảnh đầu vào
    message = sys.argv[2]     # Thông điệp cần mã hóa
    encode_image(image_path, message)

if __name__ == "__main__":
    main()
