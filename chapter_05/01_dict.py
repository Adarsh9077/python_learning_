
# ! Dictionary data type


studentMarks = {
    "john" : 42,
    "sony":55,
    "sam":56,
    "rock":69
} 

print(studentMarks,type(studentMarks))


#? Properties in python 

#* It is Unordered
#* It is mutable
#* It is indexed
#* Cannot contains duplicate keys


print(studentMarks.items())
print(studentMarks.keys())
print(studentMarks.values())

studentMarks.update({"john":33,"sara":69})

print(studentMarks.items())


print(studentMarks.get("smith")) #! it return none 
#? print(studentMarks["smith"]) 
#! it return an error and stop the compilation  

#! 02:37:00