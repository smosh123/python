import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

import time

while True:
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

block = 11

mc.setBlock(x, y, z, block)