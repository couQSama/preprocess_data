import emoji
import re
from underthesea import text_normalize, word_tokenize

def preprocess_comments(comments, abbr, emoji_vi):
    if not comments:
        return

    for cmt in comments:
        cmt['cmt_content'] = preprocess_text(cmt['cmt_content'], abbr, emoji_vi)
        preprocess_comments(cmt['comments'], abbr, emoji_vi)

def replace_abbr_and_emoji(text, abbr, emoji_vi):
    text_with_emoji_name = emoji.demojize(text)

    pattern = r':[^:]+:|[\w]+|[^\w\s]'
    words = re.findall(pattern, text_with_emoji_name)

    for i, word in enumerate(words):
        if word in abbr:
            words[i] = abbr[word]
        elif word in emoji_vi:
            words[i] = f'[{emoji_vi[word]}]'
    return ' '.join(words)

def preprocess_text(text, abbr, emoji_vi):
    text_with_emoji_name = emoji.demojize(text)
    nor_text = text_normalize(text_with_emoji_name)

    print('after nor')
    print(nor_text)
    print()

    pattern = r': [^:]+ :|[\w]+|[^\w\s]'
    words = re.findall(pattern, nor_text)
    print('after split')
    print(words)
    print()

    for i, word in enumerate(words):
        if word in abbr:
            words[i] = abbr[word]

    text_after_segment = word_tokenize(' '.join(words), format='text')
    print('after tokenize')
    print(text_after_segment)
    print()

    pattern = r': [^:]+ :|[\w]+|[^\w\s]'
    words = re.findall(pattern, text_after_segment)
    print('after split')
    print(words)
    print()

    for i, word in enumerate(words):
        if word.startswith(':') and word.endswith(':'):
            word = re.sub(r'\s+', '', word)
            emoji_vi_name = word_tokenize(emoji_vi[word], format='text')
            words[i] = f'[ {emoji_vi_name} ]'

    print('after replay emoji')
    print(' '.join(words))
    print()

    return ' '.join(words)