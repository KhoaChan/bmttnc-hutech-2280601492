def dem_so_lan_xuat_hien(lst):
    count_fict = {}
    for item in lst:
        if item in count_fict:
            count_fict[item] += 1
        else:
            count_fict[item] = 1
    return count_fict
input_string = input("Nhap ds cac ptu, cach nhau bang dau phay: ")
word_list = input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("So lan xuat hien cua cac ptu:", so_lan_xuat_hien)