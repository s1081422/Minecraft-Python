from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getPos()
    a=mc.getBlock(x-1,y-1,z)
    b=mc.getBlock(x+1,y-1,z)
    c=mc.getBlock(x,y-1,z-1)
    d=mc.getBlock(x,y-1,z+1)
    if a==8 or b==8 or c==8 or d==8:
         mc.setBlock(x-1,y-1,z-1,x+1,y-1,z+1,38)
    

    