// Define userform variable
let form = document.querySelector("#grandpy_form");
// Define map variable for gmap api
var map;
// Define marker variable for gmap api
var marker;

// Hide the loader at page first loading
document.querySelector("#loader").style.visibility = "hidden";

function postFormData(url, data) {
    // Display loader
    document.querySelector("#loader").style.visibility = "visible";
    // Hide text div (answer and story)
    document.querySelector("#grandpy").style.visibility = "hidden";
    // Hide google map
    document.querySelector("#map").style.visibility = "hidden";
    // return userform
    return fetch(url, {
        method: "POST",
        body: data
    })
    // convert response to json
    .then(response => response.json())
    .catch(error => console.log(error));
}

// if user submit an input
form.addEventListener("submit", function (event) {

    // does not reload a page
    event.preventDefault();

    // use function with user input
    postFormData("/API/request", new FormData(form))
    .then(response => {
        // display adress in adress div
        var answerDiv = document.getElementById("answer");
        answerDiv.innerHTML = response.adress;
        // display story in story div
        var storyDiv = document.getElementById("story");
        storyDiv.innerHTML = response.story;
        // get latitude to setup google map
        var latitude = response.lat
        // get longitude to setup google map
        var longitude = response.lng
        // set google map
        map = new google.maps.Map(document.getElementById("map"), {
            center: {lat: latitude, lng: longitude},
            zoom: 18
        });
        // set google map marker
        marker = new google.maps.Marker({
            position: {lat: latitude, lng: longitude},
            map: map
        });
        
        // hide loader
        document.querySelector("#loader").style.visibility = "hidden";
        // show text div (answer and story)
        document.querySelector("#grandpy").style.visibility = "visible";
        // show google map
        document.querySelector("#map").style.visibility = "visible";
        // reset userform
        document.getElementById("grandpy_form").reset();
    })
});