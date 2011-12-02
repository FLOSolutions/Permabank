/* NYC GA UI JS classes
/* Created by Thiago de Mello Bueno 2011, NYC General Assembly thiago [a] madeofpeople.org
 * MIT (http://www.opensource.org/licenses/mit-license.php) licensed.
*/

// create nycga namespace if necessary
if( !nycga ) var nycga = { ui: {} };

/* cross browser friendly css3 dropshadow */
/* reffer to http://www.css3.info/preview/box-shadow/ */
nycga.ui.addDropShadow = function( el, shadow ){
	var styles, styleName, browser = jQuery.browser;
	// if not specified, go with a reasonable default
	styles = ( shadow )? shadow : '1px 1px 5px #ccc';
	// choose the right selector for the job
	if( browser.safari && browser.version < 500 ){
		styleName = "-webkit-box-shadow";
	}else if( browser.mozilla && browser.version < 4 ){
		styleName = "-moz-box-shadow";
	}else{
		styleName = "box-shadow";
	}
	if( ( browser.msie && browser.version >= 9) || !browser.ie ){
		jQuery( el ).css( styleName, styles );
	}else if( jQuery.boxShadow ){
		// if old ie, use the jQuery boxShadow plugin
		jQuery( el ).boxShadow( '1px', '1px', '5px', '#ccc' );
	}
};
/* css rounded corners */
nycga.ui.roundCorners = function( el, radius ){
	var browser = jQuery.browser, borderStyle;
	if( browser.safari && browser.version < 500 ){
		borderStyle = "-webkit-border-radius";
	}else if( browser.firefox && browser.version < 4 ){
		borderStyle = "-moz-border-radius";
	}else{
		borderStyle = "border-radius";
	}
	if( ( browser.ie && browser.version >= 9) || !browser.ie  ){
		jQuery( el ).css( borderStyle, radius + "px" );
	}
};

/* Created by Martin Hintzmann 2008 martin [a] hintzmann.dk
 * MIT (http://www.opensource.org/licenses/mit-license.php) licensed.
 *
 * Version: 0.1
 *
 * Requires:
 *   jQuery 1.2+
 */
(function($) {
	$.fn.boxShadow = function(xOffset, yOffset, blurRadius, shadowColor) {
		if (!$.browser.msie) return;
		return this.each(function(){
			$(this).css({
				position:	"relative",
				zoom: 		1,
				zIndex:		"2"
			});
			$(this).parent().css({
					position:	"relative"
			});
			
			var div=document.createElement("div");
			$(this).parent().append(div);

			var _top, _left, _width, _height;
			if (blurRadius != 0) {
				$(div).css("filter", "progid:DXImageTransform.Microsoft.Blur(pixelRadius="+(blurRadius)+", enabled='true')");
				_top = 		yOffset-blurRadius-1;
				_left =		xOffset-blurRadius-1;
				_width =		$(this).outerWidth()+1;
				_height =	$(this).outerHeight()+1;
			} else {
				_top = 		yOffset;
				_left =		xOffset;
				_width = 	$(this).outerWidth();
				_height = 	$(this).outerHeight();
			}
			$(div).css({
				top: 			_top,
				left:			_left,
				width:		_width,
				height:		_height,
				background:	shadowColor,
				position:	"absolute",
				zIndex:		1
			});
			
	  });
	};
})(jQuery);