import socket
import ssl
import threading

# Thông tin server: localhost + cổng 12345
server_address = ('localhost', 12345)

# Danh sách các client đã kết nối (dùng để gửi broadcast)
clients = []

# Hàm xử lý một client
def handle_client(client_socket):
    clients.append(client_socket)  # Thêm client vào danh sách quản lý
    print("Đã kết nối với:", client_socket.getpeername())  # In ra địa chỉ client

    try:
        while True:
            data = client_socket.recv(1024)  # Nhận dữ liệu từ client
            if not data:
                break  # Nếu không nhận được dữ liệu thì thoát vòng lặp
            print("Nhận:", data.decode('utf-8'))

            # Gửi dữ liệu đến các client khác (broadcast)
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        clients.remove(client)  # Nếu lỗi thì xóa khỏi danh sách
    except:
        clients.remove(client_socket)  # Nếu lỗi trong xử lý client
    finally:
        print("Đã ngắt kết nối:", client_socket.getpeername())
        clients.remove(client_socket)  # Xóa client khỏi danh sách
        client_socket.close()  # Đóng kết nối

# Tạo socket TCP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)  # Gắn socket vào địa chỉ
server_socket.listen(5)  # Lắng nghe tối đa 5 kết nối đang chờ

print("Server đang chờ kết nối...")

# Lặp vô hạn để chấp nhận client mới
while True:
    client_socket, client_address = server_socket.accept()

    # Tạo SSL context để bảo mật kết nối
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)

    # Nạp chứng chỉ số và khóa bí mật của server
    context.load_cert_chain(certfile="./certificates/server-cert.crt",
                            keyfile="./certificates/server-key.key")

    # Gói socket TCP thành socket SSL, dùng cho server
    ssl_socket = context.wrap_socket(client_socket, server_side=True)

    # Tạo và khởi động một luồng mới để xử lý client vừa kết nối
    client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
    client_thread.start()
