from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
time.sleep(5)
x,y,z=mc.player.getTilePos()
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z)