import os
import sys
import helpers

helpers.printMe("Starting!")

mySet = {'Jerusalem', 'Tel-Aviv', 'Haifa', 'Hertzelia', 'Tel-Aviv'}
helpers.printMe(mySet)

# Phone:
adam_phone = helpers.phones(phoneVersion='4', phoneOS='iOS')
print('  #> Adam phone  is:   ', adam_phone)

# Location:
f = mySet.pop()
f = mySet.pop()
f = mySet.pop()
adam_location = helpers.locations(Lat='32.16203973676016', Long='34.81067665423914', City=f)
print('  #> Adam location is: ', adam_location)
