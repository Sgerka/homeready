import bpy
import math


def scale_adjustment(number: float) -> float:
    scale = 0.1
    pixel = 0.977
    return number * scale * pixel


def _location_scale_adjustmeny(location: list) -> list:
    for i in enumerate(location):
        location[i[0]] = scale_adjustment(i[1])
    return location


def _build_wall(location: list, pats):
    location = _location_scale_adjustmeny(location)
    print('l:', location)
    bpy.ops.archipack.wall2()
    bpy.context.active_object.location.x = location[0]
    bpy.context.active_object.location.y = location[1]
    o = bpy.context.active_object
    m = o.data
    prop = m.archipack_wall2[0]
    map = pats
    prop.n_parts = len(map)

    for i in enumerate(map):
        if 'l' in i[1]:
            prop.parts[i[0]].length = scale_adjustment(i[1].get('l'))
        if 'c' in i[1]:
            prop.parts[i[0]].a0 = math.radians(i[1].get('c'))


def _build_doors(location):
    _location_scale_adjustmeny(location)
    bpy.ops.archipack.door()
    bpy.context.active_object.location.x = location[0]
    bpy.context.active_object.location.y = location[1]


def _build_windows(location):
    _location_scale_adjustmeny(location)
    bpy.ops.archipack.window()
    bpy.context.active_object.location.x = location[0]
    bpy.context.active_object.location.y = location[1]

apartment_map = {
    "salon": [
        {
            't': 'wall',
            'l': [-873.5, -385.5],
            'map': [
                {'l': 725, 'c': 0},
                {'l': 167, 'c': 90},
            ]
        },
        {
            't': 'door',
            'l': [-144.8, -217]
        }, 
        
         {
            't': 'wall',
            'l': [-873.5, -385.5],
            'map': [
                {'l': 405, 'c': 90},
                {'l': 265, 'c': -90},
                {'l': 335, 'c': 90},
                {'l': 260, 'c': -90},
                {'l': 335, 'c': -90},
                {'l': 188, 'c': 90},
            ]
        }, 

          {
            't': 'wall',
            'l': [-873.5, -385.5],
            'map': [
                {'l': 405, 'c': 90},
                {'l': 265, 'c': -90},
                {'l': 335, 'c': 90},
                {'l': 260, 'c': -90},
                {'l': 335, 'c': -90},
                {'l': 188, 'c': 90},
            ]
        }, 
         {
            't': 'door',
            'l': [-160.5, 20]
        }, 
    ]
}

for room in apartment_map:
    for ob in apartment_map[room]:
        if ob.get('t') == 'wall':
            _build_wall(ob.get('l'), ob.get('map'))
        if ob.get('t') == 'door':
            _build_doors(ob.get('l'))
