from time_calc import Time_calc
from link_and_name_ import Link_and_name_
from file_writer import File_writer
from info_parser import Info_parser



limit = input('Поиск (за последний месяц — ввести "M"(англ.), или кол-во дней): \n')

time_calc_ = Time_calc(limit)
_link_and_name_ = Link_and_name_()
info_parser_ = Info_parser()
links_and_names = list()

str_link = 'link'
str_amount_of_chapters = 'amount_of_chapters'


end = False
number = 1
amount_of_pages = info_parser_.Find_last_page()
p_index = 0  # = 1
a_index = 0  # = 0
p_index, a_index = info_parser_.Find_indexes(p_index, a_index)

for page_number in range(1, amount_of_pages):
    bS = info_parser_.BS_html_from_page_number(page_number)
    story_items = bS.select('.span8 .story-item')

    for story_item in story_items:
        p = story_item.findAll('p')
        meta_info = p[p_index]    # = 1
        limit_is_exceeded = time_calc_.Limit_is_exceeded(meta_info)
        if (limit_is_exceeded):
            end = True
            break
        a = meta_info.findAll('a')  # <class 'bs4.element.Tag'>
        link_with_name = a[a_index]    # = 0
        link_and_name = _link_and_name_.Create_self(link_with_name, number)
        already_is = _link_and_name_.Check_list_of_self(links_and_names, link_and_name)
        if(already_is == False):
            number += 1

        #chapter_link_and_name = story_item.find('h3')
    if(end):
        break


_link_and_name_.Make_readables(links_and_names)

output_form = input("Форма вывода (C (англ.) — консоль, F — в файл): ")
print()

if (output_form == 'F'):
    file_writer_ = File_writer()
    file_writer_.Write(links_and_names)

if (output_form == 'C'):
    _link_and_name_.Print_selfs(links_and_names)
    input()
