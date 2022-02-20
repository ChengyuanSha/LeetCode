



def romanToInt(s: str) -> int:
   dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
   i = 0
   num = 0
   while i < len(s):
      special = False
      if (i + 1) < len(s):
         if s[i] == "I" and s[i + 1] == "V":
            num += 4
            special = True
         if s[i] == "I" and s[i + 1] == "X":
            num += 9
            special = True
         if s[i] == "X" and s[i + 1] == "L":
            num += 40
            special = True
         if s[i] == "X" and s[i + 1] == "C":
            num += 90
            special = True
         if s[i] == "C" and s[i + 1] == "D":
            num += 400
            special = True
         if s[i] == "C" and s[i + 1] == "M":
            num += 900
            special = True
         if special == True:
            i += 2
      if (i + 1) < len(s) and special == False:
         num += dic[s[i]]
      i += 1

   return num




romanToInt("MCMXCIV")