document.getElementById('predictionForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const area = document.getElementById('area').value;
    const location = document.getElementById('location').value;
    const bath = document.getElementById('bath').value;
    const bhk = document.getElementById('bhk').value;

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ area, location, bath, bhk })
    });

    const result = await response.json();

    if (result.price) {
        document.getElementById('result').innerText = `Estimated Price: ₹ ${result.price} lakhs`;
    } else {
        document.getElementById('result').innerText = `Error: ${result.error}`;
    }
});
