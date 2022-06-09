const mapContainer = document.getElementById('map'),
    mapOption = {
    center: new kakao.maps.LatLng(36.610030, 127.284156),
    level: 1
    };

function push_alarm() {
    (async () => {
        const response = fetch('/push_alarm',
        {
            method: 'GET',
        });
    })();
}

// load map
const map = new kakao.maps.Map(mapContainer, mapOption);
map.setMapTypeId(kakao.maps.MapTypeId.HYBRID);
const imageSRC = "http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
const imageSize = new kakao.maps.Size(24, 35);
const markerImage = new kakao.maps.MarkerImage(imageSRC, imageSize);

// center marker
var drone_pos = new kakao.maps.LatLng(36.610030, 127.284156);
var marker_drone = new kakao.maps.Marker({
    position: drone_pos,
    image : markerImage
});
marker_drone.setMap(map);

// real-time mark bebop2 on map
function update_gps(lat, lon) {  // update_gps
    if(lat) document.getElementById('lati').value = lat;
    else; // if(lat == undefined) do nothing

    if(lon) document.getElementById('long').value = lon;
    else; // if(lon == undefined) do nothing

    var drone_pos = new kakao.maps.LatLng(lat, lon);
    var marker_drone = new kakao.maps.Marker({
        position: drone_pos,
        image : markerImage
    });
    marker_drone.setMap(map);
    // every 3sec
    setTimeout(function() {marker_drone.setMap(null)}, 3000);
} 
let timerId = setInterval(update_gps, 1000);
