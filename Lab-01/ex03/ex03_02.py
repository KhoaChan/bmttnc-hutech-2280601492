def dao_nguoc_list(lst):
    return lst[::-1]

input_list = input("Nhap ds cac so, cach nhau bang dau phay: ")
number = list(map(int, input_list.split(',')))

list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi dao nguoc la: ", list_dao_nguoc)