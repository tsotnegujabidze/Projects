document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const email = document.getElementById('loginEmail').value
    const password = document.getElementById('loginPassword').value
    const users = JSON.parse(localStorage.getItem('users')) || [];
    const user = users.find(u => u.email === email && u.password === password);

    if (user) {
        alert('Login Successful');
        window.location.href = 'index.html'
    } else {
        alert('Invalid inputs')
    }
});