import json
import math
import re
svg = {"name":"svg","type":"element","value":"","attributes":{"version":"1.1","id":"Layer_2","xmlns":"http://www.w3.org/2000/svg","xmlns:xlink":"http://www.w3.org/1999/xlink","x":"0px","y":"0px","viewBox":"0 0 1272.1 1000","style":"enable-background:new 0 0 1272.1 1000;","xml:space":"preserve"},"children":[{"name":"style","type":"element","value":"","attributes":{"type":"text/css"},"children":[{"name":"","type":"text","value":"\n\t.st0{fill:none;stroke:#000000;stroke-width:20;stroke-miterlimit:10;}\n\t.st1{fill:none;stroke:#000000;stroke-width:10;stroke-miterlimit:10;}\n\t.st2{fill:none;stroke:#FF008C;stroke-width:20;stroke-miterlimit:10;}\n","attributes":{},"children":[]}]},{"name":"g","type":"element","value":"","attributes":{"id":"Outer_Walls"},"children":[{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"513.6","y1":"911.1","x2":"112.5","y2":"911.1"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"122.5","y1":"693.9","x2":"122.5","y2":"911.1"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"26.9","y1":"693.9","x2":"132.5","y2":"693.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"36.9","y1":"381.2","x2":"36.9","y2":"693.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"236","y1":"291.2","x2":"106.5","y2":"291.2"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"226","y1":"69.3","x2":"226","y2":"291.2"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"443.7","y1":"69.3","x2":"216","y2":"69.3"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"444.7","y1":"120.2","x2":"444.7","y2":"59.2"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"589.5","y1":"117.2","x2":"415","y2":"117.2"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"589.5","y1":"353.7","x2":"589.5","y2":"107.4"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"415","y1":"343.9","x2":"589.5","y2":"343.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"415","y1":"107.2","x2":"415","y2":"353.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"415","y1":"534","x2":"415","y2":"353.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"462.7","y1":"577","x2":"412.3","y2":"526.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"510.7","y1":"573.9","x2":"454.8","y2":"573.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"503.6","y1":"911.1","x2":"503.6","y2":"563.8"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"116.5","y1":"292.6","x2":"116.5","y2":"401.2"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st0","x1":"36.9","y1":"391.2","x2":"116.5","y2":"391.2"},"children":[]}]},{"name":"g","type":"element","value":"","attributes":{"id":"Inner_Walls"},"children":[{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"266.8","y1":"763.7","x2":"266.8","y2":"496"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"346.6","y1":"501","x2":"266.8","y2":"501"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"338.5","y1":"501","x2":"338.5","y2":"262.8"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"415","y1":"266.4","x2":"333.4","y2":"266.4"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"232.7","y1":"296.2","x2":"338.5","y2":"296.2"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"270.8","y1":"688.9","x2":"132.5","y2":"688.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"208.7","y1":"292.6","x2":"208.7","y2":"346.9"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"123.9","y1":"396.2","x2":"212.9","y2":"396.2"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"36.9","y1":"500","x2":"212.9","y2":"500"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"208","y1":"391.3","x2":"208","y2":"500"},"children":[]},{"name":"line","type":"element","value":"","attributes":{"class":"st1","x1":"208","y1":"428.5","x2":"338.5","y2":"428.5"},"children":[]}]},{"name":"g","type":"element","value":"","attributes":{"id":"Windows"},"children":[{"name":"line","type":"element","value":"","attributes":{"class":"st2","x1":"238.6","y1":"911.1","x2":"157.7","y2":"911.1"},"children":[]}]}]}
























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
                        angle = round(math.degrees(math.atan2(y2-y1, x2-x1)))
                        w = 0.1 if children.get('attributes').get('id') == 'Inner_Walls' else 0.2
                        lenth = math.hypot(x2 - x1, y2 - y1)
                        if y1 == y2 and children.get('attributes').get('id') == 'Outer_Walls':
                            angle = 0
                            start_point = [min(x1, x2)-(w/2*100), min(y1, y2)]
                        if y1 == y2 and children.get('attributes').get('id') == 'Inner_Walls':
                            angle = 0
                            start_point = [min(x1, x2)-(w*100), min(y1, y2)+(w/2*100)]
                        if x1 == x2 and children.get('attributes').get('id') == 'Outer_Walls':
                            angle = 90
                            lenth = abs(y1 - y2)
                            start_point = [min(x1, x2), min(y1, y2)+(w/2*100)]
                        if x1 == x2 and children.get('attributes').get('id') == 'Inner_Walls':
                            angle = 90
                            lenth = abs(y1 - y2)
                            start_point = [min(x1, x2)-(w/2*100), min(y1, y2)+(w*100)]
                        if x1 != x2 and y1 != y2 and angle < -90 and angle > -180:
                            theta_rad = math.radians(angle+180)
                            x3 = x1+(w/2*100)*math.cos(theta_rad)
                            y3 = y1-(w/2*100)*math.sin(theta_rad)
                            x4 = x2+(w/2*100)*math.cos(theta_rad)
                            y4 = y2-(w/2*100)*math.sin(theta_rad)
                            start_point = [min(x3, x4)-w/2*100, min(y3, y4)+w/2*100]
                        if x1 != x2 and y1 != y2 and angle > 90 and angle < 180:
                            theta_rad = math.radians(angle+180)
                            x3 = x1+(w/2*100)*math.cos(theta_rad)
                            y3 = y1-(w/2*100)*math.sin(theta_rad)
                            x4 = x2+(w/2*100)*math.cos(theta_rad)
                            y4 = y2-(w/2*100)*math.sin(theta_rad)
                            start_point = [max(x3, x4)-w/2*100, min(y3, y4)+w/2*100]
                        if x1 != x2 and y1 != y2 and angle < 0 and angle > -90:
                            theta_rad = math.radians(angle+180)
                            x3 = x1-(w/2*100)*math.cos(theta_rad)
                            y3 = y1+(w/2*100)*math.sin(theta_rad)
                            x4 = x2-(w/2*100)*math.cos(theta_rad)
                            y4 = y2+(w/2*100)*math.sin(theta_rad)
                            start_point = [max(x3, x4)-w/2*100, min(y3, y4)+w/2*100]
                        if x1 != x2 and y1 != y2 and angle > 0 and angle < 90:
                            theta_rad = math.radians(angle+180)
                            x3 = x1-(w/2*100)*math.cos(theta_rad)
                            y3 = y1+(w/2*100)*math.sin(theta_rad)
                            x4 = x2-(w/2*100)*math.cos(theta_rad)
                            y4 = y2+(w/2*100)*math.sin(theta_rad)
                            start_point = [min(x3, x4)-w/2*100, min(y3, y4)+w/2*100]


                        m = {}
                        m['t'] = 'wall'
                        m['l'] = start_point
                        m['w'] = w
                        m['h'] = 0.25
                        m['map'] = [{'l': lenth, 'c': angle}]
                        map.append(m)
            if children.get('attributes').get('id') == 'Windows':
                windows = children.get('children')
                for window in windows:
                    if window.get('name') == 'line':
                        atr = window.get('attributes')
                        x1, x2, y1, y2 = float(atr.get('x1')), float(atr.get('x2')), float(atr.get('y1')), float(
                            atr.get('y2'))
                        start_point = [min(x1, x2), min(y1, y2)]
                        m = {}
                        m['t'] = 'window'
                        m['l'] = start_point
                        map.append(m)
print(map)


