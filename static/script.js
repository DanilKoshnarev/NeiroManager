document.getElementById("queryForm").addEventListener("submit", async function(e) {
    e.preventDefault();
    const prompt = document.getElementById("prompt").value;
    const service = document.getElementById("service").value;

    const responseDiv = document.getElementById("response");
    responseDiv.innerHTML = "Loading...";

    const response = await fetch("/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt, service })
    });

    const data = await response.json();
    responseDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
});