from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
a=0
while True: a<20
    mc.setBlock(x-30,y-10,z,x=30,y+10,z,19)
    z=z-5
    a=a+1