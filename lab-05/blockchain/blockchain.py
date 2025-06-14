from block import Block  # Import lớp Block từ file block.py
import hashlib           # Dùng để băm SHA-256
import time              # Lấy thời gian tạo block

# Lớp Blockchain đại diện cho một chuỗi khối
class Blockchain:
    def __init__(self):
        self.chain = []  # Danh sách các khối trong chuỗi
        self.current_transactions = []  # Danh sách các giao dịch đang chờ xác nhận

        # Tạo block đầu tiên (genesis block)
        self.create_block(proof=1, previous_hash='0')

    # Tạo một block mới và thêm vào chuỗi
    def create_block(self, proof, previous_hash):
        block = Block(
            index=len(self.chain) + 1,                # Chỉ số của block
            previous_hash=previous_hash,              # Hash của block trước
            timestamp=time.time(),                    # Thời gian tạo block
            transactions=self.current_transactions,   # Giao dịch hiện tại
            proof=proof                               # Bằng chứng proof-of-work
        )
        self.current_transactions = []  # Reset danh sách giao dịch sau khi block được tạo
        self.chain.append(block)        # Thêm block vào chuỗi
        return block

    # Lấy block gần nhất (cuối cùng) trong chuỗi
    def get_previous_block(self):
        return self.chain[-1]

    # Thuật toán Proof of Work (PoW)
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        # Tìm giá trị new_proof sao cho hàm băm bắt đầu bằng 4 số 0
        while not check_proof:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()
            ).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    # Thêm giao dịch mới vào danh sách chờ
    def add_transaction(self, sender, receiver, amount):
        self.current_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        # Trả về chỉ số của block kế tiếp mà giao dịch này sẽ được ghi vào
        return self.get_previous_block().index + 1

    # Xác minh tính hợp lệ của toàn bộ chuỗi khối
    def is_chain_valid(self, chain):
        previous_block = chain[0]  # Block đầu tiên
        block_index = 1

        # Duyệt từng block trong chuỗi để kiểm tra tính hợp lệ
        while block_index < len(chain):
            block = chain[block_index]

            # Kiểm tra xem block hiện tại có trỏ đúng tới hash của block trước không
            if block.previous_hash != previous_block.hash:
                return False

            # Kiểm tra điều kiện proof of work
            previous_proof = previous_block.proof
            proof = block.proof
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()
            ).hexdigest()

            if hash_operation[:4] != '0000':
                return False

            # Chuyển sang block tiếp theo
            previous_block = block
            block_index += 1

        return True  # Nếu không có sai sót, chuỗi là hợp lệ
