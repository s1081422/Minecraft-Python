from mcpi.minecraft import Minecraft
mc=Minecraft.create()
t=5
while t<10:
    mc.postToChat("hi")
    t=t+1  