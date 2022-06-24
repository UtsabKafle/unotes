from cgitb import text
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
###
import requests
from bs4 import BeautifulSoup
import wikipedia


class unotes:
    def __init__(self,*args):
        self.data_list = args
        self.content = {}
        self.links = {}
    def __str__(self):
        return f"unotes for {self.data_list}"
    def search(self):
        contents = []
        wiki_content = []
        sub_results = []
        data = self.data_list
        for i in range(len(data)):
            searches = wikipedia.search(data[i])
            # print(searches)
            main_result = wikipedia.summary(searches[0],auto_suggest=False)
            self.content[f'{data[i]}'] = main_result
            req = requests.get(f"https://www.google.com/search?q={data[i]}")
            content = BeautifulSoup(req.text,features='html.parser')
            x = content.find_all('a')
            links = []
            for j in x:
                link = j.attrs['href']
                if 'url' in link.split("?")[0]:
                    url_ = link.split("?")[1].split("&")[0].split("=")[1]
                    if "%" not in url_:
                        links.append(url_)
            self.links[data[i]] = links
            temp_ = {'name':f'{data[i]}','content':str(main_result),'links':links}
            contents.append(temp_)
            # print("   ---    "*20)
            # print(self.links)
        # print(contents[1])
        return contents

    def wikipedia_search(self):
        wiki_content = []
        sub_results = []
        data = self.data_list
        for i in range(len(data)):
            searches = wikipedia.search(data[i])
            print(searches)
            main_result = wikipedia.summary(searches[0],auto_suggest=False)
            self.content[f'{self.data_list[i]}'] = main_result
        return self.content





class SayHello(App):
    def search(self,instance):
            inp = self.inp.text
            note = unotes(inp)
            self.result = note.search()
            print(self.result)
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.5,0.9)
        self.window.pos_hint = {'center_x':0.5,'center_y':0.5}
        self.shit = Label(text="Unotes",font_size=20)
        self.window.add_widget(self.shit)
        self.inp = TextInput(multiline=False,padding_y = (10,10),size_hint = (1,0.3),padding_x = (10,10))
        self.window.add_widget(self.inp)
        self.btn = Button(text='search',size_hint=(1,0.3),bold=True,background_color='#00FFCE')
        self.btn.bind(on_press=self.search)
        self.window.add_widget(self.btn)
        self.shit = Label(text="Enter the topics. Seperate them with commas.",font_size=11)
        self.window.add_widget(self.shit)
        return self.window

if __name__ == "__main__":
    SayHello().run()