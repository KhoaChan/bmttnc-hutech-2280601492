from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Hàm sinh tham số Diffie-Hellman (generator, prime)
def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048)  # Sinh tham số với generator=2 và độ dài 2048 bit
    return parameters

# Hàm sinh cặp khóa server từ các tham số Diffie-Hellman
def generate_server_key_pair(parameters):
    private_key = parameters.generate_private_key()  # Sinh khóa riêng
    public_key = private_key.public_key()           # Lấy khóa công khai từ khóa riêng
    return private_key, public_key

def main():
    # Sinh các tham số DH
    parameters = generate_dh_parameters()

    # Sinh cặp khóa server (riêng và công khai)
    private_key, public_key = generate_server_key_pair(parameters)

    # Lưu khóa công khai của server vào file dưới dạng PEM
    with open("server_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,                            # Định dạng PEM (chuỗi base64 có header/footer)
            format=serialization.PublicFormat.SubjectPublicKeyInfo         # Định dạng khóa công khai chuẩn
        ))

if __name__ == "__main__":
    main()  # Gọi hàm chính nếu chạy trực tiếp
