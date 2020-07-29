from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
time.sleep(2)
mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
time.sleep(2)
mc.setBlocks(x,y,z,x,y+4,z,17)