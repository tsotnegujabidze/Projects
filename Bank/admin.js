const convertionRate = 0.93;

function convertCurrency() {
    const usdAmount = document.getElementById('usdAmount').value;
    
    if (usdAmount <= 0) {
        alert('Please enter a valid amount in USD');
        return;
    }

    const eurAmount = usdAmount * convertionRate

    document.getElementById('exchangeRateResult').textContent = `${usdAmount} USD = ${eurAmount.toFixed(2)} EUR`
}