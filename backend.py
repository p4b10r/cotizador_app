import sqlite3

db_name="database.db"

def runQuery(query,parameters=()):
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        result=cursor.execute(query, parameters)
        conn.commit()
    return result
#===============================DBCLIENTE===============================================
def insertDataCliente(cliente, empresa, email, comentarios):
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        result=cursor.execute('INSERT INTO clientes VALUES (NULL,?,?,?,?)',(cliente, empresa, email, comentarios))
        conn.commit()
        return result

def clearDataCliente():
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        result=cursor.execute('DELETE FROM clientes;',)
        conn.commit()
        return result


def getClientes(treecliente):
    query='SELECT * FROM clientes'
    db_rows=runQuery(query)
    for row in db_rows:
        treecliente.insert('',0,text=row[1],values=(row[2],row[3],row[4]))

#===============================DBLOTE===============================================

def insertDataLote(descripcion, pesolote, tiempolote, qpiezas, qlote):
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        result=cursor.execute('INSERT INTO lote VALUES (NULL,?,?,?,?,?,NULL)',(descripcion, pesolote, tiempolote, qpiezas, qlote))
        conn.commit()
        return result

def clearDataLote():
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        result=cursor.execute('DELETE FROM lote;',)
        conn.commit()
        return result

def deleteDataLote(treelote):

    descripcion=treelote
    query="DELETE FROM lote WHERE descripcion=?"
    runQuery(query,(descripcion,))


def getLote(treelote):

    records=treelote.get_children()
    if (records!=0):
        for elementos in records:
            treelote.delete(elementos)
        conn=sqlite3.connect(db_name)
        cursor=conn.cursor()
        query='SELECT * FROM lote'
        db_rows=cursor.execute(query)
        conn.commit()
        for row in db_rows:
            treelote.insert('',0,text=row[1],values=(row[2],row[3],row[4],row[5]))
#===============================DBCOSTOS===============================================

def insDataCostos(costofijo, nmaquinas, fmtto,horascubiertas,ferror,depreciacion,costohorareal,costomaterialpeso):
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        result=cursor.execute('INSERT INTO costos VALUES (NULL,?,?,?,?,?,?,?)',(costofijo, nmaquinas, fmtto,horascubiertas,ferror,depreciacion,costohorareal,costomaterialpeso))
        conn.commit()

def getDataCostos(treevariable):
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        db_rows=cursor.execute("SELECT * FROM costos")
        conn.commit()
        for row in db_rows:
            treevariable.insert('',0,values=(row[1],row[2],row[3],row[5],row[4], row[7],row[8]))
