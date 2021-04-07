#backend
import mysql.connector
import get_variable_name
    
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

def DeleteMovieRec(m_id):    
    connection = mysql.connector.connect(host='localhost',
                                            database='project',
                                            user='root',
                                            password='admin',
                                            charset='utf8')
    cur = connection.cursor()
    cur.execute("DELETE FROM movie WHERE M_id=%d" %m_id)
    connection.commit()
    connection.close()  

def SearchMovieData(M_ID):  
    connection = mysql.connector.connect(host='localhost',
                                            database='project',
                                            user='root',
                                            password='admin',
                                            charset='utf8')
    cur = connection.cursor()
    M_ID=int(M_ID)
    qsearch="SELECT * FROM movie WHERE M_ID=%d" %M_ID
    cur.execute(qsearch)
    rows=cur.fetchall()
    connection.close()    
    return rows

