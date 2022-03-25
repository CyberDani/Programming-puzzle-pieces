function getDatePartString(datePartAsInt, str) {
	ans = datePartAsInt + " " + str;
	if (datePartAsInt > 1)
		ans += "s";
	
	return ans;
}

function getSecondsString(secondsAsInt) {	
	return getDatePartString(secondsAsInt, "second");
}

function getMinutesString(minutesAsInt) {	
	return getDatePartString(minutesAsInt, "minute");
}

function getHoursString(hoursAsInt) {	
	return getDatePartString(hoursAsInt, "hour");
}

function getDaysString(daysAsInt) {	
	return getDatePartString(daysAsInt, "day");
}

function getWeekString(weekAsInt) {	
	return getDatePartString(weekAsInt, "week");
}

function getYearString(yearAsInt) {	
	return getDatePartString(yearAsInt, "year");
}

function getMonthString(monthAsInt) {	
	return getDatePartString(monthAsInt, "month");
}

function getTwoDatePart(fn1, int1, fn2, int2) {
	ans = fn1(int1);
	if (int2 > 0)
		ans += " and " + fn2(int2);
	
	return ans;
}

function getDaysAndHoursString(daysAsInt, hoursAsInt) {
	return getTwoDatePart(getDaysString, daysAsInt, getHoursString, hoursAsInt);
}

function getWeeksAndDaysString(weeksAsInt, daysAsInt) {
	return getTwoDatePart(getWeekString, weeksAsInt, getDaysString, daysAsInt);
}

function getMonthsAndWeeksString(monthsAsInt, weeksAsInt) {
	return getTwoDatePart(getMonthString, monthsAsInt, getWeekString, weeksAsInt);
}

function getYearsAndMonthsString(yearsAsInt, monthsAsInt) {
	return getTwoDatePart(getYearString ,yearsAsInt, getMonthString, monthsAsInt);
}

function getTotalDatePartsFromMs(ms) {
	let sec = Math.ceil(ms / 1000);
	let mins = Math.ceil(sec / 60);
	let hours = Math.floor(mins / 60);
	let days = Math.floor(hours / 24);
	let weeks = Math.floor(days / 7);
	let months = Math.floor(weeks / 4);
	let years = Math.floor(months / 12);
	
	return {
		"sec": sec, 
		"mins": mins,
		"hours": hours,
		"days": days,
		"weeks": weeks,
		"months": months,
		"years": years
	};
}

function getDateStringFromDateParts(totalDateParts) {
	if (totalDateParts.sec < 60)
		return getSecondsString(totalDateParts.sec);
	
	if (totalDateParts.mins < 60) 
		return getMinutesString(totalDateParts.mins);
	
	if (totalDateParts.hours < 24)
		return getHoursString(totalDateParts.hours);
	
	if (totalDateParts.days < 7) {
		totalDateParts.hours = totalDateParts.hours % 24;
		return getDaysAndHoursString(totalDateParts.days, totalDateParts.hours);
	}
	
	if (totalDateParts.weeks < 4) {
		totalDateParts.days = totalDateParts.days % 7;
		return getWeeksAndDaysString(totalDateParts.weeks, totalDateParts.days);
	}
	
	if (totalDateParts.months < 12) {
		totalDateParts.weeks = totalDateParts.weeks % 4;
		return getMonthsAndWeeksString(totalDateParts.months, totalDateParts.weeks);
	}
	
	totalDateParts.months = totalDateParts.months % 12;
	return getYearsAndMonthsString(totalDateParts.years, totalDateParts.months);
}

function getDateStringFromMs(ms) {
	let dateParts = getTotalDatePartsFromMs(ms);
	return getDateStringFromDateParts(dateParts);
}

function getDateStringSinceMs(ms) {
	let timeDurationAsMs = new Date().getTime() - ms;
	return getDateStringFromMs(timeDurationAsMs);
}

function updateLastUpdatedTextAsync() {
	$.ajax({
	  url: "https://api.github.com/repos/CyberDani/Programming-puzzle-pieces",
	  dataType: "json",
	  method: "GET"
	}).done(function(resp, textStatus, jqXHR) {
		let updatedAtMs = new Date(resp.pushed_at).getTime();
		let githubLink = "<a href='https://github.com/CyberDani/Programming-puzzle-pieces'"
					+ " class='teal-text text-lighten-4'><i class='fa-brands fa-github fa-fw'></i> GitHub</a>";
		let durationString = getDateStringSinceMs(updatedAtMs) + " ago on " + githubLink;
		
		$('#githubRepoUpdatedText').html(durationString);
	}).fail(function() {
		// alert( "error" );
	}).always(function() {
		//alert( "complete" );
	});
}