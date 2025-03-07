# Ваше завдання написати функцію, яка прочитає заданий файл, очистить текст
# від html-тегів і запише цей текст в інший файл. html-тег завжди починається
# з "<" і закінчується на ">" тобто. потрібно видалити ці символи та все, що
# між ними. Функція отримує на вхід два параметри – ім'я файлу, який потрібно
# очистити, та ім'я файлу, куди потрібно записати очищений текст. Ім'я файлу,
# куди потрібно писати, можна задати за замовчуванням.
# Приклади файлів у вкладенні – файл який потрібно очистити (draft.html) та
# приклад файлу, який може вийти на виході з очищеним текстом (cleaned.txt).
# Файл draft.html необхідно завантажити та покласти поряд з файлом, де буде
# вирішення цієї домашки.
#
# Додаткове завдання для тих, хто захоче ускладнити рішення - спробуйте
# прибрати рядки, в яких немає інформації.


def index_tags(line: str) -> list:
    """The function searches for the start and end indices of paired html-tags

    :param line: line of the html-file
    :return: list of tuples with the start and end indices of the html-tags
    """
    start, end = '<', '>'
    idx_start = []
    idx_end = []
    for idx in range(len(line)):
        if line[idx] == start:
            idx_start.append(idx)
        elif line[idx] == end:
            idx_end.append(idx)
    return list(zip(idx_start, idx_end))


def index_tag(line: str) -> list:
    """The function searches for the start and end index of a single html-tag

    :param line: line of the html-file
    :return: list whose elements are the start and end indices of the html-tag
    """
    start, end = '<', '>'
    idx_tag = []
    for idx in range(len(line)):
        if line[idx] == start:
            idx_tag.append(idx)
        elif line[idx] == end:
            idx_tag.append(idx)
    return idx_tag


def clean_line_tags(line: str, idx_tags):
    """The function cleans a string of even html-tags

    :param line: line of the html-file
    :param idx_tags: list of tuples with starting and ending html-tag indices
    :return: string without html-tags
    """
    result = []
    last_end = 0
    for start, end in idx_tags:
        result.append(line[last_end: start])
        last_end = end + 1
    return ''.join(result)


def clean_line_tag(line: str, idx_tag):
    """The function cleans a string from a single html-tag

    :param line: line of the html-file
    :param idx_tag: list whose elements are the starting and ending indices of the html-tag
    :return: string without the html-tag
    """
    start, end = idx_tag
    return line[:start] + line[end + 1:]


def clean_html_tags(path_file: str, new_file = 'cleaned_html.txt'):
    """The function reads html-file, cleans the text from html-tags,
    and writes this text to another file

    :param path_file: filename or path to the html-file to be cleaned
    :param new_file: the name of the file where the cleaned text should be written
    :return: text file
    """
    with open(path_file, 'r', encoding= 'utf-8-sig') as file:
        data = file.readlines()

    update_data = []

    for line in data:
        if all([line.count('<') == 1, line.count('>') == 1]):
            result = clean_line_tag(line, index_tag(line))
            update_data.append(result.split())
        elif all([line.count('<') == 1, line.count('>') == 0]):
            idx = index_tag(line)
            result = line[:idx[0]]
            update_data.append(result.split())
        elif all([line.count('<') == 0, line.count('>') == 1]):
            idx = index_tag(line)
            result = line[idx[0] + 1:]
            update_data.append(result.split())
        elif line.count('>') % 2 == 0:
            line = clean_line_tags(line, index_tags(line))
            if '>' in line:
                idx = index_tag(line)
                result = line[idx[0] + 1:]
                update_data.append(result.split())
            else:
                result = line
                update_data.append(result.split())
        else:
            result = ''
            update_data.append(result.split())

    update_data = list(filter(lambda x: x != [], update_data))
    update_data = list(map(lambda x: " ".join(x) + '\n', update_data))
    update_data = ''.join(update_data)

    print(update_data)

    with open(new_file, 'w', encoding= 'utf-8-sig') as file1:
        file1.write(update_data)


clean_html_tags('draft.html')
