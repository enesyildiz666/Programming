import re

oldpassword = 'testing'

newpassword = input ('geef nieuwe ww testing: ')



if newpassword == oldpassword:
    print ('ww is al gebruikt')

elif len(newpassword) < 6:
    print ('niet genoeg letters')

elif re.search('[0-9]',newpassword) is None:
            print("moet nummer in anders is het false")

else:
    print ('nieuwe password werkt')





