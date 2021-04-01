#backend
import mysql.connector
    
def AddMovieRec(M_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating):
    connection = mysql.connector.connect(host='localhost',
                                            database='project',
                                            user='root',
                                            password='admin',
                                            charset='utf8')
    cur = connection.cursor()
    cur.execute("INSERT INTO movie VALUES (NULL, ?,?,?,?,?,?,?,?)", (M_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    connection.commit()
    connection.close()

def ViewMovieData():
    connection = mysql.connector.connect(host='localhost',
                                            database='project',
                                            user='root',
                                            password='admin',
                                            charset='utf8')
    cur = connection.cursor()
    cur.execute("SELECT * FROM movie")
    rows=cur.fetchall()
    connection.close()    
    return rows

def DeleteMovieRec(id):    
    connection = mysql.connector.connect(host='localhost',
                                            database='project',
                                            user='root',
                                            password='admin',
                                            charset='utf8')
    cur = connection.cursor()
    cur.execute("DELETE FROM movie WHERE id=?", (id,))
    connection.commit()
    connection.close()  

def SearchMovieData(M_ID="",Movie_Name="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):  
    connection = mysql.connector.connect(host='localhost',
                                            database='project',
                                            user='root',
                                            password='admin',
                                            charset='utf8')
    cur = connection.cursor()
    cur.execute("SELECT * FROM movie WHERE M_ID=? OR Movie_Name=? OR Release_Date=? OR Director=? OR Cast=? OR Budget=? OR Duration=? OR Rating=?",(M_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    rows=cur.fetchall()
    connection.close()    
    return rows

def UpdateMovieData(id,M_ID="",Movie_Name="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):
    connection = mysql.connector.connect(host='localhost',
                                            database='project',
                                            user='root',
                                            password='admin',
                                            charset='utf8')
    cur = connection.cursor()
    cur.execute("UPDATE movie SET M_ID=?,Movie_Name=?,Release_Date=?,Director=?,Cast=?,Budget=?,Duration=?,Rating=?, WHERE id=?",(M_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    connection.commit()
    connection.close()

