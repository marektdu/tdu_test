# this is where the tests go to

import os
import sys


sys.path.insert(0,
                os.path.abspath(
                    os.path.join(os.path.dirname(__file__), '..',))
                )


from sample import bla


bla.print_something()
       
# Restaurant

### santity checks
## test for name
## test for adtres
## test for coords

# test get_cords
## test sufficant coordinates
## test coordinates with illeagal values

# more stuff