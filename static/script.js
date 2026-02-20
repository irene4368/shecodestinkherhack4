document.getElementById("caseForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        officerName: document.getElementById("officerName").value,
        designation: document.getElementById("designation").value,
        code: document.getElementById("code").value,
        mobile: document.getElementById("mobile").value,
        missingName: document.getElementById("missingName").value,
        missingAge: document.getElementById("missingAge").value,
    };

    const response = await fetch("/add-case", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    alert(result.message);

    loadCases();
});

async function loadCases() {
    const response = await fetch("/get-cases");
    const cases = await response.json();

    const list = document.getElementById("casesList");
    list.innerHTML = "";

    cases.forEach(c => {
        const li = document.createElement("li");
        li.innerText = `${c.missingName} (Age: ${c.missingAge}) - Officer: ${c.officerName}`;
        list.appendChild(li);
    });
}

loadCases();