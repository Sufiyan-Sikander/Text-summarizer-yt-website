const button = document.getElementById("summarizeBtn");
const result = document.getElementById("result");
const loader = document.getElementById("loader");

button.addEventListener("click", async () => {

    const url = document.getElementById("url").value;
    const apiKey = document.getElementById("apiKey").value;

    if (!url || !apiKey) {
        alert("Please fill all fields");
        return;
    }

    result.innerHTML = "";
    loader.classList.remove("hidden");

    try {

        const response = await fetch("/summarize", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url,
                groq_api_key: apiKey
            })
        });

        const data = await response.json();

        loader.classList.add("hidden");

        if (data.error) {
            result.innerHTML =
                `<p style="color:red">${data.error}</p>`;
            return;
        }

        result.innerHTML = marked.parse(data.summary);

    } catch (error) {

        loader.classList.add("hidden");

        result.innerHTML =
            `<p style="color:red">${error}</p>`;
    }
});