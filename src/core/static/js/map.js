/**
 * Created by partiu on 08/12/16.
 */
var center;
var map;
function calculateCenter() {
    center = map.getCenter();
}function init_map_all() {
    var queryObject = {};
    location.search.substr(1).split("&").forEach(function(item) {queryObject[item.split("=")[0]] = item.split("=")[1]});
    $.ajax({
        url: '/api/estabelecimentos/?'+ $.param(queryObject),
        dataType: 'json',
        success: function (data) {
            for (var i=0;i< data.length; i++) {
                new google.maps.Marker({
                    map: map,
                    position: new google.maps.LatLng(data[i].latitude, data[i].longitude),
                    title: data[i].nome,
                    icon: data[i].categoria_icon
                });
            }

        }
    });
    var Lat = parseFloat(-25.513475);
    var Lng = parseFloat(-54.615440);

    var myOptions = {
        zoom: 14,
        center: new google.maps.LatLng(Lat, Lng), //change the coordinates
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        scrollwheel: false,
        styles: [{featureType:'all',stylers:[{gamma:0.90}]}]
    };
    map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);
    calculateCenter();

}
google.maps.event.addDomListener(window, 'load', init_map_all);
var resizeTimeout;
google.maps.event.addDomListener(window, "resize", function() {
        if (resizeTimeout) {
            clearTimeout(resizeTimeout);
        }
        resizeTimeout = setTimeout(function() { map.setCenter(center); }, 100);
    }
);