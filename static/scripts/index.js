console.log("index.js loaded fine.");

var timestampLabel = document.getElementById("timestamp");

function updateTime() 
{
    timestampLabel.innerText = new Date().toTimeString();
}
updateTime();
setInterval(updateTime, 1000);

