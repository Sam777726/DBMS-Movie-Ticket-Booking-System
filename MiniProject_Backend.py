#backend
import mysql.connector
    
def AddMovieRec(M_ID,M_NAME,Release_Date,Director,Budget,Duration,Rating):
    connection = mysql.connector.connect(host='localhost',
                                            database='project',
                                            user='root',
                                            password='admin',
                                            charset='utf8')
    cur = connection.cursor()
    q="INSERT INTO movie VALUES ('%f','%s','%s','%s','%d','%f','%f')"
    arg=(Duration,M_NAME,Release_Date,Director,M_ID,Rating,Budget)
    cur.execute(q %arg)
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
    cur.execute("DELETE FROM movie WHERE id=%d", id)
    connection.commit()
    connection.close()  

def SearchMovieData(M_ID="",M_NAME="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):  
    connection = mysql.connector.connect(host='localhost',
                                            database='project',
                                            user='root',
                                            password='admin',
                                            charset='utf8')
    cur = connection.cursor()
    cur.execute("SELECT * FROM movie WHERE M_ID=? OR M_NAME=? OR Release_Date=? OR Director=? OR Budget=? OR Duration=? OR Rating=?",(M_ID,M_NAME,Release_Date,Director,Budget,Duration,Rating))
    rows=cur.fetchall()
    connection.close()    
    return rows

def UpdateMovieData(id,M_ID="",M_NAME="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):
    connection = mysql.connector.connect(host='localhost',
                                            database='project',
                                            user='root',
                                            password='admin',
                                            charset='utf8')
    cur = connection.cursor()
    cur.execute("UPDATE movie SET M_ID=?,M_NAME=?,Release_Date=?,Director=?,Cast=?,Budget=?,Duration=?,Rating=?, WHERE id=?",(M_ID,M_NAME,Release_Date,Director,Cast,Budget,Duration,Rating))
    connection.commit()
    connection.close()

