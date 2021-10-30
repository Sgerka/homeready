import bpy
import math


def scale_adjustment(number):
    scale = 0.1
    pixel = 0.977
    return number * scale * pixel
     

bpy.ops.archipack.wall2()
o = bpy.context.active_object.location[0] = scale_adjustment(-873) # 0 -> X
o = bpy.context.active_object.location[1] = scale_adjustment(-382.5) # 1 -> Y
o = bpy.context.active_object
m = o.data

prop = m.archipack_wall2[0] 


map = [
    {'l': 725, 'c': 0},
    {'l': 167, 'c': 90},
    {'l': 156, 'c': -90},
     {'l': 122},
     {'l': 375, 'c': -90},
     {'l': 274, 'c': -90},
     {'l': 370, 'c': 90},
     {'l': 480, 'c': 90},
     {'l': 380, 'c': 90}
]
prop.n_parts = len(map)

for i in enumerate(map):
    if 'l' in i[1]:
        prop.parts[i[0]].length = scale_adjustment(i[1].get('l'))
    if 'c' in i[1]:
        prop.parts[i[0]].a0 =  math.radians(i[1].get('c'))
  
dist = scale_adjustment(95)
bpy.ops.archipack.wall2()
o = bpy.context.active_object.location[0] = scale_adjustment(-215) # Y + len of second
o = bpy.context.active_object.location[1] = scale_adjustment(-148) + dist # X + len of first
o = bpy.context.active_object
m = o.data
       


maps = [
   {'l': 725},
   {'l': 167, 'c': -90},
   
]
prop.n_parts = len(maps)

for i in enumerate(maps):
   if 'l' in i[1]:
       prop.parts[i[0]].length = scale_adjustment(i[1].get('l'))
   if 'c' in i[1]:
       prop.parts[i[0]].a0 =  math.radians(i[1].get('c'))
       
       
       
dist = scale_adjustment(95)














import bpy




def create_custom_mesh(objname, px, py, pz):
 
    # Define arrays for holding data    
    myvertex = []
    myfaces = []

    # Create all Vertices

    # vertex 0
    mypoint = [(-1.0, -1.0, 0.0)]
    myvertex.extend(mypoint)

    # vertex 1
    mypoint = [(1.0, -1.0, 0.0)]
    myvertex.extend(mypoint)

    # vertex 2
    mypoint = [(-1.0, 1.0, 0.0)]
    myvertex.extend(mypoint)

    # vertex 3
    mypoint = [(1.0, 1.0, 0.0)]
    myvertex.extend(mypoint)

    # -------------------------------------
    # Create all Faces
    # -------------------------------------
    myface = [(0, 1, 3, 2)]
    myfaces.extend(myface)

    
    mymesh = bpy.data.meshes.new(objname)

    myobject = bpy.data.objects.new(objname, mymesh)

    bpy.context.scene.collection.objects.link(myobject)
    
    # Generate mesh data
    mymesh.from_pydata(myvertex, [], myfaces)
    # Calculate the edges
    mymesh.update(calc_edges=True)

    # Set Location
    myobject.location.x = px
    myobject.location.y = py
    myobject.location.z = pz

    return myobject

curloc = bpy.context.scene.cursor.location

create_custom_mesh("Awesome_object", curloc[0], curloc[1], 0)