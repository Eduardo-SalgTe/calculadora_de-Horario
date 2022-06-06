import reticula as ret
import schedule as sc

class Menu():
    print('Bienvenido al programa calculador de horarios')
    op = int(input('1 cargar reticula (en caso de que no este en DDBB)\n2 agregar series\n3 modificar historial\n4 calcular horario\n'))
    
    if (op > 0 and  op < 4):
        ret.MenuOP(op)
    elif (op == 4):
        op = int(input('1 cargar grupos\n2 buscar horario\n'))
        sc.initialPrm(op)
    