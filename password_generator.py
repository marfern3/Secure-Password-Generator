import string
import random 

def password_generator():
    try:
      longitud = int(input('Longitud de contraseña deseada:'))
      if longitud < 1:
        print("Error, la longitud debe ser mayor a 0")
        return
      incluir_mayusculas = (input('¿Quieres mayúsculas en tu contraseña? (y/n)')).strip().lower() == 'y'
      incluir_minusculas = (input('¿Quieres minusculas en tu contraseña? (y/n)')).strip().lower() == 'y'
      incluir_numeros = (input('¿Quieres números en tu contraseña? (y/n)')).strip().lower() == 'y'
      incluir_especiales = (input('¿Quieres caracteres especiales en tu contraseña? (y/n)')).strip().lower() == 'y'
      
      caracteres = ""
      
      if incluir_mayusculas:
        caracteres += string.ascii_uppercase

      if incluir_minusculas:
        caracteres += string.ascii_lowercase

      if incluir_numeros:
        caracteres += string.digits

      if incluir_especiales:
        caracteres += string.punctuation

      if not caracteres:
        print("Error: selecciona un tipo de caracter")
        return
        
      password =  "".join(random.choice(caracteres) for _ in range (longitud))

      print("\n La contraseña generada es:", password)
      return password
    
    except ValueError:
        print ("Error: Ingresa un número valido para la longitud")

password_generator()
