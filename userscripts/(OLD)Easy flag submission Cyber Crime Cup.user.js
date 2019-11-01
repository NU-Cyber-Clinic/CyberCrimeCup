// ==UserScript==
// @name         Easy flag submission Cyber Crime Cup
// @namespace    https://rtm516.co.uk/
// @version      1.0
// @description  Adds a button to auto submit the flag
// @author       rtm516
// @match        http://*.cybertrial.co.uk/
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

	function submitFlag() {
		var flag = document.body.textContent.match(".{4}-.{4}-.{4}-.{4}-.{4}-.{4}-.{4}")[0];

		var newIFrame = document.createElement("iframe");
		newIFrame.setAttribute("style", "display:none;");
		newIFrame.src = `data:text/html;charset=utf-8,` + encodeURI(`<html><body onload="document.querySelector(\`form\`).submit();"><form id="keySubmit" method="POST" action="https://www.cybercrime.co.uk/dashboard-challenges"><input type="hidden" name="captureflag" value="` + flag + `"></form></body></html>`);

		document.body.append(newIFrame);

		setTimeout(function() {newIFrame.remove()}, 1000);
	}

	var newDiv = document.createElement("div");
	newDiv.setAttribute("style", "top:50px;right:15px;position:absolute;");
	newDiv.innerHTML = "<button onclick='" + submitFlag + ";submitFlag();'>Submit flag</button>";

	document.body.append(newDiv);
})();