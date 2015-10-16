import os
import sys

from minecraft_data.tools import convert


_dir = os.path.join(os.path.dirname(__file__),"../data/data/1.8")

for name, data in convert(_dir).items():
    setattr(sys.modules[__name__], name, data)
