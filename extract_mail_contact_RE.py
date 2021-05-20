import re

Source = "Hello my name is ninja and I am 100 years old. My conatct number is +911234567890 and my email is k2p1020@gmail.com"
print(Source)

print("=========Extracted Contact Number and Mail=========")
for i in re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', Source):
    print(i)
    
for i in re.findall('\S+@\S+', Source):
    print(i) 
