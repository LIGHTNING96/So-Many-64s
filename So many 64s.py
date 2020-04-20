import base64
from io import open
### coded by Mr.Lightning96 && Demon1 ###
#we are the best friends
print("""
       ___                                _  _          __     _ _        
      / __| ___        _ __   __ _  _ _  | || |        / /    | | |    ___
      \__ \/ _ \      | '  \ / _` || ' \  \_. |       / _ \   |_  _|  (_-/
      |___/\___/      |_|_|_|\__/_||_||_| |__/        \___/     |_|   /__/
      
challenge in ctf-learn
coded by
https://github.com/DEMON1A [Demon1] 
facebook.com/xcberlin {Mr. Lightning}
""")
count = 0
with open("the ctf.txt",encoding='utf-8') as f:
    ctext = f.read()

while True:
  count += 1
  ctext=base64.b64decode(ctext)
  if "ABCTF" in str(ctext):
      print(ctext.decode("utf-8"))
      print(str("Number Of Decodes: {0}").format(count))
      input("Enter To Exit....")
      break
      
ctf = open("FLAG.txt" ,"w")
ctf= open("FLAG.txt", "a")
ctf.write(str(ctext.decode("utf-8")))
ctf.close()

