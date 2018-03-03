class File_writer:

    def Write(self, file_name, links_and_names):
        file = []

        file_path = input("Путь до файла (\"1\" — в папку с main.py, или по указанному пути):\n")

        if (file_path == '1'):
            file = open(file_name + '.txt', 'w')
        else:
            file_path.replace('/', '\\')
            if (file_path[-1] != ('/' or '\\')):
                file_path += '\\'
            file = open(file_path + file_name + '.txt', 'w')

        counter = 0
        for i in links_and_names:
            for key in i.keys():
                file.write(i[key] + '\n')
            file.write('\n')

        file.close()

        # output = open(file_name + ".json", "w")
        # json.dump(links_and_names, output)
        # output.close()