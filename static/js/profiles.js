$(function(){
	$('#gifts').hide();
	$('#wishesClick').click(toggle);
	$('#giftsClick').click(toggle);
});
function toggle () { 
	myWishes = $('#wishes');
	myWishesContainer = $('#wishesContainer');
	myGifts = $('#gifts');
	myGiftsContainer = $('#giftsContainer');
	
	if(myWishes.is(':visible'))
	{
		myWishes.hide();
		myGifts.fadeIn();
		
		myGiftsContainer.addClass('stripes-arrow');
		myGiftsContainer.removeClass('stripes');
		
		myWishesContainer.addClass('stripes');
		myWishesContainer.removeClass('stripes-arrow');
	} else {
		myGifts.hide();
		myWishes.fadeIn();
		
		myWishesContainer.addClass('stripes-arrow');
		myWishesContainer.removeClass('stripes');
		
		myGiftsContainer.addClass('stripes');
		myGiftsContainer.removeClass('stripes-arrow');
	}
}
