# this is where the tests go to

import os
import sys


sys.path.insert(0,
                os.path.abspath(
                    os.path.join(os.path.dirname(__file__), '..',))
                )


from sample import bla


bla.print_something()
       
