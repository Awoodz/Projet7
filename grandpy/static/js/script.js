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
    // Return userform
    return fetch(url, {
        method: "POST",
        body: data
    })
    // Convert response to json
    .then(response => response.json())
    .catch(error => console.log(error));
}

// If user submit an input
form.addEventListener("submit", function (event) {

    // Does not reload a page
    event.preventDefault();

    // Use function with user input
    postFormData("/API/request", new FormData(form))
    .then(response => {
        // Display adress in adress div
        var answerDiv = document.getElementById("answer");
        answerDiv.innerHTML = response.adress;
        // Display story in story div
        var storyDiv = document.getElementById("story");
        storyDiv.innerHTML = response.story;
        // Get latitude to setup google map
        var latitude = response.lat
        // Get longitude to setup google map
        var longitude = response.lng
        // Set google map
        map = new google.maps.Map(document.getElementById("map"), {
            center: {lat: latitude, lng: longitude},
            zoom: 20
        });
        // Set google map marker
        marker = new google.maps.Marker({
            position: {lat: latitude, lng: longitude},
            map: map
        });
        
        // Hide loader
        document.querySelector("#loader").style.visibility = "hidden";
        // Show text div (answer and story)
        document.querySelector("#grandpy").style.visibility = "visible";
        // Show google map
        document.querySelector("#map").style.visibility = "visible";
        // Reset userform
        document.getElementById("grandpy_form").reset();
    })
});