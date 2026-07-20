import os
import re  
failed_attempts={}
pattern_ip = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

def readFile(n):
   for i in n:
       yield i

while True:
    file_input = input("Enter your path: ").strip()
    if os.path.isfile(file_input):
      with open(file_input) as f:
           for i in readFile(f):
             ip=re.findall(pattern_ip, i)
             if not ip :
               continue
             else:  
              if "Failed" in i:
                 ip_add = ip[0]
                 if ip_add not in failed_attempts:
                    failed_attempts[ip_add] = 1
                 else:
                  failed_attempts[ip_add] += 1
           print(failed_attempts)  
           break
           
    else:
        print("File not exist or Error in File ")
   