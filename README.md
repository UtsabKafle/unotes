## unotes
Search for notes.



Unotes is a web scrapping project that pulls the defination from wikipedia using the wikipedia library and also scraps the top reults from google making it easier to just copy the notes and submit to your teacher or whatever.





## how to use
1) just clone the project or download the <a target="_blank" href='https://github.com/UtsabKafle/unotes/blob/master/unotes.py'>unotes.py</a> file.
        OR
    ```sh
    pip install unotes
2) Usuage 

- `form unotes import unotes`
- // create a unotes instance
- `notes = unotes("note_topic_1","note_topic_2",)`
- // pass the topics you want to search as parameters to the unotes class. Spaces in the parameters is supported.
- `chapters = notes.search()`
- // `Search` returns a list of dictionaries. `chapters` is a list of dictionaries with 3 key value pairs. The keys are `name`, `content` and `links` which contains, the parameter you passed, the content from wikipedia and the top links on google as values respectively.

- // if you want to save notes in a file, then you can use the `save` method.
- `notes.save('file.html',chapters)`
- // this will create a file with the name you passed and write the content with some styling using html and css.
