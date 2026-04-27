from oopconcets.college import College
cc = int(input('C code: '))
cn = input(' C name: ')
ci = input('City: ')

project = College(ccode=cc, cname=cn, ccity=ci)

project.welocome_message()
project.display_college_details()