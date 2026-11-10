def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    clean_text = ''
    inside_tag = False

    for symbol in html:
        if symbol == '<':
            inside_tag = True
        elif symbol == '>':
            inside_tag = False
        elif not inside_tag:
            clean_text += symbol

    lines = clean_text.splitlines()

    clean_text = '\n'.join(line for line in lines if line.strip())

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(clean_text)


delete_html_tags('draft.html')