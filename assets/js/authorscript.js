$(document).ready(function() {
	var previousScroll, 
			previousWidth = 0,
			currentScroll = $(this).scrollTop(),
			curentWidth = $(window).width(),
			SpeedOfAnimationActivation = 0,
			totalHide = $('.hide'),
			posFirstBlock = $('.block').eq(0).offset().top - 150;
	
	// If the current position is > than the first 2 divs then force add the class to all divs.
	if (currentScroll > 600){
		for ( var i = 0; i < totalHide.length; i++ ){
			//Desktop animation
			$(totalHide[i]).addClass('slideIn_Mobile').removeClass('hide');
		}
	}
	
	// If the current width > than the 961px .... do something.
	function SpeedAnimation(){
		if (curentWidth >= 1136){
			SpeedOfAnimationActivation = 100;
		}
		else{
			SpeedOfAnimationActivation = 450;
		}
	}
	SpeedAnimation();

	// End
	
	// Get the position of each div just once and store it into the array.
	var array_div = [];// holds the relative position of each div in the page.
	for ( var j = 0; j < totalHide.length; j++ ){
		array_div[j] = $(totalHide[j]).offset().top + $(totalHide[j]).outerHeight()-SpeedOfAnimationActivation;
	}
	var startWidth = $(window).width();
	// If difference is > or < then recalculate each position again
	$(window).resize(function(event) {							
		var curentWidth = $(window).width();
		var difference = curentWidth - startWidth;

		if (difference > 175 || difference < -175){
			SpeedAnimation();
			
			for (var j = 0; j < totalHide.length; j++){
				array_div[j] = $(totalHide[j]).offset().top + $(totalHide[j]).outerHeight()-SpeedOfAnimationActivation;
			}
		}
	});
	// -------> End
	
	// Show each div on scroll
	$(window).scroll( function(){		
		var currentScroll = $(this).scrollTop();
		// Here we start the search of each div if we are scrolling down.
		if (currentScroll > previousScroll){
			// Get the current position of viewport from the top of page.
			var browser_window = $(window).scrollTop() + $(window).height();
			// Start the search for the current class in the html.
			for (var k = 0; k < totalHide.length; k++){
				let curentWidth = $(window).width();
				if ($(totalHide[k]).is('.hide') && array_div[k] != true && currentScroll > posFirstBlock){
					if (browser_window > array_div[k]){
						$(totalHide[k]).addClass('slideIn_Mobile').removeClass('hide');
						array_div[k] = true;
					}
				}
			}
		}
		previousScroll = currentScroll;
	});
	// End
});