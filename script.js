function generateAlert() {
    function generateAlert() {
    const aiBox = document.getElementById("aiOutput");

    if (!roadMode) {
        aiBox.innerText = "⚠ Please activate 'On The Road' mode first.";
        aiBox.style.backgroundColor = "#fff3cd";
        return;
    }

    const selectedArea = document.getElementById("areaSelect").value;

    aiBox.innerText = "🤖 Generating AI Alert...";
    aiBox.style.backgroundColor = "#fff3cd";

    setTimeout(function() {
        const alertMessage =
            "🚨 HIGH PRIORITY ALERT for " + selectedArea + " Workers\n\n" +
            "Stay alert near bus stands and railway stations.\n" +
            "Observe individuals matching the displayed profile.\n\n" +
            "Report immediately if spotted.";

        aiBox.innerText = alertMessage;
        aiBox.style.backgroundColor = "#fecaca";
    }, 2000);
}
    }

    const selectedArea = document.getElementById("areaSelect").value;

    const aiBox = document.getElementById("aiOutput");

    // Show generating message
    aiBox.innerText = "🤖 Generating AI Alert...";
    aiBox.style.backgroundColor = "#fff3cd";  // light yellow while generating

    // Simulate 2 second AI thinking delay
    setTimeout(function() {

        const alertMessage =
            "🚨 HIGH PRIORITY ALERT for " + selectedArea + " Workers\n\n" +
            "Missing Person: Stay alert in crowded transport hubs.\n" +
            "• Check bus stands\n" +
            "• Monitor railway stations\n" +
            "• Observe individuals matching the displayed description\n\n" +
            "If spotted, report immediately.";

        aiBox.innerText = alertMessage;
        aiBox.style.backgroundColor = "#ffcccc";  // light red alert box

    }, 2000);
}