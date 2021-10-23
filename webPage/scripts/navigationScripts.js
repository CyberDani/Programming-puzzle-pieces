function loadPage(url){
	$('.sidenav').sidenav('close');
	$("#webContent").LoadingOverlay("show")
	
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

$( ".menu-online-resources" ).click(function() {
	loadPage("webPage/pages/OnlineResources/main.html");
});

$( ".menu-design-patterns" ).click(function() {

});

$( ".menu-book-summaries" ).click(function() {

});

$( ".menu-common-principles" ).click(function() {

});