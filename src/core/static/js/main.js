$(document).ready(function(){
	$(".places").find(".itens").owlCarousel({
		loop:true,
		margin:20,
		nav:false,
		dots: false,
		autoplay:true,
		autoplayTimeout:2000,
		responsive:{
			0:{
				items:2
			},
			600:{
				items:3
			},
			1000:{
				items:6
			}
		}
	});
	$(".pictures").owlCarousel({
		loop:true,
		nav:false,
		dots: true,
		autoplay:true,
		autoplayTimeout:6000,
		items:1
	});

	$("#rateYo").rateYo({
	   rating: 3.6
	 });

});
