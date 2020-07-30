from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(5):
    r = random.randrange(2,8)
    if r==2:
        mc.setBlocks(x,y,z,x,y,z+4,1)
        z = z+4
    elif r==3:
        mc.setBlocks(x,y,z,x,y,z-4,1)
        z = z-4
    elif r==4:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x = x-4
    elif r==5:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x = x+4
    elif r==6:
        mc.setBlocks(x,y,z,x,y+4,z,1)
        y = y+4
    else:
        mc.setBlocks(x,y,z,x,y+4,z,1)
        y = y-4