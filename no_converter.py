numerics = {'1':'১','2':'২',
            '3':'৩',
            '4':'৪',
            '5':'৫',
            '6':'৬',
            '7':'৭', '8':'৮','9':'৯','0':'০'
            }



inputt=(input('Add no: '))
input_number_string = inputt.__str__()
new = inputt.replace(',','')
new_num = int(new)
new_str = new_num.__str__()


alu = ""
for a in new_str:
      hala= numerics[a]
      alu= alu+hala
print("Digit without comma: "+alu)
print ("Digit with comma: ")
string = list(alu)
numerical_range = []

if (len(string)%2)!=0:
      for a in range(2, len(string)-2,2):
             numerical_range.append(a)
      for i,j in enumerate(numerical_range):
             string.insert(i+j, ",")
      print(''.join(string))
elif (len(string)%2)==0:
      for b in range(1,len(string)-2,2):
             numerical_range.append(b)
      for i,j in enumerate(numerical_range):
             string.insert(i+j, ",")
      print(''.join(string))
else:
      print('sorry')
