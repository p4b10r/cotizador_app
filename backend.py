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

def insertDataLote(descripcion,mat,pesolote, tiempolote, qpiezas, qlote):
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        result=cursor.execute('INSERT INTO lote VALUES (NULL,?,?,?,?,?,?,?,?,?)',(descripcion, mat, pesolote, tiempolote, qpiezas, qlote, costoHora(tiempolote),costoMaterial(mat,pesolote),costoHora(tiempolote)+costoMaterial(mat,pesolote)))
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
            treelote.insert('',0,text=row[1],values=(row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
#===============================DBCOSTOS===============================================

def insDataCostos(costofijo, maquinas, fmtto,horascubiertas,ferror,depreciacion,costohorareal,costomaterialpeso):
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        result=cursor.execute('INSERT INTO costos VALUES (NULL,?,?,?,?,?,?,?,?)',(costofijo, maquinas, fmtto,horascubiertas,ferror,depreciacion,((costofijo/(horascubiertas*maquinas))*ferror*fmtto)+depreciacion,fmtto*costofijo))
        conn.commit()

def deleteDataCostos(treevariable):
    with sqlite3.connect(db_name) as conn:
        descripcion=treevariable
        cursor=conn.cursor()
        cursor.execute('DELETE FROM costos;',)
        conn.commit()


def getDataCostos(treevariable):
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        db_rows=cursor.execute("SELECT * FROM costos")
        conn.commit()
        for row in db_rows:
            treevariable.insert('',0,text=row[1],values=(row[2],row[3],row[5],row[4],row[6], row[7],row[8]))



#==================================DBMATERIAL==========================================

def insertDataMaterial(pla,abs,petg,tecnico):
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO material VALUES (NULL,?,?,?,?)",(pla/1000,abs/1000,petg/1000,tecnico/1000))
        conn.commit()


def getDataMaterial(treematerial):
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        db_rows=cursor.execute("SELECT * FROM material")
        conn.commit()
        for row in db_rows:
            treematerial.insert('',0,text=row[1],values=(row[2],row[3], row[4]))

def deleteDataMaterial(treematerial):
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        cursor.execute("DELETE FROM material;",)
        conn.commit()




#=============================CALCULOS=================================================


def costoHora(tiempolote):
    with sqlite3.connect(db_name) as conn:
        cursora=conn.cursor()
        cursora.execute("SELECT costohorareal FROM costos")
        cursorb=conn.cursor()
        cursorb.execute("SELECT tiempo FROM lote")
        a=cursora.fetchall()
        b=cursorb.fetchall()
        costo_hora=tiempolote*a[0][0]
        print(costo_hora)
        return costo_hora

def costoMaterial(mat,pesolote):
    with sqlite3.connect(db_name) as conn:
        if mat=="PLA+":
            cursor=conn.cursor()
            cursor.execute("SELECT pla FROM material")
            pla=cursor.fetchall()
            costo_mat=pla[0][0]*pesolote

        elif mat=="ABS":
            cursor=conn.cursor()
            cursor.execute("SELECT abs FROM material")
            abs=cursor.fetchall()
            costo_mat=abs[0][0]*pesolote
        elif mat=="PETG":
            cursor=conn.cursor()
            cursor.execute("SELECT petg FROM material")
            petg=cursor.fetchall()
            costo_mat=petg[0][0]*pesolote
        elif mat=="TECNICO":
            cursor=conn.cursor()
            cursor.execute("SELECT tecnico FROM material")
            tecnico=cursor.fetchall()
            costo_mat=tecnico[0][0]*pesolote
    return costo_mat
