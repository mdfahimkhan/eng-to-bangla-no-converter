numerics = {'1':'১','2':'২',
            '3':'৩',
            '4':'৪',
            '5':'৫',
            '6':'৬',
            '7':'৭', '8':'৮','9':'৯','0':'০'
            }



input_no= input('Add no: ').__str__()
new = input_no.replace(',','')
alu = ""
for a in new:
      hala= numerics[a]
      alu= alu+hala
print("Digit without comma: "+alu)
string = list(alu)


if len(string)==7:
      for i,j in enumerate([2,4]):
             string.insert(i+j, ",")
      print(''.join(string))
elif len(string)==3 or len(string)<3:
      print(''.join(string))
elif len(string)==4:
      for i,j in enumerate([1]):
             string.insert(i+j, ",")
      print(''.join(string))
elif len(string)==5:
      for i,j in enumerate([3]):
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
elif len(string)==9:
      for i,j in enumerate([2,4,6]):
             string.insert(i+j, ",")
      print(''.join(string))
elif len(string)==10:
      for i,j in enumerate([1,3,5,7]):
             string.insert(i+j, ",")
      print(''.join(string))
elif len(string)==11:
      for i,j in enumerate([2,4,6,8]):
             string.insert(i+j, ",")
      print(''.join(string))
else:
      print('Range crossed')
