document.addEventListener('DOMContentLoaded', function () {
    console.log("Hello")

    // Functions for the speech recognition
    const startBtn = document.getElementById('startBtn');
    const stopBtn = document.getElementById('stopBtn');
    const questionInput = document.getElementById('question'); // Get the input field element
    const recognition = new webkitSpeechRecognition();
    //recognition.continuous = true;
    recognition.interimResults = true;

    recognition.addEventListener('result', (e) =>{
        const text = Array.from(e.results).map(result => result[0]).map(result => result.transcript).join('');
        console.log(e.results);
        questionInput.value = text;
    });

    /*recognition.onresult = (event) => {
        const resultIndex = event.resultIndex;
        const transcript = event.results[resultIndex][0].transcript;

        console.log(transcript);
        questionInput.value = transcript; // Update the input field value
    };*/

    startBtn.addEventListener('click', () => {
        recognition.start();
        startBtn.disabled = true;
        stopBtn.disabled = false;
        startBtn.innerText = 'Recording...';
    });

    stopBtn.addEventListener('click', () => {
        recognition.stop();
        startBtn.disabled = false;
        stopBtn.disabled = true;
        startBtn.innerText = 'Start Recording';
    });
});