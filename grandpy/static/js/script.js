let form = document.querySelector("#grandpy_form");
var map;
var marker;

document.querySelector("#loader").style.visibility = "hidden";

function postFormData(url, data) {
    document.querySelector("#loader").style.visibility = "visible";
    document.querySelector("#grandpy").style.visibility = "hidden";
    document.querySelector("#map").style.visibility = "hidden";
    return fetch(url, {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}

form.addEventListener("submit", function (event) {

    event.preventDefault();

    postFormData("/userinput", new FormData(form))
    .then(response => {
        console.log(response);
        var answerDiv = document.getElementById("answer");
        answerDiv.innerHTML = response.adress;
        var storyDiv = document.getElementById("story");
        storyDiv.innerHTML = response.story;
        var latitude = response.lat
        var longitude = response.lng
        map = new google.maps.Map(document.getElementById("map"), {
            center: {lat: latitude, lng: longitude},
            zoom: 18
        });
        marker = new google.maps.Marker({
            position: {lat: latitude, lng: longitude},
            map: map
        });
        
        document.querySelector("#loader").style.visibility = "hidden";
        document.querySelector("#grandpy").style.visibility = "visible";
        document.querySelector("#map").style.visibility = "visible";
        document.getElementById("grandpy_form").reset();
    })
});