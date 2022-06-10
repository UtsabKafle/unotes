import re
import requests
from bs4 import BeautifulSoup
import wikipedia

class unotes:
    def __init__(self,*args):
        self.data_list = args
        self.content = {}
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
    def wikipedia_search(self):
        wiki_content = []
        sub_results = []
        data = self.data_list
        for i in range(len(data)):
            searches = wikipedia.search(data[i])
            print(searches)
            main_result = wikipedia.summary(searches[0])
            self.content[f'{self.data_list[i]}'] = main_result
        return self.content
           
    def save_all(self,file_name,data_obj):
        html_upper = f"<!DOCTYPE html><html lang='en'><head><title>Document</title></head><body>"
        html_lower = f"</body></html>"
        file =  open(f'{str(file_name)}.html','w+')
        file.write(str(html_upper))
        for i in data_obj:
            content_ = f"<h3>{i}</h3><p>{data_obj[i]}</p>"
            file.write(str(content_))
            for i in content_:
                print(i)
                print('------')
        file.write(str(html_lower))
        file.close()

def main():
    note = unotes('database')
    a = note.wikipedia_search()
    # print(a)
    note.save_all('kafle',a)
    
if __name__=='__main__':
    main()