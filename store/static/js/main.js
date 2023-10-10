var SpeechRecognition = new (window.SpeechRecognition || window.webkitSpeechRecognition
    || window.mozSpeechRecognition || window.msSpeechRecognition)();

   const the_button = document.getElementById("textinput");
   the_button.addEventListener('click', function(event) {
       SpeechRecognition.start();
   })

   SpeechRecognition.onresult = function(event){
       var the_text = event.results[0][0].transcript;
       document.getElementById('search').value = the_text;
   };

   SpeechRecognition.onend = function(){
       SpeechRecognition.stop();
   };






// implementing qrcode scanner

var qrcode = document.getElementById('qrcode');

// the above is the button that will be clicked to scan the qr code

qrcode.addEventListener('click', function(event){
   // event.preventDefault();
    var scanner = new Instascan.Scanner({ video: document.getElementById('preview') });
    scanner.addListener('scan', function (content) {
        alert('You just scanned: ' + content);
    });
    Instascan.Camera.getCameras().then(function (cameras) {
        if (cameras.length > 0) {
        scanner.start(cameras[0]);
        } else {
        console.error('No cameras found.');
        }
    }).catch(function (e) {
        console.error(e);
    });
})



var barcode = document.getElementById('barcode');

// the above is the button that will be clicked to scan the qr code

barcode.addEventListener('click', function(event){
   // event.preventDefault();
    var scanner = new Instascan.Scanner({ video: document.getElementById('preview') });
    scanner.addListener('scan', function (content) {
        alert('You just scanned: ' + content);
    });
    Instascan.Camera.getCameras().then(function (cameras) {
        if (cameras.length > 0) {
        scanner.start(cameras[0]);
        } else {
        console.error('No cameras found.');
        }
    }).catch(function (e) {
        console.error(e);
    });
})

