
#! Set 


a = set()

a.add(69)
a.add(690)
a.add(169)
a.add(629)
a.add(639)
a.add(694)
a.add(659)

print(type(a),a)



#? Properties of set 

#* 1. Sets are unordered 
#* 2. Sets are un-indexed
#* 3. There is no way to change items in sets
#* 4. Sets cannot contains duplicate values



print(len(a))
s = a.remove(69)
s2 = a.pop()
print(s)
print(s2)

#! 03:09:40