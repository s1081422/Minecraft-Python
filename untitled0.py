from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
mc.setBlock(x,y,z,x+20,y+20,z+20,1)
mc.setBlock(x+1,y+1,z+1,x+19,y+19,z+19,0)

