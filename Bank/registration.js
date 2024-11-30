const users = []

document.getElementById('registerForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const name = document.getElementById('name').value
    const email = document.getElementById('email').value
    const password = document.getElementById('password').value
    const confirmPassword = document.getElementById('confirmPassword').value

    if (password === confirmPassword) {
        users.push({name, email, password});
        alert('Registration Successful!')
        localStorage.setItem('users', JSON.stringify(users));
        window.location.href = 'index.html';
    } else {
        alert('Passwords do not match');
    }
});