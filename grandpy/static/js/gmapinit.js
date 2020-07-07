var gmapKey = GMAP_API_KEY;
var gmapUrl = "https://maps.googleapis.com/maps/api/js?key=" + gmapKey + "&callback=initMap";

function loadScript() {
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = gmapUrl;
    document.body.appendChild(script);
  }
  
  window.onload = loadScript;