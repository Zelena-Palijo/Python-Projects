

import sqlite3

conn = sqlite3.connect('assignment.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fname TEXT)")
    #Added execute command as provided before, but should be table persons? or other table name
    conn.commit()
conn.close()

#provided file list
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('assignment.db')
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_persons(col_fname) VALUES(?)",(x,))
            #one element tuple
            print(x)
            conn.commit()
conn.close()
