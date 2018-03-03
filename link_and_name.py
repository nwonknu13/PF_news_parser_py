import json


class Link_and_Name:

    link_main = "https://ponyfiction.org"

    str_number = 'number'
    str_name = 'name'
    str_link = 'link'
    str_amount_of_chapters = 'amount_of_chapters'

    link_and_name = dict()


    def __init__(self, link_with_name, number):
        self.link_and_name[self.str_number] = number
        self.link_and_name[self.str_name] = link_with_name.contents[0]
        self.link_and_name[self.str_link] = self.link_main + link_with_name.get('href')
        self.link_and_name[self.str_amount_of_chapters] = 1


    def __str__(self):
        string_ = str()
        for key in self.link_and_name.keys():
            string_ += self.link_and_name[key] + '\n'
        return string_


    def One_more_chapter(self):
        self.link_and_name[self.str_amount_of_chapters] += 1


    def Get_link(self):
        return self.link_and_name[self.str_link]


    def Get_self(self):
        return self.link_and_name


    def Print_self(self):
        for key in self.link_and_name.keys():
            print(self.link_and_name[key])


    def Make_readable(self):
        self.link_and_name[self.str_number] = '№ ' + str(self.link_and_name[self.str_number])
        self.link_and_name[self.str_amount_of_chapters] = 'Кол-во глав: ' + str(self.link_and_name[self.str_amount_of_chapters])