from mcpi.minecraft import Minecraft
mc=Minecraft.create()
mc.postToChat("I'm watching you.")
while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("You are located on x:"+str(x)
                                  +", y:"+str(y)
                                  +", z:"+str(z))