const range = Number(prompt("Enter number"))

const secretNum = 12

let guess = 0

while (guess != secretNum) {
    let guess = prompt("Try to guess the number trough 1 and your guess")
    if (guess > range) {
        alert('The number is too high!')
    }
    else if (guess < 0) {
        alert('The number less than zero!')
    }
    else if (guess === secretNum) {
        alert("Well done!")
        break
    } 
}