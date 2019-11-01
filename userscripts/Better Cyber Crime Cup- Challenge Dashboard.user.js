// ==UserScript==
// @name         Better Cyber Crime Cup: Challenge Dashboard
// @namespace    https://rtm516.co.uk/
// @version      1.0
// @description  Ajusts the Cyber Crime Cup: Challenge Dashboard to add some new thing and fix others
// @author       rtm516
// @match        https://www.cybercrime.co.uk/dashboard-challenges
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

	// Fixed the buttons opening in a new tab
	var challengeButtons = document.querySelectorAll(".col-lg-5 .btn.btn-block");
	var notStarted = 0;
	var unFinished = 0;
	var finished = 0;

    challengeButtons.forEach(element => {
		//element.setAttribute("onclick", element.getAttribute("onclick").replace("document.location=", "window.open(").replace(";", ", '_blank');"))

		switch (element.textContent) {
			case "Start Challenge":
				notStarted++;
				break;
			case "Go To Challenge!":
				unFinished++;
				break;
			case "Replay For Fun":
				finished++;
				break;

			default:
				break;
		}
	});

	// Remove random spacing
	document.querySelector(".js-form-message").setAttribute("style", document.querySelector(".js-form-message").getAttribute("style").replace("75px", "15px"));

	// Fill spacing with challenge status and counts
	var total = challengeButtons.length;

	var form = document.querySelector("form[name=formflag]");
	var newDiv = document.createElement("div");
	newDiv.innerHTML = "<div><table style='width:100%;text-align:center;margin-bottom:15px;'><tr><th>Not Started</th><th>Not finished</th><th>Finished</th></tr><tr style='font-size:20pt;'><td>" + (notStarted + "/" + total) + "</td><td>" + (unFinished + "/" + total) + "</td><td>" + (finished + "/" + total) + "</td></tr></table></div>";
	form.parentNode.insertBefore(newDiv, form.nextSibling);

	// Score
	var scores = [...document.body.textContent.matchAll("[0-9][0-9]pts")];
	var totalScore = 0;
	scores.forEach(score => {
		totalScore += parseInt(score[0].replace("pts", ""));
	});

	var ptsSpan = document.querySelector("h3.display-4.text-primary  span");
	ptsSpan.setAttribute("style", "font-size:10pt;vertical-align: text-top;")
	ptsSpan.textContent = totalScore + "pts";
})();