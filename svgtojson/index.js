'use strict';
const {parse, stringify} = require('svgson');
const svgson = require('svgson');

exports.handler = (event, context, callback) => {
    return JSON.stringify(svgson.parseSync(event.svg));

};

let event = {
    'svg': `
    <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 1000 1000" style="enable-background:new 0 0 1000 1000;" xml:space="preserve">
<style type="text/css">
	.st0{fill:none;stroke:#000000;stroke-width:0.2;stroke-miterlimit:10;}
	.st1{fill:none;stroke:#000000;stroke-width:0.1;stroke-miterlimit:10;}
	.st2{fill:none;stroke:#1D71B8;stroke-width:0.2;stroke-miterlimit:10;}
	.st3{fill:none;stroke:#36A9E1;stroke-width:0.2;stroke-miterlimit:10;}
	.st4{fill:none;stroke:#2D2E83;stroke-width:0.2;stroke-miterlimit:10;}
	.st5{fill:none;stroke:#29235C;stroke-width:0.2;stroke-miterlimit:10;}
	.st6{fill:none;stroke:#662483;stroke-width:0.2;stroke-miterlimit:10;}
	.st7{fill:none;stroke:#E52421;stroke-width:0.2;stroke-miterlimit:10;}
	.st8{fill:none;stroke:#F39200;stroke-width:0.1;stroke-miterlimit:10;}
	.st9{fill:none;stroke:#E94E1B;stroke-width:0.1;stroke-miterlimit:10;}
</style>
<g id="Outer_Walls">
	<line class="st0" x1="667.6" y1="889.3" x2="286.5" y2="889.3"/>
	<line class="st0" x1="286.5" y1="672.1" x2="286.5" y2="889.3"/>
	<line class="st0" x1="200.9" y1="672.1" x2="286.5" y2="672.1"/>
	<line class="st0" x1="200.9" y1="368.9" x2="200.9" y2="672.1"/>
	<line class="st0" x1="390" y1="269.4" x2="280.5" y2="269.4"/>
	<line class="st0" x1="390" y1="47.5" x2="390" y2="269.4"/>
	<line class="st0" x1="608.7" y1="47.5" x2="390" y2="47.5"/>
	<line class="st0" x1="608.7" y1="95.4" x2="608.7" y2="47.5"/>
	<line class="st0" x1="753.5" y1="95.4" x2="576.3" y2="95.4"/>
	<line class="st0" x1="753.5" y1="322.1" x2="753.5" y2="95.4"/>
	<line class="st0" x1="576.3" y1="322.1" x2="753.5" y2="322.1"/>
	<line class="st0" x1="576.3" y1="95.4" x2="576.3" y2="332.1"/>
	<line class="st0" x1="576.3" y1="505.1" x2="576.3" y2="329.3"/>
	<line id="Skew" class="st0" x1="623.6" y1="552.1" x2="576.3" y2="505.1"/>
	<line class="st0" x1="667.7" y1="552.1" x2="623.6" y2="552.1"/>
	<line class="st0" x1="667.6" y1="889.3" x2="667.6" y2="552.1"/>
	<line class="st0" x1="280.5" y1="269.4" x2="280.5" y2="368.9"/>
	<line class="st0" x1="200.9" y1="368.9" x2="280.5" y2="368.9"/>
</g>
<g id="Inner_Walls">
	<line class="st1" x1="432.7" y1="672.1" x2="286.5" y2="672.1"/>
	<line class="st1" x1="432.7" y1="747.7" x2="432.7" y2="475.1"/>
	<line class="st1" x1="502.3" y1="475.1" x2="432.7" y2="475.1"/>
	<line class="st1" x1="502.3" y1="246.7" x2="502.3" y2="475.1"/>
	<line class="st1" x1="374.2" y1="405.2" x2="502.3" y2="405.2"/>
	<line class="st1" x1="374.2" y1="474.6" x2="374.2" y2="368.9"/>
	<line class="st1" x1="200.9" y1="475.1" x2="374.2" y2="474.1"/>
	<line class="st1" x1="280.5" y1="368.9" x2="374.2" y2="368.9"/>
	<line class="st1" x1="390" y1="269.4" x2="390" y2="315.9"/>
	<line class="st1" x1="576.3" y1="246.7" x2="390" y2="246.7"/>
</g>
<g id="Windows">
	<line class="st2" x1="479.5" y1="889.3" x2="657.8" y2="889.3"/>
	<line class="st3" x1="324.8" y1="889.3" x2="387.7" y2="889.3"/>
	<line class="st3" x1="212.7" y1="672.1" x2="274" y2="672.1"/>
	<line class="st4" x1="214.9" y1="368.9" x2="254.9" y2="368.9"/>
	<line class="st5" x1="280.6" y1="279.3" x2="280.6" y2="358.8"/>
	<line class="st3" x1="390" y1="98.4" x2="390" y2="178.7"/>
	<line class="st3" x1="444" y1="47.5" x2="524.2" y2="47.5"/>
	<line class="st6" x1="681.9" y1="95.6" x2="741.8" y2="95.6"/>
</g>
<g id="Doors">
	<line class="st7" x1="667.7" y1="565.7" x2="667.7" y2="623.4"/>
	<line class="st8" x1="502.3" y1="413.9" x2="502.3" y2="461.8"/>
	<line class="st8" x1="502.3" y1="325" x2="502.3" y2="369.9"/>
	<line class="st8" x1="374.2" y1="426.3" x2="374.2" y2="468.2"/>
	<line class="st9" x1="576.3" y1="259.9" x2="576.3" y2="304.8"/>
	<line class="st8" x1="514.3" y1="246.7" x2="562.6" y2="246.7"/>
</g>
</svg>

`
};
console.log(exports.handler(event));

