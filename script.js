function updateTelemetry(battery, gps, altitude) {
    document.getElementById("battery").textContent = `Battery: ${battery}%`;
    document.getElementById("gps").textContent = `GPS: ${gps}`;
    document.getElementById("altitude").textContent = `Altitude: ${altitude}m`;
}

function addLog(message) {
    const logContainer = document.getElementById("logs-content");
    const newLog = document.createElement("p");
    newLog.textContent = message;
    logContainer.appendChild(newLog);
}

// Example usage
updateTelemetry(85, "23.4567, 78.1234", 120);
addLog("Drone initialized successfully.");
