let form = document.querySelector("#grandpy_form");

function postFormData(url, data) {
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
        var answerDiv = document.getElementById('answer');
        answerDiv.innerHTML = response.adress;
        var storyDiv = document.getElementById('story');
        storyDiv.innerHTML = response.story;
    })
})