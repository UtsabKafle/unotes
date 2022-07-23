import requests
from bs4 import BeautifulSoup
import wikipedia

class unotes:
    def __init__(self,*args):
        self.data_list = [a.replace(' ','_')for a in args]
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
            try:
                main_result = wikipedia.summary(searches[0],auto_suggest=False)
            except:
                main_result = f"Some errors. Please consider changing the parameters for {data[i]}. :) "
            self.content[f'{data[i]}'] = main_result
            req = requests.get(f"https://www.google.com/search?q={str(data[i].replace('_','+'))}")
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
        return contents
        
    def save(self,file_name,data_obj):
        html_upper = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Unotes</title>
    <style>

        .left-cont{
             border-radius: 15px;
            display: block;
            float: left;
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
            font-weight:700;
            border:1px solid black;
            padding:3px;
            background-color:skyblue;

        }
        #links_show{
            display: none;
        }
        h3{
            text-align:center;
        }
    </style>
</head>
<body>
    <div class="navbar">
        <div class="nav-text">U-notes</div>
    </div>
        """
        html_lower = f"</body></html>"
        file =  open(f'output/{str(file_name)}','w+',encoding='utf-8')
        file.write(str(html_upper))
        for i in data_obj:
            name = i['name']
            content = i['content']
            links = i['links']
            show_function_ = f"<script>function show_{name}(){'{'} {'if'} (document.getElementById('links_show{name}').style.display == 'none') {'{'} document.getElementById('links_show{name}').style.display = 'block';{'}'}else{'{'}document.getElementById('links_show{name}').style.display = 'none';{'}}'}</script>"
            content_ = f"<h3>{name}</h3><p>{content}</p><hr><div class='more'><button type='button' class='show-text' onclick='show_{name}();'>See links ^_^</button><div class='more-links' style='display:none;' id='links_show{name}' >"
            file.write(str(show_function_))
            file.write(str(content_))
            for link in links:
                link_ = f"<div class='link'><a href='{link}' target='_blank'>{link}</a></div>"
                file.write(str(link_))
            content_end = "</div>"
            file.write(str(content_end))
        file.write(str(html_lower))
        file.close()

def main():
    note = unotes('param1','param2')
    chapters = note.search()
    note.save('new_file.html',chapters)
    
if __name__=='__main__':
    main()