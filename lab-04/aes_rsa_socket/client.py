from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading

# Tạo socket TCP cho client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # Kết nối đến server tại localhost và cổng 12345

# Sinh cặp khóa RSA cho client
client_key = RSA.generate(2048)

# Nhận khóa công khai từ server
server_public_key = RSA.import_key(client_socket.recv(2048))

# Gửi khóa công khai của client đến server
client_socket.send(client_key.public_key().export_key(format='PEM'))

# Nhận khóa AES đã được mã hóa bằng khóa công khai của client
encrypted_aes_key = client_socket.recv(2048)

# Giải mã khóa AES bằng khóa riêng RSA của client
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

# Hàm mã hóa tin nhắn sử dụng AES
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)  # Tạo đối tượng mã hóa AES ở chế độ CBC
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))  # Mã hóa sau khi pad
    return cipher.iv + ciphertext  # Trả về IV + ciphertext

# Hàm giải mã tin nhắn sử dụng AES
def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]  # Tách IV từ đầu tin nhắn
    ciphertext = encrypted_message[AES.block_size:]  # Phần còn lại là ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Tạo đối tượng AES với IV
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)  # Giải mã và bỏ pad
    return decrypted_message.decode()  # Trả về chuỗi văn bản gốc

# Luồng riêng để nhận tin nhắn từ server
def receive_message():
    while True:
        try:
            encrypted_message = client_socket.recv(1024)  # Nhận dữ liệu từ server
            if not encrypted_message:
                break
            decrypted_message = decrypt_message(aes_key, encrypted_message)  # Giải mã tin nhắn
            print(f"Received:", decrypted_message)  # In tin nhắn đã giải mã
        except:
            break

# Bắt đầu luồng nhận tin nhắn
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

# Vòng lặp chính để gửi tin nhắn
while True:
    message = input("Enter message ('exit' to quit): ")  # Nhập tin nhắn từ bàn phím
    encrypted_message = encrypt_message(aes_key, message)  # Mã hóa tin nhắn
    client_socket.send(encrypted_message)  # Gửi đến server

    if message == "exit":  # Nếu nhập 'exit' thì thoát
        break

# Đóng kết nối socket
client_socket.close()
