document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('new-task');
    const button = document.getElementById('add-task');
    const list = document.getElementById('task-list');

    button.addEventListener('click', function() {
        const taskText = input.value.trim();
        if (taskText) {
            const item = document.createElement('li');
            item.textContent = taskText;

            const removeButton = document.createElement('button');
            removeButton.textContent = 'Remove';
            removeButton.onclick = function() {
                item.remove();
            };
            item.appendChild(removeButton);

            list.appendChild(item);

            input.value = '';
        }
    });

    list.addEventListener('click', function(event) {
        if (event.target.tagName === 'LI') {
            event.target.classList.toggle('completed');
        }
    });
});
