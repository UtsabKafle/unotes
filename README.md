### unotes
a notes generator app for everyone!


## how to use
1) just clone the file
2) create a new file in the same directory as the unotes.py file
3) write this code

- `form unotes import unotes`
- `notes = unotes("note_topic_1","note_topic_2",)`
- `data = notes.search()`
- `data` is a list of dictionary with 3 key value pairs. The keys are `name`, `content` and `links` which contains, the heading you passed, the content from wikipedia and the top links on google as values respectively.

- // if you want to save notes in a file, then you can use the `save_all` method availabe.
- `notes.save_all('file_name',data)`
-//
//this creates an html file with your notes.