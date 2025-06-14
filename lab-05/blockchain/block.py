# Nhập thư viện hashlib để sử dụng hàm băm SHA-256
import hashlib

# Định nghĩa lớp Block đại diện cho một khối trong blockchain
class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, proof):
        self.index = index                        # Chỉ số (số thứ tự) của khối
        self.previous_hash = previous_hash        # Hash của khối trước đó (liên kết chuỗi)
        self.timestamp = timestamp                # Dấu thời gian tạo khối
        self.transactions = transactions          # Danh sách giao dịch trong khối
        self.proof = proof                        # Bằng chứng công việc (proof-of-work)
        self.hash = self.calculate_hash()         # Hash hiện tại của khối (được tính khi tạo)

    # Hàm tính toán mã băm SHA-256 cho khối hiện tại
    def calculate_hash(self):
        # Tạo chuỗi đại diện toàn bộ nội dung khối
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.proof}"
        
        # Mã hóa chuỗi và băm bằng SHA-256, sau đó trả về dạng hexdigest (chuỗi hex)
        return hashlib.sha256(block_string.encode()).hexdigest()
