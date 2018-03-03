class Link_and_name_:

    link_main = "https://ponyfiction.org"
    str_number = 'number'
    str_name = 'name'
    str_link = 'link'
    str_amount_of_chapters = 'amount_of_chapters'


    def Create_self(self, link_with_name, number):
        link_and_name = dict()
        link_and_name[self.str_number] = number
        link_and_name[self.str_name] = link_with_name.contents[0]
        link_and_name[self.str_link] = self.link_main + link_with_name.get('href')
        link_and_name[self.str_amount_of_chapters] = 1
        return link_and_name


    def Make_readable(self, item):
        item[self.str_number] = '№ ' + str(item[self.str_number])
        item[self.str_amount_of_chapters] = 'Кол-во глав: ' + str(item[self.str_amount_of_chapters])


    def Make_readables(self, links_and_names):
        for item in links_and_names:
            self.Make_readable(item)


    def Check_list_of_self(self, links_and_names, link_and_name):
        already_is = False
        for element in links_and_names:
            if element[self.str_link] == link_and_name[self.str_link]:
                already_is = True
                element[self.str_amount_of_chapters] += 1

        if (already_is == False):
            links_and_names.append(link_and_name)

        return already_is


    def Print_self(self, link_and_name):
        for key in link_and_name.keys():
            print(link_and_name[key])
        print()


    def Print_selfs(self, links_and_names):
        for link_and_name in links_and_names:
            self.Print_self(link_and_name)
