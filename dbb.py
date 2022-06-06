import pymysql

class ConexionDDBB():
    def __init__(self):
        self.connection  = pymysql.connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'root007',
            db = 'schedule'
            )
        
        self.cursor = self.connection.cursor()
        print('conexion [ok]')
        
    def select(self, id, sintax):
        #sint = "SELECT nombre FROM gur WHERE curp = '{0}'"
        
        sql = sintax.format(id)
        
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            
            #print("nombre: {0}".format(user[0]))
            self.mat += {user[0]}   #nombre
            self.mat += {user[1]}   #apP
            self.mat += {user[2]}   #apM
            self.mat += {user[3]}   #edad
            
            self.mat += {user[4]}   #localidad
            self.mat += {user[5]}   #curp
            #self.mat += {user[6]}   #direccion
            self.mat += {user[6]}   #telefono
            #self.mat += {user[8]}   #mail
            #self.mat += {user[9]}   #tipo
            #self.mat += {user[10]}  #pass
            #self.mat += {user[11]}  #pass
            
        except Exception as e:
            print('ha ocurrido un error en consulta a base de datos [select]')
            #raise
    def selectONE(self, sintax):
        #sint = "SELECT nombre FROM gur WHERE curp = '{0}'"
        valor = ''
        nmb = 0
        
        try:
            self.cursor.execute(sintax)
            user = self.cursor.fetchone()
            nmb = (self.cursor.rowcount)
            valor = user[0]
            
        except Exception as e:
            print('ha ocurrido un error en consulta a base de datos [selectONE]')
            #raise
        return valor, nmb
    
    def slctRtnVal(self, sintax):
        #sint = "SELECT nombre FROM gur WHERE curp = '{0}'"
        
        try:
            self.cursor.execute(sintax)
            user = self.cursor.fetchone()
            valor = user[0]
            
        except Exception as e:
            print('ha ocurrido un error en consulta a base de datos [selectVal]')
            #raise
        return valor
    
    
    def select_allT(self, fils, syntx):
        arr = []
        
        for f in range(fils):
            arr.append(['']*10)
        
        try:
            self.cursor.execute(syntx)
            users = self.cursor.fetchall()
            cnt = 0
            for user in users:
                for y in range(10):
                    arr[cnt][y] = user[y]
                cnt += 1
                #arr.append(user[0]+user[1])
                #print('id: {0}, nombre: {1}\n'.format(user[0], user[1]))
            #for p in range(fils):
                #print(arr[p])
        except Exception as e:
            print('error')
            #raise
        return arr
    
    def select_all(self, fils, syntx):
        arr = []
        try:
            self.cursor.execute(syntx)
            users = self.cursor.fetchall()
            
            for user in users:
                arr.append(user[0]+user[1])
                #print('id: {0}, nombre: {1}\n'.format(user[0], user[1]))
            #for p in range(fils):
                #print(arr[p])
        except Exception as e:
            raise
        return arr
    def update(self, syntx):
        sql = syntx
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    def inssert(self, syntx):
        sql = syntx
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            self.close()
            raise
    def close(self):
        print('conexion [close]')
        self.connection.close()