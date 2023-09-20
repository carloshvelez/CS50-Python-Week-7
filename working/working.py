import re
import sys

def main():
    print(convert(input("Hours: ")))



def convert(s):
#Función para convertir a horario militar.
    #1. Buscar patrón para identificar si tiene el formato AM, PM.
    if hora := re.search(r"^(\d{1,2}):?(\d{1,2})?\s(AM|PM)\sto\s(\d{1,2}):?(\d{1,2})?\s(AM|PM)$", s):
        hora1 = int(hora.group(1))
        minutos1 = hora.group(2)
        if minutos1 is None:
            minutos1 = 0
        minutos1 = int(minutos1)
        meridiano1 = hora.group(3)
        hora2 = int(hora.group(4))
        minutos2 = hora.group(5)
        if minutos2 is None:
            minutos2 = 0
        minutos2 = int(minutos2)
        meridiano2 = hora.group(6)


        if hora1 > 12 or hora2 > 12 or minutos1 >= 60 or minutos2 >= 60:
            raise ValueError("Formato de Hora incorrecto")

        if meridiano1 == "PM" and hora1 != 12:
            hora1 += 12

        if meridiano2 == "PM" and hora2 != 12:
            hora2 += 12

        if meridiano1 == "AM" and hora1 == 12:
            hora1 = 0

        if meridiano2 == "AM" and hora2 == 12:
            hora2 = 0

        return f"{hora1:02d}:{minutos1:02d} to {hora2:02d}:{minutos2:02d}"



    #2. Si no tiene el formato correcto de 12 horas, arrojar error.
    else:
        raise ValueError("Formato de Hora incorrecto")

    #3. Si las horas y minutos se salen del rango esperado, arrojar error.
    #4. Retornar la hora en formato 24. Es decir, si fue AM, las horas se dejan igual, pero si fue PM, se le suman 12.







if __name__ == "__main__":
    main()