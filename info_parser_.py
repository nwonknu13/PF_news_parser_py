import requests, bs4

class Info_parser_:

    link_main = "https://ponyfiction.org"
    link_pattern = link_main + "/stream/chapters/page/"


    def BS_html_from_page_number(self, page_number):
        resp = requests.get(self.link_pattern + str(page_number))  # <class 'requests.models.Response'>
        bS = bs4.BeautifulSoup(resp.text, "html.parser")
        return bS


    def Find_last_page(self):
        bS = self.BS_html_from_page_number(1)
        last_page = int(bS.select('.span8 .pagination .btn')[-1].contents[0])
        return last_page


    def Find_indexes(self, p_index, a_index):
        bS = self.BS_html_from_page_number(1)
        story_items = bS.select('.span8 .story-item')
        story_item = story_items[0]
        p = story_item.findAll('p')
        for each_p in p:
            if (each_p.findAll('a') != []):
                break
            else:
                p_index += 1
        meta_info = p[p_index]  # = 1
        a = meta_info.findAll('a')  # <class 'bs4.element.Tag'>
        for each_a in a:
            if (each_a.findAll('a', class_="authorlink") == []):
                break
            else:
                a_index += 1

        return p_index, a_index