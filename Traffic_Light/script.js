const green = document.getElementById('green');
const yellow = document.getElementById('yellow');
const red = document.getElementById('red');
const timer = document.getElementById('timer');

let currentMode = 'Green';
let countdown;

function changeLights() {
    if (currentMode === 'Green') {
        green.style.backgroundColor = 'green';
        yellow.style.backgroundColor = 'black';
        red.style.backgroundColor = 'black';
        startCountdown(15);

        setTimeout(() => {
            currentMode = 'Yellow';
            changeLights();
        }, 15000);
    } else if (currentMode === 'Yellow') {
        green.style.backgroundColor = 'black';
        yellow.style.backgroundColor = 'yellow';
        red.style.backgroundColor = 'black';
        startCountdown(3);

        setTimeout(() => {
            currentMode = 'Red';
            changeLights();
        }, 3000);
    } else if (currentMode === 'Red') {
        green.style.backgroundColor = 'black';
        yellow.style.backgroundColor = 'black';
        red.style.backgroundColor = 'red';
        startCountdown(10);

        setTimeout(() => {
            currentMode = 'Green';
            changeLights();
        }, 10000);
    }
}

function startCountdown(seconds) {
    clearInterval(countdown);
    let timeLeft = seconds;
    timer.textContent = timeLeft;

    countdown = setInterval(() => {
        timeLeft -= 1;
        timer.textContent = timeLeft;

        if (timeLeft <= 0) {
            clearInterval(countdown);
        }
    }, 1000);
};