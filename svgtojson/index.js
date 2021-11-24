'use strict';
const {parse, stringify} = require('svgson');
const svgson = require('svgson');

exports.handler = (event, context, callback) => {
    return JSON.stringify(svgson.parseSync(event.svg));

};

let event = {
    'svg': `
    <svg version="1.1" id="Layer_2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 1272.1 1000" style="enable-background:new 0 0 1272.1 1000;" xml:space="preserve">
<style type="text/css">
	.st0{fill:none;stroke:#000000;stroke-width:20;stroke-miterlimit:10;}
	.st1{fill:none;stroke:#000000;stroke-width:10;stroke-miterlimit:10;}
	.st2{fill:none;stroke:#FF008C;stroke-width:20;stroke-miterlimit:10;}
</style>
<g id="Outer_Walls">
	<line class="st0" x1="513.6" y1="911.1" x2="112.5" y2="911.1"/>
	<line class="st0" x1="122.5" y1="693.9" x2="122.5" y2="911.1"/>
	<line class="st0" x1="26.9" y1="693.9" x2="132.5" y2="693.9"/>
	<line class="st0" x1="36.9" y1="381.2" x2="36.9" y2="693.9"/>
	<line class="st0" x1="236" y1="291.2" x2="106.5" y2="291.2"/>
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
	<line class="st0" x1="116.5" y1="292.6" x2="116.5" y2="401.2"/>
	<line class="st0" x1="36.9" y1="391.2" x2="116.5" y2="391.2"/>
</g>
<g id="Inner_Walls">
	<line class="st1" x1="266.8" y1="763.7" x2="266.8" y2="496"/>
	<line class="st1" x1="346.6" y1="501" x2="266.8" y2="501"/>
	<line class="st1" x1="338.5" y1="501" x2="338.5" y2="262.8"/>
	<line class="st1" x1="415" y1="266.4" x2="333.4" y2="266.4"/>
	<line class="st1" x1="232.7" y1="296.2" x2="338.5" y2="296.2"/>
	<line class="st1" x1="270.8" y1="688.9" x2="132.5" y2="688.9"/>
	<line class="st1" x1="208.7" y1="292.6" x2="208.7" y2="346.9"/>
	<line class="st1" x1="123.9" y1="396.2" x2="212.9" y2="396.2"/>
	<line class="st1" x1="36.9" y1="500" x2="212.9" y2="500"/>
	<line class="st1" x1="208" y1="391.3" x2="208" y2="500"/>
	<line class="st1" x1="208" y1="428.5" x2="338.5" y2="428.5"/>
</g>
<g id="Windows">
	<line class="st2" x1="238.6" y1="911.1" x2="157.7" y2="911.1"/>
</g>
</svg>

`
};
console.log(exports.handler(event));

