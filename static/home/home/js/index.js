$(document).ready(()=>{
	$('.nav-item').click((e)=>{
		$('.nav-item').removeClass('active');
		$(e.currentTarget).addClass('active');
	})
})
function isInViewport(element) {
    var elementTop = $(element).offset().top;
    var elementBottom = elementTop + $(element).outerHeight();

    var viewportTop = $(window).scrollTop();
    var viewportBottom = viewportTop + $(window).height();

    return elementBottom > viewportTop && elementTop < viewportBottom;
};
$(window).on('resize scroll', function() {
	var section = $('.section')
	for (var i = section.length - 1; i >= 0; i--) {
	    if (isInViewport(section[i])) {
	        $('.nav-item').removeClass('active');
			$($('.' + section[i].id)).addClass('active');
			break
	    }
	}
});