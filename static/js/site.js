$(document).ready(function() {
	/* 
		progressive enhancement, shadows and rounded corners
	 	shadows are added by adding the className 'shadow' to any block element, 
		rounded corners are added by specifying the className rounded_X where X is the corner radius in pixels
		eg: <div class='shadow rounded_4'>
	*/	
	var shadows = $(document).find('.shadow'), roundedCorners = $(document).find('*[class^="rounded"]'), radius;

	shadows.each( function( i, element ){
		nycga.ui.addDropShadow( element );
	});

	roundedCorners.each( function( i, element ){
		radius = parseInt( element.className.split('_')[1] );
		nycga.ui.roundCorners( element, radius );
	});

  $('p.notice').delay(2000).fadeOut(1000, function () {
    $(this).remove();
  });
	
});
try{Typekit.load();}catch(e){}
