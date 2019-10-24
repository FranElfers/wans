var activa = 0;

$(document).ready(function(){
    pasarPagina(true);
    $('.hide').hide();
});

var pasarPagina = function(sentido){
    $('#1').hide();
    $('#2').hide();
    $('#3').hide();
    sentido ? activa += 1 : activa -= 1;
    $('#' + activa).show();
};

var map = L.map('map').setView([-34.78, -58.20], 14);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);

var searchControl = L.esri.Geocoding.geosearch().addTo(map);
var geocodeService = L.esri.Geocoding.geocodeService();

var results = L.layerGroup().addTo(map);

searchControl.on('results', function (data) {
    $('.resultado').text(data.text);
    $('#dir').text('Dirección: ' + data.text);
    var presentacion = $('.presentacion').val();
    $('#id_presentacion').val(presentacion);
    $("#id_ubicacion").val(data.text);
    $("#id_latitud").val(data.latlng.lat);
    $("#id_longitud").val(data.latlng.lng);
    results.clearLayers();
    for (var i = data.results.length - 1; i >= 0; i--) {
      results.addLayer(L.marker(data.results[i].latlng));
    }
});

map.on('click', function (e) {
    geocodeService.reverse().latlng(e.latlng).run(function (error, result) {
        if (error) {
            return;
        }
        L.marker(result.latlng).addTo(map).bindPopup(result.address.Match_addr).openPopup();
    });
});