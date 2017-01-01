//GOOGLE MAP
var center;
var map;
function calculateCenter() {
    center = map.getCenter();
}
function init_map() {
    var coordenadas = $('#coordenadas').data('coordenadas');
    var LatLng = coordenadas.split(/,(.+)?/);
    var _lat = LatLng[0].replace(',', '');
    var _lng = LatLng[1].replace(',', '');

    var Lat = parseFloat(_lat);
    var Lng = parseFloat(_lng );


    var myOptions = {
        zoom: 16,
        center: new google.maps.LatLng(Lat, Lng), //change the coordinates
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        scrollwheel: false,
        styles: [{featureType:'all',stylers:[{gamma:0.90}]}]
    };
    map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);
    marker = new google.maps.Marker({
        map: map,
        position: new google.maps.LatLng(Lat, Lng) //change the coordinates
    });
    calculateCenter();

}
google.maps.event.addDomListener(window, 'load', init_map);
var resizeTimeout;
google.maps.event.addDomListener(window, "resize", function() {
        if (resizeTimeout) {
            clearTimeout(resizeTimeout);
        }
        resizeTimeout = setTimeout(function() { map.setCenter(center); }, 100);
    }
);