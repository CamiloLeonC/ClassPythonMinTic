cad='sores'
i=0
k=4
while i<k:
  if cad[i]==cad[k]:
     pal=1
  else:
     pal=0
     break
  i=i+1
  k=k-1
if pal==1:
  print('es palindrome ',cad)
else:
  print('No es palindrome ',cad)