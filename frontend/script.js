async function predictSentiment() {

    let review = document.getElementById("review").value;

    if (review.trim() === "") {
        alert("Please enter a review.");
        return;
    }

    document.getElementById("result").innerHTML = "Predicting...";

    try {

        const response = await fetch("http://127.0.0.1:8000/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text: review
            })

        });

        const data = await response.json();

        document.getElementById("result").innerHTML =
            "Prediction: " + data.prediction;

    }

    catch (error) {

        document.getElementById("result").innerHTML =
            "Error connecting to API.";

        console.log(error);

    }

}