### unotes
a notes generator app for everyone!


## how to use
-> just clone the file
-> create a new file in the same directory as the unotes.py file
-> write this code

form unotes import unotes
notes = unotes("note_topic_1","note_topic_2",)
data = notes.search()
// you can print `data` if you want
// if you want to save notes in a file, which I would recommend, then
notes.save_all('file_name',data)
//this creates an html file with your notes.