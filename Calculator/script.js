const output = document.getElementById('output');

const operators = ['+', '-', '*', '/'];

function clearOutput() {
    output.textContent = '';
}

function computeResult() {
    try {
        output.textContent = eval(output.textContent);
    } catch (error) {
        output.textContent = 'Error';
    }
}

function appendToOutput(value) {
    let currentText = output.textContent;

    if (operators.includes(value) && operators.includes(currentText.slice(-1))) {
        return;
    }
    output.textContent += value;
}

function removeLastChar() {
    let currentText = output.textContent;
    output.textContent = currentText.slice(0, -1);
}