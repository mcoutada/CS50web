function startDictation() {

    if (window.hasOwnProperty('webkitSpeechRecognition')) {

        var recognition = new webkitSpeechRecognition();

        recognition.continuous = false;
        recognition.interimResults = false;

        recognition.lang = "en-US";
        recognition.start();

        // recognition.onstart = function() { ... }
        // recognition.onresult = function(event) { ... }
        // recognition.onerror = function(event) { ... }
        // recognition.onend = function() { ... }


        document.getElementById('transcript').value

        recognition.onstart = function(e) {
            document.getElementById('transcript').value = 'Recording...';
        }

        recognition.onresult = function(e) {
            document.getElementById('transcript').value = e.results[0][0].transcript;
            recognition.stop();
            document.getElementById('labnol').submit();
        };

        recognition.onerror = function(e) {
            recognition.stop();
        }

    }
}