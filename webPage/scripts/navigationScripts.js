function loadPage(url) {
	$('.sidenav').sidenav('close');
	$("#webContent").LoadingOverlay("show");
	
	$.ajax({
		url: url,
		dataType: "html",
		method: "GET"
	}).done(function(html) {
		$("#webContent").html(html);
	}).fail(function() {
		alert( "error" );
	}).always(function() {
		$("#webContent").LoadingOverlay("hide");
	});
}

async function loadMainPage() {
	$('.sidenav').sidenav('close');
	$("#webContent").LoadingOverlay("show");
	
  let part1 = new Promise(function(resolve, reject) {
	$.ajax({
		url: "webPage/pages/mainPage/svgCurve1.txt",
		dataType: "html",
		method: "GET"
	}).done(function(html) {
		resolve(html);
	}).fail(function() {
		reject()
	});
  });
  
  let part2 = new Promise(function(resolve, reject) {
	$.ajax({
		url: "webPage/pages/mainPage/whatThisProjectOffers.txt",
		dataType: "html",
		method: "GET"
	}).done(function(html) {
		resolve(html);
	}).fail(function() {
		reject()
	});
  });
  
  let part3 = new Promise(function(resolve, reject) {
	$.ajax({
		url: "webPage/pages/mainPage/svgCurve2.txt",
		dataType: "html",
		method: "GET"
	}).done(function(html) {
		resolve(html);
	}).fail(function() {
		reject()
	});
  });
  
  let part4 = new Promise(function(resolve, reject) {
	$.ajax({
		url: "webPage/pages/mainPage/personalRecommandation.txt",
		dataType: "html",
		method: "GET"
	}).done(function(html) {
		resolve(html);
	}).fail(function() {
		reject()
	});
  });
  
  let part5 = new Promise(function(resolve, reject) {
	$.ajax({
		url: "webPage/pages/mainPage/svgCurve3.txt",
		dataType: "html",
		method: "GET"
	}).done(function(html) {
		resolve(html);
	}).fail(function() {
		reject()
	});
  });
  
  let part6 = new Promise(function(resolve, reject) {
	$.ajax({
		url: "webPage/pages/mainPage/textBelowCurves.txt",
		dataType: "html",
		method: "GET"
	}).done(function(html) {
		resolve(html);
	}).fail(function() {
		reject()
	});
  });
  
  $("#webContent").html(await part1);
  $("#webContent").append(await part2);
  $("#webContent").append(await part3);
  $("#webContent").append(await part4);
  $("#webContent").append(await part5);
  $("#webContent").append(await part6);
  
  $("#webContent").LoadingOverlay("hide");
}

$( ".topnav-logo" ).click(function() {
	loadMainPage();
});

$( ".menu-online-resources" ).click(function() {
	loadPage("webPage/pages/OnlineResources/main.html");
});

$( ".menu-design-patterns" ).click(function() {
	loadPage("webPage/pages/DesignPatterns/main.html");
});

$( ".menu-book-summaries" ).click(function() {

});

$( ".menu-common-principles" ).click(function() {

});