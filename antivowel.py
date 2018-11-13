#this program will display all letters except vowels
def anti_vowel(text):
  i=0
  s=""
  while i<len(text):     
         if text[i] in "aeiouAEIOU":
             #s=s+text[i]
             pass
         else:
             s=s+text[i]
         i=i+1
  return s
st=str(input("Enter :"))
print("You entered : ",st)
print()
anti_vowel(st)
print(s)
