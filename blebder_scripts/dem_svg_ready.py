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


def _build_wall(location: list, width, pats):
    location = _location_scale_adjustmeny(location)
    print('l:', location)
    bpy.ops.archipack.wall2()
    bpy.context.active_object.location.x = location[0]
    bpy.context.active_object.location.y = location[1]
    o = bpy.context.active_object
    m = o.data
    prop = m.archipack_wall2[0]
    map = pats
    prop.width = width
    prop.n_parts = len(map)

    for i in enumerate(map):
        if 'l' in i[1]:
            prop.parts[i[0]].length = scale_adjustment(i[1].get('l'))
        if 'c' in i[1]:
            prop.parts[i[0]].a0 = math.radians(i[1].get('c'))
            if(i[1].get('c')) < 0:
                bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False))
                bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False))
    

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





apartment_map = [{'t': 'wall', 'l': [286.5, 889.3], 'w': 2, 'map': [{'l': 381.1, 'c': 0}]}, {'t': 'wall', 'l': [286.5, 672.1], 'w': 2, 'map': [{'l': 217.19999999999993, 'c': 90}]}, {'t': 'wall', 'l': [200.9, 672.1], 'w': 2, 'map': [{'l': 85.6, 'c': 0}]}, {'t': 'wall', 'l': [200.9, 368.9], 'w': 2, 'map': [{'l': 303.20000000000005, 'c': 90}]}, {'t': 'wall', 'l': [271.2, 269.4], 'w': 2, 'map': [{'l': 118.80000000000001, 'c': 0}]}, {'t': 'wall', 'l': [390.0, 47.5], 'w': 2, 'map': [{'l': 221.89999999999998, 'c': 90}]}, {'t': 'wall', 'l': [380.0, 47.5], 'w': 2, 'map': [{'l': 227.70000000000005, 'c': 0}]}, {'t': 'wall', 'l': [608.7, 37.4], 'w': 2, 'map': [{'l': 61.00000000000001, 'c': 90}]}, {'t': 'wall', 'l': [579.0, 95.4], 'w': 2, 'map': [{'l': 174.5, 'c': 0}]}, {'t': 'wall', 'l': [753.5, 85.6], 'w': 2, 'map': [{'l': 246.29999999999998, 'c': 90}]}, {'t': 'wall', 'l': [579.0, 322.1], 'w': 2, 'map': [{'l': 174.5, 'c': 0}]}, {'t': 'wall', 'l': [576.3, 95.4], 'w': 2, 'map': [{'l': 236.70000000000002, 'c': 90}]}, {'t': 'wall', 'l': [576.3, 329.3], 'w': 2, 'map': [{'l': 175.8, 'c': 90}]}, {'t': 'wall', 'l': [576.3, 505.1], 'w': 2, 'map': [{'l': 50.40000000000009, 'c': -135}]}, {'t': 'wall', 'l': [626.7, 552.1], 'w': 2, 'map': [{'l': 41.0, 'c': 0}]}, {'t': 'wall', 'l': [667.6, 542.0], 'w': 2, 'map': [{'l': 347.29999999999995, 'c': 90}]}, {'t': 'wall', 'l': [280.5, 270.8], 'w': 2, 'map': [{'l': 108.0, 'c': 90}]}, {'t': 'wall', 'l': [200.9, 368.9], 'w': 2, 'map': [{'l': 79.6, 'c': 0}]}, {'t': 'wall', 'l': [286.5, 667.4], 'w': 1, 'map': [{'l': 146.2, 'c': 0}]}, {'t': 'wall', 'l': [432.7, 475.1], 'w': 1, 'map': [{'l': 257.9, 'c': 90}]}, {'t': 'wall', 'l': [432.7, 475.1], 'w': 1, 'map': [{'l': 77.80000000000001, 'c': 0}]}, {'t': 'wall', 'l': [502.3, 247.7], 'w': 1, 'map': [{'l': 231.2, 'c': 90}]}, {'t': 'wall', 'l': [374.2, 405.2], 'w': 1, 'map': [{'l': 128.10000000000002, 'c': 0}]}, {'t': 'wall', 'l': [374.2, 373.9], 'w': 1, 'map': [{'l': 100.70000000000005, 'c': 90}]}, {'t': 'wall', 'l': [200.9, 474.1], 'w': 1, 'map': [{'l': 173.29999999999998, 'c': 0}]}, {'t': 'wall', 'l': [280.5, 373.9], 'w': 1, 'map': [{'l': 93.69999999999999, 'c': 0}]}, {'t': 'wall', 'l': [374.2, 273.2], 'w': 1, 'map': [{'l': 46.5, 'c': 90}]}, {'t': 'wall', 'l': [497.2, 246.7], 'w': 1, 'map': [{'l': 77.30000000000001, 'c': 0}]}]
for ob in apartment_map:
    if ob.get('t') == 'wall':
        _build_wall(ob.get('l'), ob.get('w'), ob.get('map')) 
    if ob.get('t') == 'door':
        _build_doors(ob.get('l'))


bpy.ops.object.select_by_type(type='MESH')
bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False))