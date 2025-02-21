piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
#            0   1    2    3    4    5    6    7
piano_tuple= ["do", "re", "mi", "fa", "so", "la", "ti"]

#Slicing also works on tuples

print(piano_keys[ 2:5 ])
print(piano_keys[ 2: ])
print(piano_keys[ :5 ])
print(piano_keys[ ::2 ])
print(piano_keys[ 2:5:2 ]) #last number is the no. of steps
print(piano_keys[ ::-1 ]) # Reverse the list