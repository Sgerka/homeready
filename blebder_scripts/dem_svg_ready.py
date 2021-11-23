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
    bpy.context.active_object.location.x = location[0]
    bpy.context.active_object.location.y = location[1]





apartment_map = [{'t': 'wall', 'l': [102.5, 911.1], 'w': 0.2, 'h': 0.25, 'map': [{'l': 401.1, 'c': 0}]}, {'t': 'wall', 'l': [122.5, 703.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 217.20000000000005, 'c': 90}]}, {'t': 'wall', 'l': [17.1, 693.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 103.9, 'c': 0}]}, {'t': 'wall', 'l': [36.9, 391.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 312.7, 'c': 90}]}, {'t': 'wall', 'l': [97.2, 291.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 127.49999999999999, 'c': 0}]}, {'t': 'wall', 'l': [226.0, 79.3], 'w': 0.2, 'h': 0.25, 'map': [{'l': 221.89999999999998, 'c': 90}]}, {'t': 'wall', 'l': [206.0, 69.3], 'w': 0.2, 'h': 0.25, 'map': [{'l': 227.7, 'c': 0}]}, {'t': 'wall', 'l': [444.7, 69.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 61.0, 'c': 90}]}, {'t': 'wall', 'l': [405.0, 117.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 174.5, 'c': 0}]}, {'t': 'wall', 'l': [589.5, 117.4], 'w': 0.2, 'h': 0.25, 'map': [{'l': 246.29999999999998, 'c': 90}]}, {'t': 'wall', 'l': [405.0, 343.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 174.5, 'c': 0}]}, {'t': 'wall', 'l': [415.0, 117.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 246.7, 'c': 90}]}, {'t': 'wall', 'l': [415.0, 363.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 180.10000000000002, 'c': 90}]}, {'t': 'wall', 'l': [409.3710678118655, 529.8289321881346], 'w': 0.2, 'h': 0.25, 'map': [{'l': 71.06454812351937, 'c': -135}]}, {'t': 'wall', 'l': [444.8, 573.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 55.89999999999998, 'c': 0}]}, {'t': 'wall', 'l': [503.6, 573.8], 'w': 0.2, 'h': 0.25, 'map': [{'l': 347.30000000000007, 'c': 90}]}, {'t': 'wall', 'l': [116.5, 302.6], 'w': 0.2, 'h': 0.25, 'map': [{'l': 108.0, 'c': 90}]}, {'t': 'wall', 'l': [26.9, 390.7], 'w': 0.2, 'h': 0.25, 'map': [{'l': 79.6, 'c': 0}]}, {'t': 'wall', 'l': [725.4, 911.1], 'w': 0.2, 'h': 0.25, 'map': [{'l': 401.1, 'c': 0}]}, {'t': 'wall', 'l': [1126.5, 703.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 217.20000000000005, 'c': 90}]}, {'t': 'wall', 'l': [1108.0, 693.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 103.90000000000009, 'c': 0}]}, {'t': 'wall', 'l': [1212.1, 391.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 312.7, 'c': 90}]}, {'t': 'wall', 'l': [1004.3, 291.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 127.5, 'c': 0}]}, {'t': 'wall', 'l': [1023.0, 79.3], 'w': 0.2, 'h': 0.25, 'map': [{'l': 221.89999999999998, 'c': 90}]}, {'t': 'wall', 'l': [795.3, 69.3], 'w': 0.2, 'h': 0.25, 'map': [{'l': 227.70000000000005, 'c': 0}]}, {'t': 'wall', 'l': [804.3, 69.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 61.0, 'c': 90}]}, {'t': 'wall', 'l': [649.5, 117.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 174.5, 'c': 0}]}, {'t': 'wall', 'l': [659.5, 117.4], 'w': 0.2, 'h': 0.25, 'map': [{'l': 246.29999999999998, 'c': 90}]}, {'t': 'wall', 'l': [649.5, 343.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 174.5, 'c': 0}]}, {'t': 'wall', 'l': [834.0, 117.2], 'w': 0.2, 'h': 0.25, 'map': [{'l': 246.7, 'c': 90}]}, {'t': 'wall', 'l': [834.0, 363.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 180.10000000000002, 'c': 90}]}, {'t': 'wall', 'l': [833.7710678118655, 543.9710678118655], 'w': 0.2, 'h': 0.25, 'map': [{'l': 71.06454812351944, 'c': 135}]}, {'t': 'wall', 'l': [728.3, 573.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 55.90000000000009, 'c': 0}]}, {'t': 'wall', 'l': [745.4, 573.8], 'w': 0.2, 'h': 0.25, 'map': [{'l': 347.30000000000007, 'c': 90}]}, {'t': 'wall', 'l': [1132.5, 302.6], 'w': 0.2, 'h': 0.25, 'map': [{'l': 108.0, 'c': 90}]}, {'t': 'wall', 'l': [1122.5, 390.7], 'w': 0.2, 'h': 0.25, 'map': [{'l': 79.59999999999991, 'c': 0}]}, {'t': 'wall', 'l': [102.5, 949.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 401.1, 'c': 0}]}, {'t': 'wall', 'l': [122.5, 959.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 217.19999999999993, 'c': 90}]}, {'t': 'wall', 'l': [17.1, 1167.1], 'w': 0.2, 'h': 0.25, 'map': [{'l': 103.9, 'c': 0}]}, {'t': 'wall', 'l': [36.9, 1177.1], 'w': 0.2, 'h': 0.25, 'map': [{'l': 312.70000000000005, 'c': 90}]}, {'t': 'wall', 'l': [97.2, 1569.8], 'w': 0.2, 'h': 0.25, 'map': [{'l': 127.49999999999999, 'c': 0}]}, {'t': 'wall', 'l': [226.0, 1579.8], 'w': 0.2, 'h': 0.25, 'map': [{'l': 221.9000000000001, 'c': 90}]}, {'t': 'wall', 'l': [206.0, 1791.7], 'w': 0.2, 'h': 0.25, 'map': [{'l': 227.7, 'c': 0}]}, {'t': 'wall', 'l': [444.7, 1750.8], 'w': 0.2, 'h': 0.25, 'map': [{'l': 61.0, 'c': 90}]}, {'t': 'wall', 'l': [405.0, 1743.8], 'w': 0.2, 'h': 0.25, 'map': [{'l': 174.5, 'c': 0}]}, {'t': 'wall', 'l': [589.5, 1517.3], 'w': 0.2, 'h': 0.25, 'map': [{'l': 246.29999999999995, 'c': 90}]}, {'t': 'wall', 'l': [405.0, 1517.1], 'w': 0.2, 'h': 0.25, 'map': [{'l': 174.5, 'c': 0}]}, {'t': 'wall', 'l': [415.0, 1517.1], 'w': 0.2, 'h': 0.25, 'map': [{'l': 246.70000000000005, 'c': 90}]}, {'t': 'wall', 'l': [415.0, 1337.0], 'w': 0.2, 'h': 0.25, 'map': [{'l': 180.0999999999999, 'c': 90}]}, {'t': 'wall', 'l': [459.77106781186546, 1301.0710678118655], 'w': 0.2, 'h': 0.25, 'map': [{'l': 71.06454812351929, 'c': -45}]}, {'t': 'wall', 'l': [444.8, 1287.1], 'w': 0.2, 'h': 0.25, 'map': [{'l': 55.89999999999998, 'c': 0}]}, {'t': 'wall', 'l': [503.6, 959.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 347.30000000000007, 'c': 90}]}, {'t': 'wall', 'l': [116.5, 1470.4], 'w': 0.2, 'h': 0.25, 'map': [{'l': 108.0, 'c': 90}]}, {'t': 'wall', 'l': [26.9, 1470.3], 'w': 0.2, 'h': 0.25, 'map': [{'l': 79.6, 'c': 0}]}, {'t': 'wall', 'l': [725.4, 949.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 401.1, 'c': 0}]}, {'t': 'wall', 'l': [1126.5, 959.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 217.19999999999993, 'c': 90}]}, {'t': 'wall', 'l': [1108.0, 1167.1], 'w': 0.2, 'h': 0.25, 'map': [{'l': 103.90000000000009, 'c': 0}]}, {'t': 'wall', 'l': [1212.1, 1177.1], 'w': 0.2, 'h': 0.25, 'map': [{'l': 312.70000000000005, 'c': 90}]}, {'t': 'wall', 'l': [1004.3, 1569.8], 'w': 0.2, 'h': 0.25, 'map': [{'l': 127.5, 'c': 0}]}, {'t': 'wall', 'l': [1023.0, 1579.8], 'w': 0.2, 'h': 0.25, 'map': [{'l': 221.9000000000001, 'c': 90}]}, {'t': 'wall', 'l': [795.3, 1791.7], 'w': 0.2, 'h': 0.25, 'map': [{'l': 227.70000000000005, 'c': 0}]}, {'t': 'wall', 'l': [804.3, 1750.8], 'w': 0.2, 'h': 0.25, 'map': [{'l': 61.0, 'c': 90}]}, {'t': 'wall', 'l': [649.5, 1743.8], 'w': 0.2, 'h': 0.25, 'map': [{'l': 174.5, 'c': 0}]}, {'t': 'wall', 'l': [659.5, 1517.3], 'w': 0.2, 'h': 0.25, 'map': [{'l': 246.29999999999995, 'c': 90}]}, {'t': 'wall', 'l': [649.5, 1517.1], 'w': 0.2, 'h': 0.25, 'map': [{'l': 174.5, 'c': 0}]}, {'t': 'wall', 'l': [834.0, 1517.1], 'w': 0.2, 'h': 0.25, 'map': [{'l': 246.70000000000005, 'c': 90}]}, {'t': 'wall', 'l': [834.0, 1337.0], 'w': 0.2, 'h': 0.25, 'map': [{'l': 180.0999999999999, 'c': 90}]}, {'t': 'wall', 'l': [783.3710678118655, 1286.9289321881345], 'w': 0.2, 'h': 0.25, 'map': [{'l': 71.06454812351937, 'c': 45}]}, {'t': 'wall', 'l': [728.3, 1287.1], 'w': 0.2, 'h': 0.25, 'map': [{'l': 55.90000000000009, 'c': 0}]}, {'t': 'wall', 'l': [745.4, 959.9], 'w': 0.2, 'h': 0.25, 'map': [{'l': 347.30000000000007, 'c': 90}]}, {'t': 'wall', 'l': [1132.5, 1470.4], 'w': 0.2, 'h': 0.25, 'map': [{'l': 108.0, 'c': 90}]}, {'t': 'wall', 'l': [1122.5, 1470.3], 'w': 0.2, 'h': 0.25, 'map': [{'l': 79.59999999999991, 'c': 0}]}]




























for ob in apartment_map:
    if ob.get('t') == 'wall':
        _build_wall(ob.get('l'), ob.get('w'), ob.get('map')) 
    if ob.get('t') == 'door':
        _build_doors(ob.get('l'))


bpy.ops.object.select_by_type(type='MESH')
bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False))