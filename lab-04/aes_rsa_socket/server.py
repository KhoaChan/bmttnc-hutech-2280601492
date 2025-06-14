from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

# Tạo socket TCP cho server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))     # Gắn socket vào địa chỉ localhost và cổng 12345
server_socket.listen(5)                      # Lắng nghe tối đa 5 kết nối đang chờ

# Sinh cặp khóa RSA cho server
server_key = RSA.generate(2048)

# Danh sách lưu trữ các client đã kết nối (kèm theo khóa AES tương ứng)
clients = []

# Hàm mã hóa tin nhắn bằng AES
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)                             # Tạo đối tượng mã hóa AES ở chế độ CBC
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))  # Mã hóa sau khi pad dữ liệu
    return cipher.iv + ciphertext                                   # Ghép IV và ciphertext để gửi đi

# Hàm giải mã tin nhắn bằng AES
def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]                         # Lấy IV từ đầu gói tin
    ciphertext = encrypted_message[AES.block_size:]                # Lấy phần còn lại là ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)                        # Tạo đối tượng AES với IV
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)  # Giải mã và bỏ padding
    return decrypted_message.decode()                              # Trả về chuỗi đã giải mã

# Hàm xử lý mỗi client kết nối
def handle_client(client_socket, client_address):
    print(f"Connected with {client_address}")  # Thông báo kết nối mới

    # Gửi khóa công khai RSA của server cho client
    client_socket.send(server_key.publickey().export_key(format='PEM'))

    # Nhận khóa công khai RSA từ client
    client_received_key = RSA.import_key(client_socket.recv(2048))

    # Sinh khóa AES ngẫu nhiên (16 byte)
    aes_key = get_random_bytes(16)

    # Mã hóa khóa AES bằng khóa công khai RSA của client
    cipher_rsa = PKCS1_OAEP.new(client_received_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(encrypted_aes_key)  # Gửi khóa AES đã mã hóa cho client

    # Lưu client cùng với khóa AES dùng để giao tiếp
    clients.append((client_socket, aes_key))

    # Bắt đầu nhận và xử lý tin nhắn từ client
    while True:
        encrypted_message = client_socket.recv(1024)  # Nhận tin nhắn đã mã hóa từ client
        decrypted_message = decrypt_message(aes_key, encrypted_message)  # Giải mã tin nhắn
        print(f"Received from {client_address}: {decrypted_message}")    # In nội dung ra màn hình

        # Gửi tin nhắn này tới tất cả các client khác (broadcast)
        for client, key in clients:
            if client != client_socket:  # Không gửi lại cho chính client đã gửi
                encrypted = encrypt_message(key, decrypted_message)  # Mã hóa lại bằng khóa của từng client
                client.send(encrypted)  # Gửi đến client

        # Nếu client gửi 'exit', thì thoát vòng lặp và đóng kết nối
        if decrypted_message == "exit":
            break

    # Xóa client khỏi danh sách, đóng socket
    clients.remove((client_socket, aes_key))
    client_socket.close()
    print(f"Connection with {client_address} closed")  # Thông báo kết thúc kết nối

# Vòng lặp chính: chấp nhận các kết nối client mới
while True:
    client_socket, client_address = server_socket.accept()  # Chấp nhận client mới
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))  # Tạo luồng xử lý riêng cho client
    client_thread.start()  # Bắt đầu luồng
