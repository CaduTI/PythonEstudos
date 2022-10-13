#add,update, clear, discard
#union ou |
#intersection &(todos os elementos presentes em dois sets
#difference- diferença entre dois sets
#symmetric_differenc^ (elementos que estão nos dois sets, mas n em ambos
s1 = {1,2,3,4}
s2 = {1,2,4,68,9,7,6}
s3 = s1 | s2
s4 = s2 - s1
s5 = s1 ^ s2

print(f'Union: {s3}')
print(f'difference: {s4}')
print(f'Symmetric: {s5}')