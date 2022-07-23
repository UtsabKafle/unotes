### unotes
a notes generator app for everyone!



#### let me try to write it more professionally >_<

Okay, Unotes is a web scrapping project that pulls the defination from wikipedia using the wikipedia library in python and also pulls the top reults from google making it easier to just copy the notes and submit to your teacher or whatever.





## how to use
1) just clone the project or download the <a href='https'>unotes.py</a> file
2) create a new file in the same directory as the unotes.py file
3) write this code

- `form unotes import unotes`
- `notes = unotes("note_topic_1","note_topic_2",)`
- `chapters = notes.search()`
- // `chapters` is a list of dictionary with 3 key value pairs. The keys are `name`, `content` and `links` which contains, the parameter you passed, the content from wikipedia and the top links on google as values respectively.

- // if you want to save notes in a file, then you can use the `save` method.
- `notes.save('file.html',chapters)`
- // this will create a file with the name you passed and write the content with some styling using html and css.