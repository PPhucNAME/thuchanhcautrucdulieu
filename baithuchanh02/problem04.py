import os

def count_words_in_file(file_name):
   # Lấy đường dẫn tuyệt đối của thư mục hiện tại
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Tạo đường dẫn tuyệt đối đến tệp với tên file_name
    file_path = os.path.join(current_directory, file_name)
    word_count = {}

    # Mở file và đọc các dòng
    with open(file_path, 'r') as file:
        # Duyệt qua từng dòng trong file
        for line in file:
            # Tách các từ trong dòng và chuyển đổi chúng thành chữ cái viết thường
            words = line.strip().lower().split()

            # Duyệt qua từng từ trong danh sách các từ
            for word in words:
                # Tăng giá trị của từ trong từ điển hoặc thêm từ vào từ điển nếu chưa có
                word_count[word] = word_count.get(word, 0) + 1

    return word_count

# Sử dụng hàm để đếm số từ trong file và in kết quả
file_path = "sample.txt"  # Thay đường dẫn tệp văn bản của bạn ở đây
word_counts = count_words_in_file(file_path)
print("Dictionary đếm số lần xuất hiện của các từ trong file:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
