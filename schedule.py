import dbb
    
class initialPrm():

    arrG = [''] * 10
    arrGp = []
    
    matW = []
    matR = []
    
    nGp = 0
    nGpsc = 0
    pCnt = 0
    
    def __init__(self, op):
        if(op == 1):
            self.loadGrp()
        if(op == 2):
            #self.srch()
            #self.cnt()
            self.matCrt()
            self.srch()
            
    def loadGrp(self):
        ntp = int(input('numero de grupos a ingresar: '))
        for x in range(ntp):
            self.arrG[0] = input('semestre: ')
            self.arrG[1] = input('grupo')
            nm = int(input('numero de asignaturas: '))
            cad = ''
            cad1 = ''
            for y in range(nm):
                self.arrG[2] = input('abrebiacion: ')
                tnm = int(input('numero de horas: '))
                self.arrG[3] = str(tnm)
                cnt = 0
                n1, n2 = 0, 0
                dif = 0
                arrn = [''] * 6
                ver = True
                while(ver):
                    cad = input('\t\tingresar horario\ndia: ')+'_'
                    cad1 = input('hora: ')
                    hr = list(cad1)
                    cad1 = (hr[0]+hr[1])
                    n1 = int(cad1)
                    cad1 = (hr[3]+hr[4])
                    n2 = int(cad1)
                    
                    dif = n2-n1
                    for pt in range(dif):
                        for pu in range(6):
                            if(arrn[pu] == ''):
                                arrn[pu] = cad+str(n1)+'-'+str(n1+1)
                                break
                        n1 += 1
                        if(n1 == n2):
                            break
                        
                    cnt += dif
                    if(cnt == (tnm)):
                        for snd in range(4, 10, 1):
                            self.arrG[snd] = arrn[snd-4]
                        ver = False
                self.db(self.arrG)
            
            
    def srch(self):
        comp = [0]*self.nGp
        
        indsec = 0
        
        for gF in range(self.nGp):
            con = 0
                        ##
            for z in range(self.nGp):
                comp[z] = 0
            comp[self.pCnt] = 1
                        ##
                        
            syntx = "SELECT ID, GRP, ABRB, NHORAS, H1, H2, H3, H4, H5, H6 FROM grupos WHERE ID = '{0}' AND GRP = '{1}'".format(
                self.arrGp[self.pCnt][0], self.arrGp[self.pCnt][1])
            dbc = dbb.ConexionDDBB()
            self.matW = dbc.select_allT(6, syntx)
            dbc.close()
                        ##
            vl = True      
            while(vl):
                        ##
                for y in range(self.nGp):
                    if(comp[y] == 0):
                        indsec = y
                        comp[y] = 1
                        self.llenarR(indsec)
                
                        self.fnl()
                        break
                    if(con == self.nGp):
                        vl = False
                    else:
                        con += 1
                        ##
                 
            self.pCnt += 1
            print(gF)
    def fnl(self):
                          
        vfr = vcr = vfw = vcw = True
        fr = fw = 0
        cr = cw = 4 
        while(vfr):
            cr = 4
            while(vcr):
                fw = 0
                if(self.matR[fr][cr] != ''):
                    while(vfw):
                        cw = 4
                        while(vcw):
                            #print('fr:{0}, cr:{1}, fw:{2}, cw:{3}'.format(fr, cr, fw, cw))
                            if(self.matW[fw][cw] != ''):
                                
                                if(self.matR[fr][cr] == self.matW[fw][cw]):
                                    vcr = vwf = vcw = False
                            cw += 1
                            if(cw >= 10):
                                cw = 4
                                break
                        fw += 1
                        if(fw >= len(self.matW)):
                            fw = 0
                            break
                cr += 1
                
                if(cr >= 10):
                    cr = 4
                    self.matW.append(self.matR[fr])
                    print('exito')
                    break
            print('W')
            for p in range(len(self.matW)):
                print(self.matW[p])
            fr += 1
            if(fr >= (self.nGpsc)):
                fr = 0
                break 
                    
        
        
    
    def llenarR(self, indsec):
                    #cntR_asig
        syntx = "SELECT ID FROM grupos WHERE ID = '{0}' AND GRP = '{1}'".format(
            self.arrGp[indsec][0], self.arrGp[indsec][1])
        dt = dbb.ConexionDDBB()
        cad, self.nGpsc = dt.selectONE(syntx)
        dt.close()
                    #R
        syntx = "SELECT ID, GRP, ABRB, NHORAS, H1, H2, H3, H4, H5, H6 FROM grupos WHERE ID = '{0}' AND GRP = '{1}'".format(
            self.arrGp[indsec][0], self.arrGp[indsec][1])
        dbc = dbb.ConexionDDBB()
        self.matR = dbc.select_allT(self.nGpsc, syntx)
        dbc.close()
    
    def matCrt(self):
        syntx = "SELECT ID, GRP FROM grupos GROUP BY ID,GRP"
        
        dbc = dbb.ConexionDDBB()
        cad, nmb = dbc.selectONE(syntx)
        dbc.close()
        #print('cad: {0}\tnmb: {1}'.format(cad, nmb))
        self.nGp = nmb
        
        syntx = "SELECT ID, GRP FROM grupos GROUP BY ID,GRP"
        
        dbc = dbb.ConexionDDBB()
        arr = dbc.select_all(nmb, syntx)
        dbc.close()
        
        ar2 = []
        for i in range(nmb):
            ar2.append(['']*2)
        for i in range(nmb):
            lst = list(arr[i])
            ar2[i][0] = ((lst[0][0])+(lst[1][0]))
            ar2[i][1] = lst[2][0]
        self.arrGp = ar2
        
    def db(self, arr):
        synt = "INSERT INTO grupos (ID, GRP, ABRB, NHORAS, H1, H2, H3, H4, H5, H6)"
        synt += "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}')".format(
            arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9])
        
        dtb = dbb.ConexionDDBB()
        
        dtb.inssert(synt)
        dtb.close()