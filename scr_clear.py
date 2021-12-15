import os
def clear():
   # for mac and linux
   if os.name == 'posix':
      os.system('clear')
   else:
      # for windows platfrom
      os.system('cls')
