print('modificado desde alumno')

class Pedido:
    def __init__(self,nombre_cliente,cant_pizzas,tamaño,variedad,fecha,hora):
        self.nombre_cliente = nombre_cliente
        self.cant_pizzas = cant_pizzas
        self.tamaño = tamaño
        self.variedad = variedad
        self.fecha = fecha
        self.hora = hora

    def decir_cliente (self):
        return self.nombre_cliente
    
    def decir_cantidad (self):
        return self.cant_pizzas

    def decir_tamaño (self):
        return self.tamaño
    
    def decir_variedad (self):
        return self.variedad
    
    def decir_fecha (self):
        return self.fecha
    
    def precio (self):
        if self.tamaño == 8:
            if self.variedad  == "muzzarella":
                return 350
            elif self.variedad  == "fugazeta":
                return 400
            else:
                return 450
        elif self.tamaño == 10:
            if self.variedad == "muzzarella":
                return 400
            elif self.variedad  == "fugazeta":
                return 450
            else:
                return 500
        else:
            if self.variedad  == "muzzarella":
                return 450
            elif self.variedad  == "fugazeta":
                return 50
            else:
                return 550

    def precio_total (self):
        return self.cant_pizzas*self.precio()
    
    def decir_entrega_demora (self):
        if self.verificar_hora():
            primero = int (self.hora[0:2])
            segundo = int (self.hora[3:5]) + 30
            if segundo >= 60:
                segundo=segundo-60
                primero=primero+1
            return f"la entrega es {primero}:{segundo} con una posible demora mas o menos de 10 minutos"

    def factura (self):
        print (f"El Sr. {self.decir_cliente()} pide {self.decir_cantidad()} de {self.decir_variedad()}")
        print (f"fecha: {self.decir_fecha()}/ a la hora: {self.decir_hora()}")
        print (f"precio total ${self.precio_total()}")
        print (self.decir_entrega_demora())

    def decir_hora (self):
        if self.verificar_hora():
            hr = int (self.hora[0:2])
            min = int (self.hora[3:5])
            return f"{hr}:{min}"
    
    def verificar_hora (self):
        primero = int (self.hora[0:2])
        segundo = int (self.hora[3:5])
        if primero>=0 and primero<=24:
            if segundo>=0 and segundo<60:
                return True




