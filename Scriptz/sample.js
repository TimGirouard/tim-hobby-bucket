function sign_out()
{
	/* Comment */
	$("#loading").show()
	$.get("log_in", {logout:"True"},

	function( )
	{
		window.location="";
	})
}
