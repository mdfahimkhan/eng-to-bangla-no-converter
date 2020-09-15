numerics = {'1':'১','2':'২',
            '3':'৩',
            '4':'৪',
            '5':'৫',
            '6':'৬',
            '7':'৭', '8':'৮','9':'৯','0':'০'
            }

#page no 90

input_no= input('Add no: ').__str__()
new = input_no.replace(',','')
alu = ""
for a in new:
       hala= numerics[a]
       alu= alu+hala
string = list(alu)

#for 7 digit
if len(string)==7:
       for i,j in enumerate([2,4]):
              string.insert(i+j, ",")
       print(''.join(string))
elif len(string)==6:
       for i,j in enumerate([1,3]):
              string.insert(i+j, ",")
       print(''.join(string))
elif len(string)==8:
       for i,j in enumerate([1,3,5]):
              string.insert(i+j, ",")
       print(''.join(string))
else:
       print('fuck u motherfucker')