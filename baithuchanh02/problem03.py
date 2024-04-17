def count_letters(word):
    # Khởi tạo một dictionary để lưu trữ số lần xuất hiện của mỗi chữ cái
    letter_count = {}

    # Chuyển đổi tất cả các chữ cái trong từ thành chữ cái viết thường để loại bỏ sự phân biệt
    word = word.lower()

    # Duyệt qua từng ký tự trong từ
    for char in word:
        # Kiểm tra nếu ký tự là một chữ cái
        if char.isalpha():
            # Tăng giá trị của chữ cái trong từ điển hoặc thêm chữ cái vào từ điển nếu chưa có
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count

# Test chương trình
word = "Hello, Helli!"
print("Dictionary đếm số lần xuất hiện của các chữ cái trong từ:", count_letters(word))
