import re
import pg8000

ft_inch_format = re.compile(r"([0-9]+) \` ([0-9]*\.?[0-9]+) \"")


def ft_inch_to_cm(ft_inch):
    matched = ft_inch_format.match(ft_inch)
    if matched is None:
        return None
    else:
        inches = int(matched.group(1)) * 12 + int(matched.group(2))
        centimeters = round(inches * 2.54)
        return centimeters


def cm_to_ft_inch(centimeters):
    feet = int(0.0328 * centimeters)
    remaining = centimeters - (feet * 30.48)
    inch = round(0.3937 * remaining)
    return str(feet) + " ` " + str(inch) + " \""


try:
    conn = pg8000.connect(user='postgres', host='localhost', port=5432,
                          database='woveny', password='docker')
    db = conn
    cursor = db.cursor()
except pg8000.Error:
    print("Database connect failed")

cursor.execute(
    "select sku_number, width_by_cm, width_by_inches, length_by_cm, length_by_inches "
    "from product "
    "where (length_by_cm is null "
    "or length_by_cm = 0 "
    "or length_by_inches "
    "is null or length_by_inches = '');")

resultSet = cursor.fetchall()

for result in resultSet:
    sku_number = result[0]
    cm_first = result[1]
    ftinch_second = result[2]
    cm_third = result[3]
    ftinch_fourth = result[4]
    if (result[1] == 0) and (result[2] != ''):
        cm_first = ft_inch_to_cm(result[2])
        if cm_first is None:
            continue
    if (result[1] != 0) and (result[2] == ''):
        ftinch_second = cm_to_ft_inch(result[1])
    if (result[3] == 0) and (result[4] != ''):
        cm_third = ft_inch_to_cm(result[4])
        if cm_third is None:
            continue
    if (result[3] != 0) and (result[4] == ''):
        ftinch_fourth = cm_to_ft_inch(result[3])
    cursor.execute("update product "
                   "set width_by_cm = " + str(cm_first) + "," +
                   " width_by_inches = '" + str(ftinch_second) + "'," +
                   " length_by_cm = " + str(cm_third) + "," +
                   " length_by_inches = '" + str(ftinch_fourth) + "'" +
                   " where sku_number = '" + sku_number + "';")
    conn.commit()
    print(sku_number)
