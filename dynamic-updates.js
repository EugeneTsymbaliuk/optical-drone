let file_volts = 'files/volts.txt';
let file_amps = 'files/amps.txt';
let file_sats = 'files/sats.txt';
let file_heading = 'files/heading.txt';
let file_arm = 'files/arm.txt';
let file_gspeed = 'files/gspeed.txt';
let file_lat = 'files/lat.txt';
let file_lon = 'files/lon.txt';

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

    // Heading
    fetchDada(file_arm, 'arm')

    // Heading
    fetchDada(file_gspeed, 'gspeed')

    // Heading
    fetchDada(file_lat, 'lat')

    // Heading
    fetchDada(file_lon, 'lon')
 
    // Update timestamp
    updateTimestamp();
}

const timer = setInterval(updateLiveData, 1000);
updateLiveData();
