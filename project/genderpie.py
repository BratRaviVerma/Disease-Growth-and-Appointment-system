import matplotlib.pyplot as plt
from dboperation.dbconnection import DatabaseConnection as dbc

def main():

    con = dbc.createconnection()
    dbcursor = con.cursor()
    str1 = "select count(registrationid) from patient where gender = 'M';"
    dbcursor.execute(str1)
    m_pat = dbcursor.fetchall()
    str2 = "select count(registrationid) from patient where gender = 'F';"
    dbcursor.execute(str2)
    f_pat = dbcursor.fetchall()
    graphlabels = ('Male Patients', 'Female Patients')
    sizes = [m_pat, f_pat]
    clr = ['green', 'red']
    plt.pie(sizes, labels=graphlabels, colors=clr)
    plt.title('Gender Vs Disease')
    plt.show()


if __name__ == '__main__':
    main()
