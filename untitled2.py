from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
     x,y,z = mc.player.getPos()
      mc.setBlock(x-1,y-1,z+1,8)