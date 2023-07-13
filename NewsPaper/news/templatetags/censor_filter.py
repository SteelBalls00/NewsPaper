from django import template


register = template.Library()


@register.filter()
def censor(content, censor_list):
    censor_list = ['редиска', 'Редиска', 'сортировки', 'богатые', 'метод'] # Пример списка запрещенных слов который
    lower_censor_list = [words.lower() for words in censor_list] # мы приводим в нижний регистр дабы исключить
    split_content = content.split()                              # заглавные буквы.

    for i in range(len(split_content)):                                # Каждое слово из текста также приводится
        if split_content[i].lower() in lower_censor_list:              # в строчный вид и сравнивается с 1-м списком.
            first_letter = split_content[i][0]
            other_letter = split_content[i][1:]
            replaced_word = first_letter + '*' * len(other_letter)     # Ну тут понятно, собираем слово после цензуры
            split_content[i] = replaced_word                           # и собираем обратно в текст контента.
    return ' '.join(split_content)