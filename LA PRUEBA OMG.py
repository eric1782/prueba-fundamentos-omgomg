#Calculadora de liquidacion de sueldo
w=1
while w == 1:
    print("Bienvenido")
    nombre=input("porfavor, ingresa tu nombre: ")
    if nombre and len(nombre)<30:
        sueldo_base= int(input("ingrese su sueldo base: "))
        horas_extra= int(input("ingrese las horas extras trabajadas en el mes: "))
        #horas si o si trabajadas serian de 180, por eso no se pregunta, y porque las instrucciones de la prueba dice que se pregunte por horas extra noma (escribo esto pa q no me rete pipipi)
        if sueldo_base >= 0 and horas_extra >= 0:
            Sueldo_x_Hora = sueldo_base/180
            Sueldo_x_Hora_Extra= int(Sueldo_x_Hora*1.5)
            pago_hora_extra = horas_extra*(Sueldo_x_Hora*1.5)
            total_ingresos = int(sueldo_base+pago_hora_extra)
            descuento_fonasa = (total_ingresos*7)/100
            descuento_AFP = (total_ingresos*10)/100
            descuento_total_malditos= int(descuento_AFP+descuento_fonasa)
            sueldo_neto = int(total_ingresos-descuento_AFP-descuento_fonasa)
            print("Desglose liquidacion:")
            print(f"nombre trabajador: {nombre}")
            print(f"sueldo base: {sueldo_base}")
            print(f"pago por hora extra: {Sueldo_x_Hora_Extra}")
            print(f"total de ingresos: {total_ingresos}")
            print(f"descuento seguridad social (fonasa + AFP): {descuento_total_malditos}")
            print(f"sueldo neto: {sueldo_neto}")
        else:
            print("porfavor ingresa sueldo y horas extras validos, no se permiten numeros negativos o decimales")
    else:
        print("nombre ingresado no valido, porfavor ingresa un nombre no mas largo de 30 caracteres.")
    
    f= open(f"liquidacion_{nombre}","w")
    f.writelines(f"nombre: {nombre}\nsueldo base: {sueldo_base}\npago por hora extra: {Sueldo_x_Hora_Extra}\ntotal de ingresos: {total_ingresos}\ndescuento seguridad social (fonasa + AFP): {descuento_total_malditos}\nsueldo neto: {sueldo_neto}")
    f.close()


#horas si o si trabajadas serian de 180, por eso no se pregunta, y porque las instrucciones de la prueba dice que se pregunte por horas extra noma (escribo esto pa q no me rete pipipi)
