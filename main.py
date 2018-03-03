import json, requests, bs4, datetime

from link_and_name import Link_and_Name


link_main = "https://ponyfiction.org"

link_pattern = link_main + "/stream/chapters/page/"

start_page = 1

limit = input('Поиск (за последний месяц — ввести "M"(англ.), или кол-во дней): \n')

now_ = datetime.datetime.now()

seconds_limit = 0


def set_seconds_limit(limit, seconds_limit):
    if (limit == 'M'):
        a_month_ago = now_
        if (now_.month > 1):
            a_month_ago = datetime.datetime(now_.year, (now_.month - 1), now_.day, now_.hour, now_.minute, now_.second,
                                            now_.microsecond, now_.tzinfo)
        else:
            a_month_ago = datetime.datetime((now_.year - 1), 11, now_.day, now_.hour, now_.minute, now_.second,
                                            now_.microsecond, now_.tzinfo)

        seconds_in_month = (now_ - a_month_ago).total_seconds()
        seconds_limit = seconds_in_month
    else:
        seconds_in_week = 3600 * 24 * int(limit)
        seconds_limit = seconds_in_week

    return seconds_limit


seconds_limit = set_seconds_limit(limit, seconds_limit)

links_and_names = list()

empty_arr = []

str_number = 'number'
str_name = 'name'
str_link = 'link'
str_amount_of_chapters = 'amount_of_chapters'

str_link_name = [str_name, str_link, str_amount_of_chapters]


file_name = 'PF_news'

p_index = 0  # = 1
p_index_founded = False

a_index = 0  # = 0
a_index_founded = False


def find_last_page():
    resp = requests.get(link_pattern + str(1))
    bS = bs4.BeautifulSoup(resp.text, "html.parser")
    pagination = bS.select('.span8 .pagination')[0]
    last_a = pagination.findAll('a', class_='btn')[-1]
    last_page = int(last_a.contents[0])
    return last_page


def create_link_and_name(link_with_name, number):
    link_and_name = dict()
    link_and_name[str_number] = number
    link_and_name[str_name] = link_with_name.contents[0]
    link_and_name[str_link] = link_main + link_with_name.get('href')
    link_and_name[str_amount_of_chapters] = 1
    return link_and_name


def check_elements_of_list_of_links(links_and_names, link_and_name):
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

amount_of_pages = find_last_page()

for page_noumber in range(start_page, amount_of_pages):
    resp = requests.get(link_pattern + str(page_noumber))  # <class 'requests.models.Response'>
    bS = bs4.BeautifulSoup(resp.text, "html.parser")
    span8 = bS.select('.span8')[0]  # <class 'bs4.element.Tag'>
    chapters_list = span8.find('div', id="chapters-list")  # <class 'bs4.element.Tag'>

    story_items = [story_item for story_item in chapters_list if (type(story_item) == bs4.element.Tag)]

    for story_item in story_items:
        p = story_item.findAll('p')
        if (p_index_founded == False):
            for each_p in p:
                if(each_p.findAll('a') != []):
                    p_index_founded = True
                else:
                    p_index += 1
        meta_info = p[p_index]    # = 1
        tag_time = meta_info.find('time')
        datetime_str = tag_time.get('datetime').split('T')
        date_ = [int(each) for each in datetime_str[0].split('-')]
        time_ = [int(each) for each in datetime_str[1].replace('Z', '').split(':')]
        datetime_story = datetime.datetime(date_[0], date_[1], date_[2], time_[0], time_[1], time_[2])
        time_delta = now_ - datetime_story
        if (time_delta.total_seconds() > seconds_limit):
            end = True
            break
        a = meta_info.findAll('a')  # <class 'bs4.element.Tag'>
        if (a_index_founded == False):
            for each_a in a:
                if(each_a.findAll('a', class_="authorlink") == []):
                    a_index_founded = True
                else:
                    a_index += 1
        link_with_name = a[a_index]    # = 0
        link_and_name = create_link_and_name(link_with_name, number)
        already_is = check_elements_of_list_of_links(links_and_names, link_and_name)
        if(already_is == False):
            number += 1

        #chapter_link_and_name = story_item.find('h3')
    if(end):
        break


for item in links_and_names:
    item[str_number] = '№ ' + str(item[str_number])
    item[str_amount_of_chapters] = 'Кол-во глав: ' + str(item[str_amount_of_chapters])


output_form = input("Форма вывода (C (англ.) — консоль, F — в файл): ")
print()

if (output_form == 'F'):
    file = []

    file_path = input("Путь до файла (\"1\" — в папку с main.py, или по указанному пути):\n")

    if (file_path == '1'):
        file = open(file_name + '.txt', 'w')
    else:
        file_path.replace('/', '\\')
        if(file_path[-1] != ('/' or '\\')):
            file_path += '\\'
        file = open(file_path + file_name + '.txt', 'w')

    counter = 0
    for i in links_and_names:
        for key in i.keys():
            file.write(i[key] + '\n')
        file.write('\n')

    file.close()

    #output = open(file_name + ".json", "w")
    #json.dump(links_and_names, output)
    #output.close()


if (output_form == 'C'):
    for each in links_and_names:
        for key in each.keys():
            print(each[key])
        print()
    input()