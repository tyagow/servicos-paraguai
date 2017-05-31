$(document).ready(function(){
	 //Quebra as coordenadas usando , como parametro de separação
	 coord = $("#coordenadas").attr("data-coordenadas").split(',');

	 //Recebe as coordenadas
	 _lat = parseFloat(coord[0]);
	 _lng = parseFloat(coord[1]);

	 //Cria o Mapa posicionado em Ciudad del este
	 map = new GMaps({
	   div: '#map',
	   lat: -25.513475,
	   lng: -54.615440,
	   zoom:19,
	 });

	 //Seta o centro do mapa para as coordenadas do estabelecimento
	 map.setCenter(_lat, _lng);

	 //Adiciona o marcador baseado nas coordenadas
	 map.addMarker({
	   lat: _lat,
	   lng: _lng
	 });
});