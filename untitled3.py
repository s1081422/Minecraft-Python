from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange
for i in range(10):
    x,y,z = mc.player.getTilePos()
    x = x+i
    for i in range(10):
        color = randrange(0,16)
        z = z+1
        mc.setBlock(x,y,z,35,color)
ans = randrange(0,16)
t=0
while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if data==ans:
            mc.postToChat("good")
            mc.setBlock(hit.pos,57)
            break
        elif data<ans:
             mc.postToChat("big")
        elif data>ans:
             mc.postToChat("small")
        t = t+1
        if t>5:
            mc.postToChat("run!!!!!!")
            x,y,z = mc.player.getTilePos()
            mc.createExplosion(x,y,z)
            
            
            