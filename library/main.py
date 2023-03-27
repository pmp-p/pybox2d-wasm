import sys
import asyncio
import pygame
try:
    import i18n
    import pygame_gui
except:
    shell = None

import os
import Box2D

if sys.argv[-1].find("Box2D")>=0:
    arg = sys.argv[-1]
else:
    arg = "Box2D/examples/pinball.py"

print(arg)

exec( open(arg).read() )

