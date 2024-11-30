function addToCart(button) {
    const cartSection = document.getElementById('cart-section');
    const cart = document.querySelector('.cart');

    if (cartSection.style.display === 'none') {
        cartSection.style.display = 'block';
    }

    const imageSrc = button.getAttribute('data-image');

    const image = document.createElement('img');
    image.src = imageSrc;
    image.alt = "Product Photo";

    cart.appendChild(image);
}