from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# Hàm sinh cặp khóa (riêng + công khai) phía client dựa trên tham số Diffie-Hellman
def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()  # Tạo khóa riêng
    public_key = private_key.public_key()           # Tạo khóa công khai tương ứng
    return private_key, public_key

# Hàm tính khóa bí mật dùng chung từ khóa riêng của client và khóa công khai của server
def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)  # Tính toán khóa chung (shared secret)
    return shared_key

def main():
    # Tải khóa công khai của server từ file PEM
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())  # Giải mã khóa PEM

    # Lấy các tham số Diffie-Hellman từ khóa công khai của server
    parameters = server_public_key.parameters()

    # Sinh cặp khóa của client từ cùng tham số với server
    private_key, public_key = generate_client_key_pair(parameters)

    # Tính khóa bí mật dùng chung giữa client và server
    shared_secret = derive_shared_secret(private_key, server_public_key)

    # Hiển thị khóa bí mật ở dạng hex (chỉ để debug)
    print("Shared Secret:", shared_secret.hex())

if __name__ == "__main__":
    main()  # Chạy hàm chính nếu script được thực thi trực tiếp
