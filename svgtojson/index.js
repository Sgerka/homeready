'use strict';
const {parse, stringify} = require('svgson');
const svgson = require('svgson');

exports.handler = (event, context, callback) => {
    return JSON.stringify(svgson.parseSync(event.svg));

};

let event = {
    'svg': `
    <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 1272.1 1846.3" style="enable-background:new 0 0 1272.1 1846.3;" xml:space="preserve">
<style type="text/css">
	.st0{fill:none;stroke:#000000;stroke-width:20;stroke-miterlimit:10;}
</style>
<g id="Outer_Walls">
	<line class="st0" x1="513.6" y1="911.1" x2="112.5" y2="911.1"/>
	<line class="st0" x1="122.5" y1="693.9" x2="122.5" y2="911.1"/>
	<line class="st0" x1="27.1" y1="693.9" x2="131" y2="693.9"/>
	<line class="st0" x1="36.9" y1="381.2" x2="36.9" y2="693.9"/>
	<line class="st0" x1="234.7" y1="291.2" x2="107.2" y2="291.2"/>
	<line class="st0" x1="226" y1="69.3" x2="226" y2="291.2"/>
	<line class="st0" x1="443.7" y1="69.3" x2="216" y2="69.3"/>
	<line class="st0" x1="444.7" y1="120.2" x2="444.7" y2="59.2"/>
	<line class="st0" x1="589.5" y1="117.2" x2="415" y2="117.2"/>
	<line class="st0" x1="589.5" y1="353.7" x2="589.5" y2="107.4"/>
	<line class="st0" x1="415" y1="343.9" x2="589.5" y2="343.9"/>
	<line class="st0" x1="415" y1="107.2" x2="415" y2="353.9"/>
	<line class="st0" x1="415" y1="534" x2="415" y2="353.9"/>
	<line class="st0" x1="462.7" y1="577" x2="412.3" y2="526.9"/>
	<line class="st0" x1="510.7" y1="573.9" x2="454.8" y2="573.9"/>
	<line class="st0" x1="503.6" y1="911.1" x2="503.6" y2="563.8"/>
	<line class="st0" x1="116.5" y1="292.6" x2="116.5" y2="400.6"/>
	<line class="st0" x1="36.9" y1="390.7" x2="116.5" y2="390.7"/>
	<line class="st0" x1="1136.5" y1="911.1" x2="735.4" y2="911.1"/>
	<line class="st0" x1="1126.5" y1="911.1" x2="1126.5" y2="693.9"/>
	<line class="st0" x1="1118" y1="693.9" x2="1221.9" y2="693.9"/>
	<line class="st0" x1="1212.1" y1="693.9" x2="1212.1" y2="381.2"/>
	<line class="st0" x1="1141.8" y1="291.2" x2="1014.3" y2="291.2"/>
	<line class="st0" x1="1023" y1="291.2" x2="1023" y2="69.3"/>
	<line class="st0" x1="1033" y1="69.3" x2="805.3" y2="69.3"/>
	<line class="st0" x1="804.3" y1="59.2" x2="804.3" y2="120.2"/>
	<line class="st0" x1="834" y1="117.2" x2="659.5" y2="117.2"/>
	<line class="st0" x1="659.5" y1="107.4" x2="659.5" y2="353.7"/>
	<line class="st0" x1="659.5" y1="343.9" x2="834" y2="343.9"/>
	<line class="st0" x1="834" y1="353.9" x2="834" y2="107.2"/>
	<line class="st0" x1="834" y1="353.9" x2="834" y2="534"/>
	<line class="st0" x1="836.7" y1="526.9" x2="786.3" y2="577"/>
	<line class="st0" x1="794.2" y1="573.9" x2="738.3" y2="573.9"/>
	<line class="st0" x1="745.4" y1="563.8" x2="745.4" y2="911.1"/>
	<line class="st0" x1="1132.5" y1="400.6" x2="1132.5" y2="292.6"/>
	<line class="st0" x1="1132.5" y1="390.7" x2="1212.1" y2="390.7"/>
	<line class="st0" x1="112.5" y1="949.9" x2="513.6" y2="949.9"/>
	<line class="st0" x1="122.5" y1="949.9" x2="122.5" y2="1167.1"/>
	<line class="st0" x1="131" y1="1167.1" x2="27.1" y2="1167.1"/>
	<line class="st0" x1="36.9" y1="1167.1" x2="36.9" y2="1479.8"/>
	<line class="st0" x1="107.2" y1="1569.8" x2="234.7" y2="1569.8"/>
	<line class="st0" x1="226" y1="1569.8" x2="226" y2="1791.7"/>
	<line class="st0" x1="216" y1="1791.7" x2="443.7" y2="1791.7"/>
	<line class="st0" x1="444.7" y1="1801.8" x2="444.7" y2="1740.8"/>
	<line class="st0" x1="415" y1="1743.8" x2="589.5" y2="1743.8"/>
	<line class="st0" x1="589.5" y1="1753.6" x2="589.5" y2="1507.3"/>
	<line class="st0" x1="589.5" y1="1517.1" x2="415" y2="1517.1"/>
	<line class="st0" x1="415" y1="1507.1" x2="415" y2="1753.8"/>
	<line class="st0" x1="415" y1="1507.1" x2="415" y2="1327"/>
	<line class="st0" x1="412.3" y1="1334.1" x2="462.7" y2="1284"/>
	<line class="st0" x1="454.8" y1="1287.1" x2="510.7" y2="1287.1"/>
	<line class="st0" x1="503.6" y1="1297.2" x2="503.6" y2="949.9"/>
	<line class="st0" x1="116.5" y1="1460.4" x2="116.5" y2="1568.4"/>
	<line class="st0" x1="116.5" y1="1470.3" x2="36.9" y2="1470.3"/>
	<line class="st0" x1="735.4" y1="949.9" x2="1136.5" y2="949.9"/>
	<line class="st0" x1="1126.5" y1="1167.1" x2="1126.5" y2="949.9"/>
	<line class="st0" x1="1221.9" y1="1167.1" x2="1118" y2="1167.1"/>
	<line class="st0" x1="1212.1" y1="1479.8" x2="1212.1" y2="1167.1"/>
	<line class="st0" x1="1014.3" y1="1569.8" x2="1141.8" y2="1569.8"/>
	<line class="st0" x1="1023" y1="1791.7" x2="1023" y2="1569.8"/>
	<line class="st0" x1="805.3" y1="1791.7" x2="1033" y2="1791.7"/>
	<line class="st0" x1="804.3" y1="1740.8" x2="804.3" y2="1801.8"/>
	<line class="st0" x1="659.5" y1="1743.8" x2="834" y2="1743.8"/>
	<line class="st0" x1="659.5" y1="1507.3" x2="659.5" y2="1753.6"/>
	<line class="st0" x1="834" y1="1517.1" x2="659.5" y2="1517.1"/>
	<line class="st0" x1="834" y1="1753.8" x2="834" y2="1507.1"/>
	<line class="st0" x1="834" y1="1327" x2="834" y2="1507.1"/>
	<line class="st0" x1="786.3" y1="1284" x2="836.7" y2="1334.1"/>
	<line class="st0" x1="738.3" y1="1287.1" x2="794.2" y2="1287.1"/>
	<line class="st0" x1="745.4" y1="949.9" x2="745.4" y2="1297.2"/>
	<line class="st0" x1="1132.5" y1="1568.4" x2="1132.5" y2="1460.4"/>
	<line class="st0" x1="1212.1" y1="1470.3" x2="1132.5" y2="1470.3"/>
</g>
</svg>

`
};
console.log(exports.handler(event));

