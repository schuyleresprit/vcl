var map = L.map('map').setView([15.413, -61.35], 7);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);
var marker = L.marker([15.5, -61.35]).addTo(map);
