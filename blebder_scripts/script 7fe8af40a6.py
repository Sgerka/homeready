import bpy
import math

def scale_adjustment(number):
    scale = 0.1
    pixel = 0.977
    return number * scale * pixel
     

#bpy.ops.archipack.wall2()
#o = bpy.context.active_object.location[0] = scale_adjustment(-873) # 0 -> X
#o = bpy.context.active_object.location[1] = scale_adjustment(-382.5) # 1 -> Y
#o = bpy.context.active_object
#m = o.data

##prop = m.active_object

#print(m)


bpy.ops.archipack.door()
bpy.context.active_object.location.x = scale_adjustment(0) # 0 -> X
bpy.context.active_object.location.y = scale_adjustment(0) 




bpy.ops.archipack.window()
bpy.context.active_object.location.x = scale_adjustment(10) # 0 -> X
bpy.context.active_object.location.y = scale_adjustment(10) 

