// Add event listener to navigation links
document.querySelectorAll('nav a').forEach(link => {
	link.addEventListener('click', event => {
		event.preventDefault();
		const target = event.target.getAttribute('href');
		document.querySelector(target).scrollIntoView({ behavior: 'smooth' });
	});
});

// Add animation to gallery images
document.querySelectorAll('.gallery img').forEach(image => {
	image.addEventListener('mouseover', event => {
		event.target.style.transform = 'scale(1.1)';
	});
	image.addEventListener('mouseout', event => {
		event.target.style.transform = 'scale(1)';
	});
});