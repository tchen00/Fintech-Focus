def caesar(input, shift):
    output = [] 

    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for letter in input: 
        if letter in upper: 
            index = upper.index(letter)
            new = (index + shift) % 26
            newLetter = upper[new]
            output.append(newLetter)
        elif letter in lower: 
            index = lower.index(letter)
            new = (index + shift) % 26
            newLetter = lower[new]
            output.append(newLetter)
   
    text = ""
    for i in output: 
        text += i
    
    return text 

print(caesar("cat",1))



