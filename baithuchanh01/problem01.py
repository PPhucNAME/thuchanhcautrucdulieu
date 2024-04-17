def max_in_sliding_window(num_list, k):
    if k <= 0:
        return "Kích thước của cửa sổ phải lớn hơn hoặc bằng 1"
    
    n = len(num_list)
    if n < k:
        return "Kích thước của cửa sổ lớn hơn số lượng phần tử trong danh sách"

    result = []
    window = []

    # Tạo sliding window ban đầu
    for i in range(k):
        while window and num_list[i] >= num_list[window[-1]]:
            window.pop()
        window.append(i)

    # Duyệt qua các phần tử còn lại trong danh sách
    for i in range(k, n):
        # Lấy giá trị lớn nhất trong sliding window hiện tại
        result.append(num_list[window[0]])

        # Loại bỏ các phần tử không còn nằm trong sliding window
        while window and window[0] <= i - k:
            window.pop(0)

        # Loại bỏ các phần tử nhỏ hơn phần tử hiện tại khỏi sliding window
        while window and num_list[i] >= num_list[window[-1]]:
            window.pop()

        window.append(i)

    # Thêm giá trị lớn nhất của sliding window cuối cùng
    result.append(num_list[window[0]])

    return result

# Test chương trình
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print("Số lớn nhất trong sliding window:", max_in_sliding_window(num_list, k))
