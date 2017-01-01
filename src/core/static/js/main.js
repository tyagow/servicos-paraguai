jQuery(document).ready(function($) {
    'use strict';
    //SMOOTH SCROLL
    smoothScroll.init({
        speed: 500, // How fast to complete the scroll in milliseconds
        easing: 'easeInOutCubic', // Easing pattern to use
        updateURL: false, // Boolean. Whether or not to update the URL with the anchor hash on scroll
        callbackBefore: function ( toggle, anchor ) {}, // Function to run before scrolling
        callbackAfter: function ( toggle, anchor ) {} // Function to run after scrolling
    });

    //FIX HOVER EFFECT ON IOS DEVICES
    document.addEventListener("touchstart", function(){}, true);
});

$(window).load(function(){

    //HEADER ANIMATION
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        var offset = $(".header-frame").height() / 3;

        if (scroll > offset) {
            $( ".header-frame" ).addClass( "header-frame-fixed" );
        } else {
            $( ".header-frame" ).removeClass( "header-frame-fixed" );
        }

    });

});