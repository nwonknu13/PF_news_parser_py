import json, requests, bs4, datetime

from link_and_name import Link_and_Name
from time_calc import Time_calc
from link_and_name_ import Link_and_name_
from file_writer import File_writer
from info_parser_ import Info_parser_




link_main = "https://ponyfiction.org"
link_pattern = link_main + "/stream/chapters/page/"

file_name = 'PF_news'

start_page = 1

limit = input('Поиск (за последний месяц — ввести "M"(англ.), или кол-во дней): \n')

now_ = datetime.datetime.now()
time_calc_ = Time_calc()
seconds_limit = time_calc_.Set_seconds_limit(limit, now_)

links_and_names = list()

str_link = 'link'
str_amount_of_chapters = 'amount_of_chapters'

Link_and_name_temp = Link_and_name_()

info_parser_ = Info_parser_()


p_index = 0  # = 1
p_index_founded = False

a_index = 0  # = 0
a_index_founded = False


def check_elements_of_links_and_names(links_and_names, link_and_name):
    already_is = False
    for element in links_and_names:
        if element[str_link] == link_and_name[str_link]:
            already_is = True
            element[str_amount_of_chapters] += 1

    if (already_is == False):
        links_and_names.append(link_and_name)

    return already_is


end = False

number = 1

amount_of_pages = info_parser_.Find_last_page()

p_index, a_index = info_parser_.Find_indexes(p_index, a_index)

for page_number in range(start_page, amount_of_pages):
    bS = info_parser_.BS_html_from_page_number(page_number)
    story_items = bS.select('.span8 .story-item')

    for story_item in story_items:
        p = story_item.findAll('p')
        meta_info = p[p_index]    # = 1
        limit_is_exceeded = time_calc_.Limit_is_exceeded(now_, meta_info, seconds_limit)
        if (limit_is_exceeded):
            end = True
            break
        a = meta_info.findAll('a')  # <class 'bs4.element.Tag'>
        link_with_name = a[a_index]    # = 0
        link_and_name = Link_and_name_temp.Create_link_and_name(link_with_name, number)
        already_is = check_elements_of_links_and_names(links_and_names, link_and_name)
        if(already_is == False):
            number += 1

        #chapter_link_and_name = story_item.find('h3')
    if(end):
        break


for item in links_and_names:
    Link_and_name_temp.Make_readable(item)


output_form = input("Форма вывода (C (англ.) — консоль, F — в файл): ")
print()

if (output_form == 'F'):
    file_writer = File_writer()
    file_writer.Write(file_name, links_and_names)


if (output_form == 'C'):
    for each in links_and_names:
        for key in each.keys():
            print(each[key])
        print()
    input()
