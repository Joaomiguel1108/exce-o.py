try:
    x = int(input("Digite um numero"))
    
    y= int(input("Digite outro numero:"))
    
    resultado = x/y
        
    

except ZeroDivisionError:
    
    print("Erro: não é possivel dividir por zero, lerdão!")
    
except ValueError:
    
    print("Erro: entrada invalida! por favor digite um numero")
    
else:
    print(f"o resultado é: {resultado}")
