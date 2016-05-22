import  re

def ValidaTecla(Tecla):
    if re.search('[a-z], Tecla'):
        return 'Solo se requiere letras' 
    elif Tecla.isalnum():
        return 'Solo se requiere letras y numeros' 
    else:
        return 'Caracteres  aceptados' 

Teclado = raw_input('ingrese los caracteres: ') 
print  ValidaTecla(Teclado) 