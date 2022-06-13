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
        for i in self.data_list:
            req = requests.get(f"https://www.google.com/search?q={i}")
            content = BeautifulSoup(req.text,features='html.parser')
            x = content.find_all('a')
            links = []
            for j in x:
                link = j.attrs['href']
                if 'url' in link.split("?")[0]:
                    url_ = link.split("?")[1].split("&")[0].split("=")[1]
                    if "%" not in url_:
                        links.append(url_)
            self.links[i] = links
            print("   ---    "*20)
            print(self.links)
        return self.links
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
           
    def save_all(self,file_name,data_obj):
        html_upper = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Unotes</title>
    <style>
        .left-cont{
            border-radius: 15px;
            display: block;
            margin: 25px 10px;
            box-shadow: 15px 15px 20px 5px rgb(212, 233, 231);
            padding: 15px;
        }
        .navbar{
            height: 45px;
            background-color: rgb(79, 210, 210);
            border: 1px solid blue;
            text-align: center;
        }
        .nav-text{
            align-self: center;
            margin: 14px 5px;
            font-weight: bold;
            font-family: 'Courier New', Courier, monospace;
            color: white;
        }
        .show-text{
            cursor: pointer;
        }
        #links_show{
            display: none;
        }
    </style>
</head>
<body>
    <div class="navbar">
        <div class="nav-text">U-notes</div>
    </div>
        """
        html_lower = f"</body></html>"
        file =  open(f'output/{str(file_name)}.html','w+')
        file.write(str(html_upper))
        for i in data_obj:
            content_ = f"<h3>{i}</h3><p>{data_obj[i]}</p><hr><div class='more'><div class='show-text' onclick='show();'>Show more links</div> <div class='more-links' id='links_show{i}' ></div>"
            show_function_ = f"<script>function show(){'{'} {'if'} (document.getElementById('links_show{i}').style.display == 'block') {'{'} document.getElementById('links_show{i}').style.display = 'none';{'}'}else{'{'}document.getElementById('links_show{i}').style.display = 'block';{'}}'}</script>"
            file.write(str(show_function_))
            file.write(str(content_))
        file.write(str(html_lower))
        file.close()

def main():
    note = unotes('nepal','india','usa')
    a = note.search()
    # print(a)
    note.save_all('crap',a)
    
if __name__=='__main__':
    main()