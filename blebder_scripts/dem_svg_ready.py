import bpy
import math


def scale_adjustment(number: float) -> float:
    scale = 0.01
    pixel = 1
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
    bpy.ops.archipack.generate_hole()
    bpy.context.active_object.location.x = location[0]
    bpy.context.active_object.location.y = location[1]







apartment_map = [{'t': 'wall', 'l': [102.5, 911.1], 'w': 0.2, 'h': 0.25, 'map': [{'l': 401.1, 'c': 0}]}, {'t': 'wall', 'l': [122.5, 703.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 217.20000000000005, 'c': 90}]}, {'t': 'wall', 'l': [16.9, 693.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 105.6, 'c': 0}]}, {'t': 'wall', 'l': [36.9, 391.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 312.7, 'c': 90}]}, {'t': 'wall', 'l': [96.5, 291.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 129.5, 'c': 0}]}, {'t': 'wall', 'l': [226.0, 79.3], 'w': 0.2, 'h': 0.25, 'map': [{'l': 221.89999999999998, 'c': 90}]}, {'t': 'wall', 'l': [206.0, 69.3], 'w': 0.2, 'h': 0.25, 'map': [{'l': 227.7, 'c': 0}]}, {'t': 'wall', 'l': [444.7, 69.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 61.0, 'c': 90}]}, {'t': 'wall', 'l': [405.0, 117.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 174.5, 'c': 0}]}, {'t': 'wall', 'l': [589.5, 117.4], 'w': 0.2, 'h': 0.25, 'map': [{'l': 246.29999999999998, 'c': 90}]}, {'t': 'wall', 'l': [405.0, 343.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 174.5, 'c': 0}]}, {'t': 'wall', 'l': [415.0, 117.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 246.7, 'c': 90}]}, {'t': 'wall', 'l': [415.0, 363.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 180.10000000000002, 'c': 90}]}, {'t': 'wall', 'l': [409.3710678118655, 529.8289321881346], 'w': 0.2, 'h': 0.25, 'map': [{'l': 71.06454812351937, 'c': -135}]}, {'t': 'wall', 'l': [444.8, 573.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 55.89999999999998, 'c': 0}]}, {'t': 'wall', 'l': [503.6, 573.8], 'w': 0.2, 'h': 0.25, 'map': [{'l': 347.30000000000007, 'c': 90}]}, {'t': 'wall', 'l': [116.5, 302.6], 'w': 0.2, 'h': 0.25, 'map': [{'l': 108.59999999999997, 'c': 90}]}, {'t': 'wall', 'l': [26.9, 391.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 79.6, 'c': 0}]}, {'t': 'wall', 'l': [121.5, 695.1], 'w': 0.1, 'h': 0.25, 'map': [{'l': 146.2, 'c': 0}]}, {'t': 'wall', 'l': [273.7, 508.3], 'w': 0.1, 'h': 0.25, 'map': [{'l': 256.40000000000003, 'c': 90}]}, {'t': 'wall', 'l': [263.7, 501.8], 'w': 0.1, 'h': 0.25, 'map': [{'l': 82.80000000000001, 'c': 0}]}, {'t': 'wall', 'l': [343.3, 279.4], 'w': 0.1, 'h': 0.25, 'map': [{'l': 231.20000000000005, 'c': 90}]}, {'t': 'wall', 'l': [210.2, 431.9], 'w': 0.1, 'h': 0.25, 'map': [{'l': 128.10000000000002, 'c': 0}]}, {'t': 'wall', 'l': [215.2, 401.3], 'w': 0.1, 'h': 0.25, 'map': [{'l': 109.5, 'c': 90}]}, {'t': 'wall', 'l': [215.2, 401.3], 'w': 0.1, 'h': 0.25, 'map': [{'l': 178.3028042404269, 'c': 0}]}, {'t': 'wall', 'l': [116.5, 401.2], 'w': 0.1, 'h': 0.25, 'map': [{'l': 98.6, 'c': 0}]}, {'t': 'wall', 'l': [226.0, 304.9], 'w': 0.1, 'h': 0.25, 'map': [{'l': 46.5, 'c': 90}]}, {'t': 'wall', 'l': [333.2, 273.4], 'w': 0.1, 'h': 0.25, 'map': [{'l': 77.30000000000001, 'c': 0}]}, {'t': 'wall', 'l': [206.8, 301.1], 'w': 0.1, 'h': 0.25, 'map': [{'l': 128.09999999999997, 'c': 0}]}, {'t': 'window', 'l': [315.3, 911.1]}, {'t': 'window', 'l': [160.6, 911.1]}, {'t': 'window', 'l': [48.5, 693.9]}, {'t': 'window', 'l': [50.7, 390.8]}, {'t': 'window', 'l': [116.4, 301.1]}, {'t': 'window', 'l': [225.8, 120.3]}, {'t': 'window', 'l': [279.8, 69.3]}, {'t': 'window', 'l': [517.7, 117.5]}]





























for ob in apartment_map:
    if ob.get('t') == 'wall':
        _build_wall(ob.get('l'), ob.get('w'), ob.get('map')) 
    if ob.get('t') == 'door':
        _build_doors(ob.get('l'))
    if ob.get('t') == 'window':
        _build_windows(ob.get('l'))


bpy.ops.object.select_by_type(type='MESH')
bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False))