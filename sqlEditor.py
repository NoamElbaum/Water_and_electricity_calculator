import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="apartments"
)

cursor = db.cursor()


def addVal(table, wPrice, ePrice, waterNew, electricityNew):
    try:
        waterNew = int(waterNew)
        electricityNew = int(electricityNew)
    except:
        return 1
    cursor.execute('select max(date) from ' + table)
    lastDate = cursor.fetchone()
    # print(lastDate)
    sqlDate = ''
    count = 0
    for i in str(lastDate):
        if i.isdigit():
            sqlDate += i
        elif i == ',':
            if count < 2:
                sqlDate += '-'
                count += 1

    cursor.execute("select water from " + table + " where date = " + "'" + sqlDate + "'")
    waterVal = cursor.fetchone()
    water = waterVal[0]
    cursor.execute("select electricity from " + table + " where date = " + "'" + sqlDate + "'")
    electricityVal = cursor.fetchone()
    electricity = electricityVal[0]
    # print(sqlDate)
    # print(electricity)
    # print(water)

    if water > waterNew or electricity > electricityNew:
        print('wrong values!!!!!!!!!')
        return False
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    waterT = (waterNew - water) * wPrice
    elecT = int((electricityNew - electricity) * ePrice)
    lineVal = [f"'{date}'",
               str(waterNew),
               str(electricityNew),
               f"'({waterNew}-{water})*{wPrice} = {waterT}'",
               f"'({electricityNew}-{electricity})*{ePrice} = {elecT}'",
               str(waterT + elecT)]
    sql = 'insert into ' + table + ' values (' + lineVal[0] + ',' + lineVal[1] + ',' + lineVal[2] + ',' + lineVal[
        3] + ',' + lineVal[4] + ',' + lineVal[5] + ')'
    cursor.execute(sql)
    # print(sql)
    db.commit()
    return 0


def getData(apartment):
    cursor.execute('SELECT date FROM apartments.' + apartment)
    date = cursor.fetchall()
    cursor.execute('SELECT water FROM apartments.' + apartment)
    water = cursor.fetchall()
    cursor.execute('SELECT electricity FROM apartments.' + apartment)
    electricity = cursor.fetchall()
    cursor.execute('SELECT total_water FROM apartments.' + apartment)
    total_w = cursor.fetchall()
    cursor.execute('SELECT total_electricity FROM apartments.' + apartment)
    total_e = cursor.fetchall()
    cursor.execute('SELECT total_payment FROM apartments.' + apartment)
    total_p = cursor.fetchall()

    data = [date, water, electricity, total_w, total_e, total_p]
    print(data)
    return data
