#!/usr/bin/python
import math

class fecha():
    """counter."""
    def __init__(self, dia, mes, ano):
        self.dia=dia
        self.mes=mes
        self.ano=ano

    def dia(self):
        return self.dia

    def mes(self):
        return self.mes

    def ano(self):
        return self.ano

    def mesL(self):
        if self.mes==1:
            return "enero"
        elif self.mes==2:
            return "febrero"
        elif self.mes==3:
            return "marzo"
        elif self.mes==4:
            return "abril"
        elif self.mes==5:
            return "mayo"
        elif self.mes==6:
            return "junio"
        elif self.mes==7:
            return "julio"
        elif self.mes==8:
            return "agosto"
        elif self.mes==9:
            return "septiembre"
        elif self.mes==10:
            return "octubre"
        elif self.mes==11:
            return "noviembre"
        else:
            return "diciembre"

    def compare(self, other):
        if self.ano > other.ano:
            print("la fecha " + a.toString() + " esta despues de " + other.toString())
            return ""
        elif self.ano<other.ano:
            print("la fecha " + a.toString() + " esta antes de " + other.toString())
            return""

        if  self.mes>other.mes:
            print("la fecha " + a.toString() + " esta despues de " + other.toString())
            return ""
        elif self.mes<other.mes:
            print("la fecha " + a.toString() + " esta antes de " + other.toString())
            return""

        if  self.dia>other.dia:
            print("la fecha " + a.toString() + " esta despues de " + other.toString())
            return ""
        elif self.dia<other.dia:
            print("la fecha " + a.toString() + " esta antes de " + other.toString())
            return""

        print("la fecha " + a.toString() + " es igual a " + other.toString())
        return""

    def toString(self):
        return (str(self.dia)+ " de "+ self.mesL()+ " de "+str(self.ano))

a= fecha(1, 3, 2017)
b=fecha(1, 3, 2017)
print(a.compare(b))



class Punto2D():
    """Representacion de punto en 2 dimenciones"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def radio_polar(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def angulo_polar(self):
        return math.atan(float(self.y) / float(self.x))

    def dist_euclidiana(self, other):
        a = other.get_x() - self.x
        b = other.get_y() - self.y
        return math.sqrt(a * a + b * b)


r = Punto2D(10, 20)
d = Punto2D(0, 0)
print(r.get_x(), r.get_y(), r.radio_polar(), r.angulo_polar(), "la distancia euclidiana desde el punto (", r.get_x(),
      ",", r.get_y(), ")", " hasta el punto (", d.get_x(), ",", d.get_y(), ") es: ", r.dist_euclidiana(d))
