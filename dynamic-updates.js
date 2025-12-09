  GNU nano 5.4                                                                                     dynamic-updates.js
let liveUpdatesActive = false;
let lat = 30.00
let lon = 50.00

function updateLiveData() {
    // Current time
    const now = new Date();
    document.getElementById('currentTime').textContent =
        now.toLocaleTimeString();

    // Sats number
    document.getElementById('sats').textContent =
        Math.floor(Math.random() * 1000);

    // Volts
    document.getElementById('volts').textContent =
        Math.floor(Math.random() * 1000);

    // Amps
    document.getElementById('amps').textContent =
        Math.floor(Math.random() * 1000);

    // Heading
    document.getElementById('head').textContent =
        Math.floor(Math.random() * 1000);

    // Update timestamp
    updateTimestamp();
}

const timer = setInterval(updateLiveData, 1000);
updateLiveData();



