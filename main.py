import py_vncorenlp

from src.preprocess_data import preprocess_text, preprocess_comments
from src.utils import load_data, save_json

if __name__ == '__main__':
    abbr = load_data('./alt_text/abbreviation.json')
    emoji_vi = load_data('./alt_text/emoji_vi.json')
    rdrsegmenter = py_vncorenlp.VnCoreNLP(annotators=["wseg"], save_dir='E:\Work\AI\Project\preprocess_data\.venv\Lib\site-packages\py_vncorenlp')

    path = 'E:\Work\AI\Project\preprocess_data\data.json'
    data = load_data(path)

    for post in data:
        post['post_content'] = preprocess_text(post['post_content'], rdrsegmenter, abbr, emoji_vi)
        preprocess_comments(post['comments'], rdrsegmenter, abbr, emoji_vi)

    save_json(data, 'E:\Work\AI\Project\preprocess_data\preprocessed_data.json')

    print('Done !')