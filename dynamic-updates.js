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
    
    // Volts
    fetchDada(file_volts, 'volts')
   
    // Amps
    fetchDada(file_amps, 'amps')
   
    // Heading
    fetchDada(file_heading, 'head')
 
    // Update timestamp
    updateTimestamp();
}

const timer = setInterval(updateLiveData, 1000);
updateLiveData();
