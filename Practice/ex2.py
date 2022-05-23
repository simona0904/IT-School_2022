
# Imparte un text in mai multe linii cu o maxima lungime:

def text_wrap(text: str, length: int) -> list[str]:                            
    if len(text) <= length:                                                    
        return [text,]                                                         
    lines: list[str] = []                                                      
    while True:                                                                
        index = length - 1                                                     
        while text[index] != ' ':                                              
            index -= 1                                                         
        lines.append(text[:index])                                             
        text = text[index + 1:]                                                
        if len(text) <= length:                                                
            lines.append(text)                                                 
            break
    return lines
        



