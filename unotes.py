import re
import requests
from bs4 import BeautifulSoup


class unotes:
    def __init__(self,*args):
        self.data_list = args
    def __str__(self):
        return f"unotes for {self.data_list}"
    def search(self):
        contents = []
        for i in self.data_list:
            req = requests.get(f"https://www.google.com/search?q={i}")
            content = BeautifulSoup(req.text,features='html.parser')
            contents.append(content.prettify())
            print(contents)
        return contents

def main():
    note = unotes('computer')
    a = note.search()
    for i in a:
        # print("-----"*10,"    "*10,"-----"*10)
        file = open(f'file{len(i)}.html','w+',encoding="utf-8")
        file.write(str(i))
        file.close()
        # print(i)

if __name__=='__main__':
    main()