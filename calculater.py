def calculator(a, b, c) :                   
    if c == "+":           
        result = a+b        
    elif c == "-":         
        result = a-b        
    elif c == "/":        
        result = a/b        
    elif c == "*":         
        result = a*b       
    elif c == "%":         
        result = a%b     
    else:                 
        result = 0  
    return result        


print (calculator(10, 9,"-" ) )  
print (calculator(20, 9, "*"))     
print (calculator(13, 7, "/"))
print (calculator(16, 12, "%"))
  