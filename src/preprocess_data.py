import emoji
import re
from underthesea import text_normalize, word_tokenize

def preprocess_comments(comments, rdrsegmenter, abbr, emoji_vi):
    if not comments:
        return

    for cmt in comments:
        cmt['cmt_content'] = preprocess_text(cmt['cmt_content'], rdrsegmenter, abbr, emoji_vi)
        preprocess_comments(cmt['comments'], rdrsegmenter,abbr, emoji_vi)

def replace_emoji_and_abbr(text, abbr, emoji_vi):
    pattern = r':[^:\s]+:|[\w]+|[^\w\s]'
    words = re.findall(pattern, text)

    for i, w in enumerate(words):
        if w in abbr:
            words[i] = abbr[w]
        elif len(w) > 2 and w.startswith(':') and w.endswith(':'):
            emoji_vi_name = emoji_vi.get(w, '')
            if emoji_vi_name:
                words[i] = f'[{emoji_vi_name}]'
            else:
                words[i] = ''

    return ' '.join(words)

def preprocess_text(text, rdrsegmenter, abbr, emoji_vi):
    text_with_name_emoji = emoji.demojize(text)

    text_after_replace = replace_emoji_and_abbr(text_with_name_emoji, abbr, emoji_vi)

    normalized_text = text_normalize(text_after_replace)

    segmented_text = ' '.join(rdrsegmenter.word_segment(normalized_text))

    return segmented_text
