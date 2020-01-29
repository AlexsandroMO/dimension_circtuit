#import numpy as np
import pandas as pd
import pandasql as ps
import sqlite3


def read_sql_queda(queda):

	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT queda_tesao FROM cable_tabelacondutor
        WHERE secao = '{queda}';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()

	return read_db


def read_sql_corr(corr):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT capacidade_conducao FROM cable_tabelacondutor
        WHERE secao = '{corr}';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()

	return read_db


def read_sql_dj(dj):

	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT dj FROM cable_disjuntor
        WHERE dj = '{dj}';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()

	return read_db

def read_sql_filter(projeto):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT project FROM cable_project
        WHERE id like '{projeto}';

	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db


def read_sql_filter_id(id_x):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT id FROM cable_rproject
        WHERE r_project like '{id_x}';

	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db

#---
def read_sql_filter_name(id_x):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT project FROM cable_project
        WHERE id = '{id_x}';

	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db

def read_sql_tension(tens):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT type_tension FROM calc_tension
        WHERE id = '{tens}';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()

	return read_db



#--------------------------------------
def table_calc(corrent, tension):
	
	tens = ['1.5','2.5','4','6','10','16','25','35','50','70','95','120','150','185','240','300']
	queda = [34,18,12,7.6,4.5,2.7,1.7,1.2,0.96,0.67,0.48,0.38,0.31,0.25,0.19,0.15]
	corr = [21,30,40,51,71,95,125,155,190,240,290,340,385,440,520,590]

	new = []
	for a in range(len(tens)):
		new.append([tens[a],queda[a],corr[a]])

	table = pd.DataFrame(data=new,columns=['Cable','Queda','Corrente'])
	
	result = corrent / tension
	res = round(result + 0.5)

	new = []
	for a in table['Corrente']:
		if res > int(a):
			pass
		else:
			new.append(a)
			num = int(new[0])
	
	new_table = table[table['Corrente'] == num]

	return new_table

'''
def table_tens(p_va, tension):

	tens = ['1.5','2.5','4','6','10','16','25','35','50','70','95','120','150','185','240','300']
	queda = [34,18,12,7.6,4.5,2.7,1.7,1.2,0.96,0.67,0.48,0.38,0.31,0.25,0.19,0.15]
	corr = [21,30,40,51,71,95,125,155,190,240,290,340,385,440,520,590]

	new = []
	for a in range(len(tens)):
		new.append([tens[a],queda[a],corr[a]])
        
	table = pd.DataFrame(data=new,columns=['Cable','Queda','Corrente'])
	
	xx = str(tension)

	result = p_va / int(xx)
	res = round(result + 0.5)

	new = []
	for a in table['Corrente']:
		if res > int(a):
			pass
		else:
			new.append(a)
			num = int(new[0])
	
	new_table = table[table['Corrente'] == num]
	new = []
	for a in new_table['Cable']:
		return a
		#new.append(a)
'''

def table_tens(p_va, tension):

    tens = ['1,5','2,5','4','6','10','16','25','35','50','70','95','120','150','185','240','300']
    queda = [34,18,12,7.6,4.5,2.7,1.7,1.2,0.96,0.67,0.48,0.38,0.31,0.25,0.19,0.15]
    corr = [21,30,40,51,71,95,125,155,190,240,290,340,385,440,520,590]

    new = []
    for a in range(len(tens)):
        new.append([tens[a],queda[a],corr[a]])
        
    table = pd.DataFrame(data=new,columns=['Cable','Queda','Corrente'])

    xx = str(tension)

    result = p_va / int(xx)
    res = round(result + 0.5)

    new = []
    for a in table['Corrente']:
        if res > int(a):
            pass
        else:
            new.append(a)
            num = int(new[0])

    new_table = table[table['Corrente'] == num]
    new = []

    for a in new_table['Corrente']:
        return a


def table_disj(power, tens):

    corr = [8,15,18,23,30,38,48,60,68,78,98,123,148,178,228]
    dj = [10,16,20,25,32,40,50,63,70,80,100,125,150,180,200,230]

    new = []
    for a in range(len(corr)):
        new.append([corr[a],dj[a]])
        
    table = pd.DataFrame(data=new,columns=['Corrente','DJ'])

    xx = str(tens)

    result = power / int(xx)
    res = round(result + 0.5)

    new2 = []
    for a in table['Corrente']:
        if res > int(a):
            pass
        else:
            new2.append(a)
            num = int(new2[0])

    new_table = table[table['Corrente'] == num]
    new = []

    for a in new_table['DJ']:
        return a

def calc_cable(dist, corr,tens):

    x = str(tens)

    list_127 = f'''1.5 1.5 1.5	1.5	1.5	1.5	1.5	1.5	2.5	2.5	2.5	2.5	2.5
    1.5	1.5	1.5	1.5	1.5	1.5	1.5	1.5	4	4	4	6	6
    1.5	1.5	1.5	1.5	1.5	1.5	4	4	6	6	6	10	10
    1.5	1.5	1.5	1.5	1.5	2.5	2.5	4	4	4	6	10	10
    1.5	1.5	1.5	1.5	1.5	2.5	4	4	6	6	6	16	16
    1.5	1.5	1.5	4	4	6	6	10	10	10	10	16	25
    1.5	1.5	4	4	6	6	10	10	10	16	25	25  25
    1.5	2.5	4	6	4	6	10	10	16	16	16	35	35
    1.5	4	6	6	6	10	10	16	16	16	25	35	50
    2.5	4	6	10	6	10	10	16	16	25	25	50	50
    2.5	4	6	10	10	16	16	25	25	35	35	50	50
    2.5	6	10	10	10	16	16	25	25	25	35	70	70
    4	6	10	16	10	16	25	25	25	35	35	70	95
    4	10	10	16	10	16	25	25	35	35	50	95	95
    4	10	16	16	25	35	50	50	70	70	95	95	95
    6	10	16	16	25	50	50	70	70	95	95 95 120
    6	10	16	25	25	50	50	70	95	95	95	120	120
    6	16	25	25	35	50	70	95	95	120	120	150	150
    10	16	25	25	35	50	70	95	120	120	150	150	185
    10	16	25	25	50	70	95	95	120	150	150	185	240
    10	25	35	50	50	95	95	120	120	150	240	240	240'''

    list_220 = f'''1.5	1.5	1.5	1.5	1.5	1.5	1.5	1.5	1.5	1.5	1.5	1.5	1.5
    1.5	1.5	1.5	1.5	1.5	1.5	1.5	1.5	2.5	2.5	2.5	2.5	4
    1.5	1.5	1.5	1.5	1.5	1.5	2.5	2.5	2.5	4	4	4	6
    1.5	1.5	1.5	1.5	1.5	2.5	2.5	4	4	4	6	6	6
    1.5	1.5	1.5	1.5	1.5	2.5	4	4	6	6	6	10	10
    1.5	1.5	1.5	2.5	2.5	4	6	6	10	10	10	10	16
    1.5	1.5	2.5	2.5	4	6	6	10	10	10	16	16	16
    1.5	1.5	2.5	4	4	6	10	10	16	16	16	16	25
    1.5	2.5	2.5	4	6	10	10	16	16	16	25	25	25
    1.5	2.5	4	4	6	10	10	16	16	25	25	25	25
    1.5	2.5	4	6	6	16	16	16	25	25	25	25	35
    1.5	4	6	6	10	16	16	25	25	25	35	35	35
    2.5	4	6	10	10	16	25	25	25	35	35	50	50
    2.5	4	6	10	10	16	25	25	35	35	50	50	50
    2.5	6	10	10	16	25	25	35	50	50	50	70	70
    2.5	6	10	10	16	25	35	35	50	50	50	70	70
    4	6	10	16	16	25	35	35	50	50	70	70	70
    4	10	10	16	25	25	35	50	50	70	70	95	95
    4	10	16	16	25	35	50	50	70	70	95	95	95
    6	10	16	25	25	35	50	70	70	95	95	120	120
    6	16	25	25	35	50	70	70	95	95	120	150	150'''
 
    if int(x) == 127:
        desm = list_127.split('\n')
    else:
        desm = list_220.split('\n')

    x = []
    for a in desm:
        list_all = a.split()
        x.append(list_all)

    table_220 = pd.DataFrame(
                data=x,
                columns=['10','20','30','40','60','75','100','125','150','175','200','225','250'],
                index=['1.0','2.0','3.0','4.0','5.0','7.5','10.0','12.5','15.0','17.5','20.0','25.0','30.0','35.0','40.0','45.0','50.0','60.0','70.0','80.0','100.0']\
                )

    new_col = []
    for a in table_220.columns:
        new_col.append(int(a))

    new1 = []
    for a in new_col:
        if int(dist) > float(a):
            pass
        else:
            new1.append(a)

    dist = str(min(new1))

    y = []
    for a in table_220[dist].index:
        if float(a) > int(corr):
            y.append(float(a))

    return table_220[dist].loc[str(float(min(y)))]