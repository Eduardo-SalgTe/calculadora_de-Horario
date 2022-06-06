import dbb

class MenuOP():
    
    tam = 0
    matTmp = []
    matAsig = ['']*7
    
    def __init__(self, op):
        if(op == 1):
            self.tam = int(input('numero de semestres: '))
            self.newReg(self.tam)
            self.tam = 0
        if(op == 2):
            self.serialAdd()
        if(op == 3):
            self.retModf()
        return
    
    def newReg(self, numS):
        dt = dbb.ConexionDDBB()
        for i in range(numS):
            cad = "s"
            cad += str(i+1)
            synt = "INSERT INTO semestre VALUES('{0}')".format(cad)
            dt.inssert(synt)
            cad = ''
        dt.close()
        self.matTmp = ([0]*numS)
        num = 0
        print('ingresar numero total de asignaturas del respectivo semestre.')
        for s in range(numS):
            num = int(input('Semestre{0}, numero de asignaturas: '.format(s+1)))
            self.matTmp[s] = num
        print('agregar asignaturas de cada semestre, presta cuidado\n')
        
        cad = ''
        for s in range(numS):
            print('\t\tSEMESTRE {0}'.format(s+1))
            
            for a in range(self.matTmp[s]):
                cad = 's' 
                cad += str(s+1)
                self.matAsig[0] = cad
                cad = input('nombre de la asignatura: ')
                self.matAsig[2] = cad
                ls = list(cad)
                cad = ls[0]
                cad += ls[1]
                cad += ls[2]
                self.matAsig[1] = cad
                cad = input('numero de creditos: ')
                self.matAsig[3] = cad
                cad = input('(a = aprovada) (r = reprovada) (nc = no cursado)')
                self.matAsig[4] = cad
                cad = ''
                self.abreb()
        return
        
    def serialAdd(self):
        mat = [''] * 4
        print('\t\tagregar asignaturas seriadas')
        while(True):
            mat[0] = input('La asignatura: ')
            mat[1] = input('del semestre: ')
            mat[2] = input('esta seriada con\n(asignatura): ')
            mat[3] = input('del semestre: ')
            print('[done]')
            if(mat[0] == mat[1] == mat[2] == mat[3] == ''):
                break
            else:
                self.destiSer(mat)
                mat = [''] * 4
    def retModf(self):
        
        pass
    
    
    
    
    def destiSer(self, arr):
        synt = "UPDATE reticula SET SERIADO = 'si', ASGFTHR = '{0}', SEMFTHR = '{1}' WHERE ID = '{2}' AND ABREBIACION = '{3}'".format(
            arr[2], arr[3], arr[1], arr[0])
        try:
            db = dbb.ConexionDDBB()
            db.update(synt)
            db.close()
        except:
            #db.close()
            print('[error] -> {reticula--destiSer}')
    
    def abreb(self):
        synt = 'INSERT INTO reticula (ID, ABREBIACION, ASIGNATURA, CREDITOS, CONTEXTO, SERIADO) VALUES ('
        synt += ("'{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
            self.matAsig[0], self.matAsig[1], self.matAsig[2], self.matAsig[3], self.matAsig[4], 'no'))
        dt = dbb.ConexionDDBB()
        dt.inssert(synt)
        self.matAsig = ['']*7
        dt.close()