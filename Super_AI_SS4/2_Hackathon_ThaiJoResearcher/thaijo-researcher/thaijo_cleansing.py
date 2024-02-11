import pandas as pd
import regex as re


def remove_spaces(string):
    if string == '':
        return ''
    elif string == ' ':
        return ''
    if string[0] == ' ':
        string = string[1:]
    if string[-1] == ' ':
        string = string[:-1]
    return string

if __name__ == '__main__':
    char = {'id': [], 'name': []}
    df = pd.read_csv('test.csv')
    df = df.fillna('')
    for idx, row in df.iterrows():
        names = []
        char['id'].extend([f"{row['_id']}_{i+1}" for i in range(10)])
        author = row['_source.author']
        if author != '':
            names.append(author)
        co_author = row['_source.co-author']
        if co_author != '':
            ca = co_author.split(',')
            for c in ca:
                if c not in names:
                    names.append(c)
        if len(names) == 0:
            char['name'].extend([None]*10)
            continue
        names = [remove_spaces(name) for name in names]
        if len(names) > 10:
            names = names[:10]
        elif len(names) < 10:
            names.extend(['']*(10-len(names)))
        char['name'].extend(names)
    char = pd.DataFrame(char)
    char.to_csv('predict2.csv', index=False)
