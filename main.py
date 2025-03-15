import emoji

from src.preprocess_data import preprocess_text, preprocess_comments
from src.utils import load_data, save_json
from underthesea import text_normalize

if __name__ == '__main__':
    abbr = load_data('./alt_text/abbreviation.json')
    emoji_vi = load_data('./alt_text/emoji_vi.json')
    # path = 'data.json'
    # data = load_data(path)
    #
    # for post in data:
    #     post['post_content'] = preprocess_text(post['post_content'], abbr, emoji_vi)
    #     preprocess_comments(post['comments'], abbr, emoji_vi)
    #
    # save_json(data, 'preprocessed_data.json')
    #
    # print('Done !')
    text = ' 24251250Em là sinh viên năm nhất, mặc dù còn lâu nữa em mới đi quân sự nhưng mà em muốn hỏi một chút ạ. Nước quân sự thì em nghe bảo là nó bẩn, vì thế em tính mang đầu lọc nước đi để dùng. Nhưng vấn đề là em không biết mình có nhiều thời gian tắm rửa và vệ sinh cá nhân không ạ, vì em khá hậu đậu nên lắp đầu lọc vào khi nào cũng tốn gần 10 phút. Thêm nữa em còn nghe bảo khu quân sự sẽ là nhà vệ sinh chung cho cả khoá chứ không phải riêng ở từng phòng, vì vậy nghĩa là lần nào em đi rửa mặt và tắm rửa em đều phải lắp lại đầu lọc. Nên em muốn hỏi một chút về thời gian vệ sinh cá nhân được phép.Ngoài ra, nếu các chị khoá trên có bí quyết gì cho việc da không bị nổi tùm lum khi dùng nước ở quân sự thì chỉ cho em với ạ. Em cảm ơn nhiều ạ.—✨—'
    print(preprocess_text(text, abbr, emoji_vi))