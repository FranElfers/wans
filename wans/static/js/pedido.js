$(document).ready(function(){
    $('#2').hide();
    $('#3').hide();
    console.log(2);
});

var map = L.map('map').setView([40.91, -96.63], 4);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);

var searchControl = L.esri.Geocoding.geosearch().addTo(map);
var geocodeService = L.esri.Geocoding.geocodeService();

var results = L.layerGroup().addTo(map);

searchControl.on('results', function (data) {
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

// Pasar pagina
var pasarPagina = function(a,b){
    $(a).hide();
    $(b).show();
};