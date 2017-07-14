$(document).ready(function(){
	 //Cria o Mapa posicionado em Ciudad del este
	 map = new GMaps({
	   div: '#map',
	   lat: -25.513475,
	   lng: -54.615440,
	   zoom:14,
	 });
	 
	 addMakers(map);
	 fullMapHeight();
});

function addMakers(map){

	$(".estabelecimento").each(function(){
		//Recebe as coordenadas
		coord = $(this).attr("data-coordenadas").split(',');
		_lat = parseFloat(coord[0]);
	 	_lng = parseFloat(coord[1]);
	
	 	//Adiciona o marcador baseado nas coordenadas
		map.addMarker({
	 		  lat: _lat,
	 		  lng: _lng
	 	});

	});
	
	// Se o resultado da busca for 1 estabelecimento seta o centro do mapa para o estabelecimento
	if($(".estabelecimento").length==1){
	 map.setCenter(_lat, _lng);
	}
}

function fullMapHeight(){
	var wh = $(document).height();
	var hh = $(".header").height();
	var fh = $(".footer").height();
	$("#map").height(wh-hh-fh);
}