
    function voicedata(){
     
      let recognition = new webkitSpeechRecognition();
      recognition.lang = "en-GB";
      recognition.onresult = function(event){
        console.log(event);
        document.getElementById("voicedata").value = event.results[0][0].transcript;
      };
      recognition.start();
    }
/*
    // JavaScript
    const voiceButton = document.getElementById('voiceButton');

    // Check for browser support
    if ('webkitSpeechRecognition' in window) {
        const recognition = new webkitSpeechRecognition();
    
        recognition.lang = 'en-US'; // Set language to English
    
        voiceButton.addEventListener('click', () => {
            recognition.start(); // Start speech recognition when button is clicked
        });
    
        recognition.onresult = function(event) {
            document.getElementById("voicedata").value = event.results[0][0].transcript;
            //const result = event.results[0][0].transcript;
            // Send the 'result' to your Django backend via an API endpoint
            // You can use fetch or XMLHttpRequest to send a POST request with the result
            // For example:
            // fetch('/your-backend-endpoint/', {
            //     method: 'POST',
            //     body: JSON.stringify({ query: result }),
            //     headers: {
            //         'Content-Type': 'application/json'
            //     }
            // })
            // .then(response => response.json())
            // .then(data => {
            //     // Handle the response from the backend
            // });
        };
    
        recognition.onerror = function(event) {
            console.error('Speech recognition error:', event.error);
        };
    } else {
        console.error('Speech recognition not supported in this browser');
    } */
    