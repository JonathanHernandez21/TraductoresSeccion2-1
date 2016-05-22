def ValidaPass(contra):
    if contra.isalpha():
       return 'la contrasena es alfabetica' 
    elif contra.isdigit():
       return 'la contrasena es solo digitos' 
    else:
         'la contrasena es invalida' 

contra = raw_input('ingrese contrasena: ')
print ValidaPass(contra) 

      
