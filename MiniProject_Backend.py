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

def SearchMovieData(M_ID="",M_NAME="",Release_Date="",Director="",Budget="",Duration="",Rating=""):  
    connection = mysql.connector.connect(host='localhost',
                                            database='project',
                                            user='root',
                                            password='admin',
                                            charset='utf8')
    cur = connection.cursor()
    lst=[M_ID,M_NAME,Release_Date,Director,Budget,Duration,Rating]
    for i in lst:
        if i == "":
            lst.remove(i)
    for i in lst:
        if i == M_ID:
            M_ID=int(M_ID)
            continue
        if i == Budget:
            Budget=float(Budget)
            continue
        if i == Rating:
            Rating=float(Rating)
            continue
        if i == Duration:
            Duration == float(Duration)
            continue
    l=len(lst)
    qsearch="SELECT * FROM movie WHERE "
    for i in lst:
        if c==0 and l>1:
            if i == M_ID:
                qsearch+="M_ID=%d AND "
            continue
            if i == Budget:
                qsearch+="Budget=%f AND "
            continue
            if i == Rating:
                qsearch+="Rating=%f AND"
            continue
            if i == Duration:
                qsearch+="Duration=%f AND"
            continue
        else:
            if i == M_ID:
                qsearch+=
            continue
            if i == Budget:
                Budget=float(Budget)
            continue
            if i == Rating:
                Rating=float(Rating)
            continue
            if i == Duration:
                Duration == float(Duration)
            continue
    args=tuple(lst)
    cur.execute(qsearch %args)
    rows=cur.fetchall()
    connection.close()    
    return rows

def UpdateMovieData(id,M_ID="",M_NAME="",Release_Date="",Director="",Budget="",Duration="",Rating=""):
    connection = mysql.connector.connect(host='localhost',
                                            database='project',
                                            user='root',
                                            password='admin',
                                            charset='utf8')
    cur = connection.cursor()
    cur.execute("UPDATE movie SET M_ID=?,M_NAME=?,Release_Date=?,Director=?,Cast=?,Budget=?,Duration=?,Rating=?, WHERE id=?",(M_ID,M_NAME,Release_Date,Director,Budget,Duration,Rating))
    connection.commit()
    connection.close()

