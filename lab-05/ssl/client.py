import socket
import ssl
import threading

# Thiết lập địa chỉ server (localhost và cổng 12345)
server_address = ('localhost', 12345)

# Hàm nhận dữ liệu từ server, chạy ở luồng riêng
def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)  # Nhận dữ liệu (tối đa 1024 byte)
            if not data:
                break  # Nếu không nhận được gì thì thoát vòng lặp
            print("Nhận:", data.decode('utf-8'))  # Hiển thị dữ liệu nhận được
    except:
        pass  # Bỏ qua lỗi nếu có
    finally:
        ssl_socket.close()
        print("Kết nối đã đóng.")

# Tạo socket TCP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tạo SSL context (đối tượng để quản lý kết nối bảo mật)
context = ssl.SSLContext(ssl.PROTOCOL_TLS)  # Dùng giao thức TLS
context.verify_mode = ssl.CERT_NONE         # Không xác minh chứng chỉ (KHÔNG an toàn khi dùng thật)
context.check_hostname = False              # Không kiểm tra tên host

# Gói socket thông thường thành một socket SSL
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

# Kết nối tới server đã định nghĩa
ssl_socket.connect(server_address)

# Tạo và chạy một luồng riêng để nhận dữ liệu liên tục từ server
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

# Vòng lặp chính: người dùng nhập tin nhắn và gửi đi
try:
    while True:
        message = input("Nhập tin nhắn: ")  # Nhập từ bàn phím
        ssl_socket.send(message.encode('utf-8'))  # Gửi tin nhắn đi qua kết nối SSL
except KeyboardInterrupt:
    pass  # Nhấn Ctrl+C để thoát
finally:
    ssl_socket.close()  # Đóng kết nối khi thoát chương trình
