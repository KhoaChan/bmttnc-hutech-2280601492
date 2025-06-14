from blockchain import Blockchain  # Nhập lớp Blockchain từ file blockchain.py

# Khởi tạo blockchain
my_blockchain = Blockchain()

# Thêm một số giao dịch vào danh sách chờ xử lý (sẽ được ghi vào block kế tiếp)
my_blockchain.add_transaction('Alice', 'Bob', 10)
my_blockchain.add_transaction('Bob', 'Charlie', 5)
my_blockchain.add_transaction('Charlie', 'Alice', 3)

# Tiến hành "khai thác" (mine) một block mới
previous_block = my_blockchain.get_previous_block()      # Lấy block gần nhất
previous_proof = previous_block.proof                    # Lấy proof của block trước
new_proof = my_blockchain.proof_of_work(previous_proof)  # Tìm proof mới
previous_hash = previous_block.hash                      # Lấy hash của block trước

# Thêm phần thưởng cho "người khai thác"
my_blockchain.add_transaction('Genesis', 'Miner1', 1)

# Tạo block mới với proof và previous_hash tìm được
new_block = my_blockchain.create_block(new_proof, previous_hash)

# In ra thông tin toàn bộ các block trong chuỗi blockchain
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)             # Thời gian tạo block
    print("Transactions:", block.transactions)       # Danh sách giao dịch
    print("Proof:", block.proof)                     # Proof-of-work
    print("Previous Hash:", block.previous_hash)     # Hash của block trước
    print("Hash:", block.hash)                       # Hash hiện tại của block
    print("-" * 50)

# Kiểm tra tính hợp lệ của toàn bộ chuỗi blockchain
print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
