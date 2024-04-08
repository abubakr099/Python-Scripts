#String build in Methods/Functions
"""
message = "corona Vaccine is ready to use and most of  90% effective"
print(message)
print(message.capitalize())
Message = message.capitalize()
print(Message)
print(message.upper())
print(message.islower())
print(message.isupper())
print(message.find("ready"))
print(message[18:24])
"""
"""
# dir() function
print(dir(""))
print(dir([]))
print(dir(()))
print(dir({}))
"""
"""
seq1 = ("192","168","40","90")
print(".".join(seq1))
print("/".join(seq1))
print("-".join(seq1))
"""
"""
mountains = ["Mount Everest" , "K2","Himalya","Nangaparpad","Mt Hood"]
print(mountains)
mountains.append("orgen mountain")
print(mountains)
mountains.extend(["abcd","efgh","ijklmno"])
print(mountains)
mountains.insert(2,"mt abu")
print(mountains)
mountains.pop()
print(mountains)
mountains.pop(5)
print(mountains)
"""
cntr_emp1 = {"Name":"Santa","skills":"Blockchain","code":1024}
print(cntr_emp1.keys())
print(cntr_emp1.values())
cntr_emp1.clear()
print(cntr_emp1)
cntr_emp1.pop()
print(cntr_emp1)
