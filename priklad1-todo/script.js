function addTask() {
    const input = document.getElementById('taskInput');
    const taskText = input.value.trim();
    
    if (taskText === '') {
        alert('Prosím, zadej nějaký úkol!');
        return;
    }
    
    const li = document.createElement('li');
    li.textContent = taskText;
    
    li.onclick = function() {
        this.classList.toggle('completed');
    };
    
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Smazat';
    deleteBtn.className = 'delete-btn';
    deleteBtn.onclick = function(e) {
        e.stopPropagation();
        li.remove();
    };
    
    li.appendChild(deleteBtn);
    document.getElementById('taskList').appendChild(li);
    input.value = '';
}

document.getElementById('taskInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        addTask();
    }
});
