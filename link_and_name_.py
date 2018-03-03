class Link_and_name_:

    link_main = "https://ponyfiction.org"
    str_number = 'number'
    str_name = 'name'
    str_link = 'link'
    str_amount_of_chapters = 'amount_of_chapters'


    def Create_link_and_name(self, link_with_name, number):
        link_and_name = dict()
        link_and_name[self.str_number] = number
        link_and_name[self.str_name] = link_with_name.contents[0]
        link_and_name[self.str_link] = self.link_main + link_with_name.get('href')
        link_and_name[self.str_amount_of_chapters] = 1
        return link_and_name


    def Make_readable(self, item):
        item[self.str_number] = '№ ' + str(item[self.str_number])
        item[self.str_amount_of_chapters] = 'Кол-во глав: ' + str(item[self.str_amount_of_chapters])

