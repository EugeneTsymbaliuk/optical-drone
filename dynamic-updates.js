let file_volts = 'files/volts.txt';
let file_amps = 'files/amps.txt';
let file_sats = 'files/sats.txt';
let file_heading = 'files/heading.txt';

function fetchDada(file, item) {
    fetch(file)
    .then((x) => x.text())
    .then((y) => {document.getElementById(item).innerHTML = y});
}

function updateLiveData() {
    // Current time
    const now = new Date();
    document.getElementById('currentTime').textContent =
        now.toLocaleTimeString();

    // Sats number
    fetchDada(file_sats, 'sats')
    //document.getElementById('sats').textContent =
    //    Math.floor(Math.random() * 1000);

    // Volts
    fetchDada(file_volts, 'volts')
    //document.getElementById('volts').textContent =
    //    Math.floor(Math.random() * 1000);

    // Amps
    fetchDada(file_amps, 'amps')
    // document.getElementById('amps').textContent =
    //     Math.floor(Math.random() * 1000);

    // Heading
    fetchDada(file_heading, 'head')
    //document.getElementById('head').textContent =
    //    Math.floor(Math.random() * 1000);

    // Update timestamp
    updateTimestamp();
}

const timer = setInterval(updateLiveData, 1000);
updateLiveData();
