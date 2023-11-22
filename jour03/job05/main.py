def calcule(num1,operator,num2):
    
    if operator == "+":
        result = num1 + num2
        
    elif operator == "-":
        result = num1 - num2
        
    elif operator == "*":
        result = num1 * num2
    
    elif operator == "/":
        result = num1 / num2
    
    elif operator == "%":
        result = num1 % num2
        
    return(f"resultat de {num1}{operator} {num2} est {result}")
    
print(calcule(10,"+",12))
print(calcule(10,"*",15))
print(calcule(10,"-",15))
print(calcule(10,"/",5))
print(calcule(10,"%",12))




        