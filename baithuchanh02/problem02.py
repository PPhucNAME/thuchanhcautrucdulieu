def find_common_elements(num_list1, num_list2):
    # Tạo một set từ num_list1 để tối ưu việc tìm kiếm
    set1 = set(num_list1)

    # Duyệt qua num_list2 và kiểm tra xem mỗi phần tử có trong set1 không
    common_elements = []
    for num in num_list2:
        if num in set1:
            common_elements.append(num)

    return common_elements

# Test chương trình
num_list1 = [1, 2, 3, 4, 5]
num_list2 = [3, 4, 5, 6, 7]
print("Các số chung:", find_common_elements(num_list1, num_list2))
