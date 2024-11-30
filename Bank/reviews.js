const form = document.getElementById('reviewForm')

form.addEventListener('submit', function (e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const reviewText = document.getElementById('reviewText').value;
    const reviewsContainer = document.querySelector('main');
    const newReview = document.createElement('div');
    newReview.classList.add('review');
    newReview.innerHTML = `
    <h4>${name}</h4>
    <p>⭐⭐⭐⭐⭐</p>
    <p>${reviewText}</p>
    `;
    reviewsContainer.appendChild(newReview);

    form.reset();
})
