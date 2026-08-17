dict1 = {"python":10,"C++": 9,"Java":8,"HTML":7,"JS":6}
print(dict1) 
print(dict1.get("python","NOT FOUND"))
print(dict1.get("C#","NOT FOUND"))

key = {"tech","civil", "Public servant", "POPstar"}
value = [200,30,400,300]
dict2 = dict(zip(key,value))
print(dict2)  
print(dict2.pop("civil"))
print(dict2)
del dict2["tech"]
print(dict2)

dict3 = {"engineer":{"branch":"total 5 major's","scope":"can go to any field"},"MBA":["Business","Finance"],"Medical":"HEalthcare","Pharma":"Chemist"}
print(dict3)
print(dict3["engineer"])
print(dict3["engineer"]["scope"])
print(dict3["MBA"][0])
print(dict3["Pharma"])
print(dict3["Medical"])

