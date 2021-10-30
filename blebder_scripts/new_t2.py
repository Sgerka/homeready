#THIS IS WORKING EXEMPLAR


import json
import math
import re
svg = {"name":"svg","type":"element","value":"","attributes":{"version":"1.1","id":"Layer_1","xmlns":"http://www.w3.org/2000/svg","xmlns:xlink":"http://www.w3.org/1999/xlink","x":"0px","y":"0px","viewBox":"0 0 1000 1000","style":"enable-background:new 0 0 1000 1000;","xml:space":"preserve"},"children":[{"name":"style","type":"element","value":"","attributes":{"type":"text/css"},"children":[{"name":"","type":"text","value":"\n\t.st0{fill:none;stroke:#000000;stroke-width:20;stroke-miterlimit:10;}\n\t.st1{fill:none;stroke:#000000;stroke-width:10;stroke-miterlimit:10;}\n\t.st2{fill:none;stroke:#1D71B8;stroke-width:20;stroke-miterlimit:10;}\n\t.st3{fill:none;stroke:#36A9E1;stroke-width:20;stroke-miterlimit:10;}\n\t.st4{fill:none;stroke:#2D2E83;stroke-width:20;stroke-miterlimit:10;}\n\t.st5{fill:none;stroke:#29235C;stroke-width:20;stroke-miterlimit:10;}\n\t.st6{fill:none;stroke:#662483;stroke-width:20;stroke-miterlimit:10;}\n\t.st7{fill:none;stroke:#E52421;stroke-width:20;stroke-miterlimit:10;}\n\t.st8{fill:none;stroke:#F39200;stroke-width:10;stroke-miterlimit:10;}\n\t.st9{fill:none;stroke:#E94E1B;stroke-width:20;stroke-miterlimit:10;}\n","attributes":{},"children":[]}]},{"name":"g","type":"element","value":"","attributes":{"id":"Outer_Walls"},"children":[{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"667.6","y1":"889.3","x2":"286.5","y2":"889.3"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"286.5","y1":"672.1","x2":"286.5","y2":"889.3"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"200.9","y1":"672.1","x2":"286.5","y2":"672.1"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"200.9","y1":"368.9","x2":"200.9","y2":"672.1"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"390","y1":"269.4","x2":"271.2","y2":"269.4"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"390","y1":"47.5","x2":"390","y2":"269.4"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"607.7","y1":"47.5","x2":"380","y2":"47.5"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"608.7","y1":"98.4","x2":"608.7","y2":"37.4"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"753.5","y1":"95.4","x2":"579","y2":"95.4"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"753.5","y1":"331.9","x2":"753.5","y2":"85.6"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"579","y1":"322.1","x2":"753.5","y2":"322.1"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"576.3","y1":"95.4","x2":"576.3","y2":"332.1"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"576.3","y1":"505.1","x2":"576.3","y2":"329.3"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"626.7","y1":"555.2","x2":"576.3","y2":"505.1"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"667.7","y1":"552.1","x2":"626.7","y2":"552.1"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"667.6","y1":"889.3","x2":"667.6","y2":"542"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"280.5","y1":"270.8","x2":"280.5","y2":"378.8"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"200.9","y1":"368.9","x2":"280.5","y2":"368.9"},"children":[]}]},{"name":"g","type":"element","value":"","attributes":{"id":"Inner_Walls"},"children":[{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"432.7","y1":"667.4","x2":"286.5","y2":"667.4"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"432.7","y1":"733","x2":"432.7","y2":"475.1"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"510.5","y1":"475.1","x2":"432.7","y2":"475.1"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"502.3","y1":"247.7","x2":"502.3","y2":"478.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"374.2","y1":"405.2","x2":"502.3","y2":"405.2"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"374.2","y1":"474.6","x2":"374.2","y2":"373.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"200.9","y1":"475.1","x2":"374.2","y2":"474.1"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"280.5","y1":"373.9","x2":"374.2","y2":"373.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"374.2","y1":"273.2","x2":"374.2","y2":"319.7"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"574.5","y1":"246.7","x2":"497.2","y2":"246.7"},"children":[]}]},{"name":"g","type":"element","value":"","attributes":{"id":"Windows"},"children":[{"name":"line","type":"element","value":"","attributes":{"class":"st2","x1":"479.5","y1":"889.3","x2":"657.8","y2":"889.3"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st3","x1":"324.8","y1":"889.3","x2":"387.7","y2":"889.3"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st3","x1":"212.7","y1":"672.1","x2":"274","y2":"672.1"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st4","x1":"214.9","y1":"368.9","x2":"254.9","y2":"368.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st5","x1":"280.6","y1":"279.3","x2":"280.6","y2":"358.8"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st3","x1":"390","y1":"98.4","x2":"390","y2":"178.7"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st3","x1":"444","y1":"47.5","x2":"524.2","y2":"47.5"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st6","x1":"681.9","y1":"95.6","x2":"741.8","y2":"95.6"},"children":[]}]},{"name":"g","type":"element","value":"","attributes":{"id":"Layer_5"},"children":[{"name":"line","type":"element","value":"","attributes":{"class":"st7","x1":"667.7","y1":"565.7","x2":"667.7","y2":"623.4"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st8","x1":"502.3","y1":"413.9","x2":"502.3","y2":"461.8"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st8","x1":"502.3","y1":"325","x2":"502.3","y2":"369.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st8","x1":"374.2","y1":"426.3","x2":"374.2","y2":"468.2"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st9","x1":"576.3","y1":"259.9","x2":"576.3","y2":"304.8"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st8","x1":"514.3","y1":"246.7","x2":"562.6","y2":"246.7"},"children":[]}]}]}



# print(svg)

map = []

for children in svg.get('children'):
    children_name = children.get('name')
    if children_name:
        if children_name == 'style':
            style = children.get('children')[0].get('value').replace('\n', '')
            style = re.compile(".st+?\d?\d").split(style)
            style_json = {}
            # for line in style:
            #     if line != '':
                    # print(line)
        if children_name == 'g':
            if children.get('attributes').get('id') == 'Inner_Walls' or children.get('attributes').get('id') == 'Outer_Walls':
                walls = children.get('children')
                for wall in walls:
                    if wall.get('name') == 'line':
                        atr = wall.get('attributes')
                        x1, x2, y1, y2 = float(atr.get('x1')), float(atr.get('x2')), float(atr.get('y1')), float(atr.get('y2'))
                        start_point = [min(x1, x2), min(y1, y2)]
                        angle = math.degrees(math.atan2(y2-y1, x2-x1))
                        lenth = abs(x1 - x2)
                        if y1 == y2:
                            angle = 0
                        if x1 == x2:
                            angle = 90
                            lenth = abs(y1 - y2)

                        w = 1 if children.get('attributes').get('id') == 'Inner_Walls' else 2

                        m = {}
                        m['t'] = 'wall'
                        m['l'] = start_point
                        m['w'] = w
                        m['h'] = 2.75
                        m['map'] = [{'l': lenth, 'c': angle}]
                        map.append(m)
print(map)


