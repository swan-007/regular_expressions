import csv
import re

with open("1.csv", encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=",")
    contacts_list = list(rows)
    contacts_list_updated = []

def _name():
    name_pattern = r'([А-Я])'
    name_substitution = r' \1'
    for i in contacts_list[1:]:
        x = i[0] + i[1] + i[2]
        if len((re.sub(name_pattern, name_substitution, x).split())) == 3:
            i[0] = re.sub(name_pattern, name_substitution, x).split()[0]
            i[1] = re.sub(name_pattern, name_substitution, x).split()[1]
            i[2] = re.sub(name_pattern, name_substitution, x).split()[2]
        elif len((re.sub(name_pattern, name_substitution, x).split())) == 2:
             i[0] = re.sub(name_pattern, name_substitution, x).split()[0]
             i[1] = re.sub(name_pattern, name_substitution, x).split()[1]
             i[2] = ''
        elif len((re.sub(name_pattern, name_substitution, x).split())) == 1:
             i[0] = re.sub(name_pattern, name_substitution, x).split()[0]
             i[1] = ''
             i[2] = ''
    return

def _phone():
    phone_pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'
    for i in contacts_list:
        i[5] = phone_pattern.sub(phone_substitution, i[5])

def _duplicates_combining():
    for i in contacts_list[1:]:
        last_name = i[0]
        first_name = i[1]
        for contact in contacts_list[1:]:
            new_last_name = contact[0]
            new_first_name = contact[1]
            if last_name == new_last_name and first_name == new_first_name:
                for item in range(2, 7):
                    if contact[item] == '':
                        contact[item] = i[item]
    for contact in contacts_list:
        if contact not in contacts_list_updated:
            contacts_list_updated.append(contact)
    return contacts_list_updated


def final():
    _name()
    _phone()
    _duplicates_combining()
    with open("2.csv", "w", encoding='utf-8') as file_1:
        datawriter = csv.writer(file_1, delimiter=',')
        datawriter.writerows(contacts_list_updated)
    print("Готово")
