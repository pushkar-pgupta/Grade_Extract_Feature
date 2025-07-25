const fileInput = document.getElementById('files');
const fileListContainer = document.getElementById('file-list-container');

fileInput.addEventListener('change', () => {
    fileListContainer.innerHTML = ''; // Clear the previous list/message

    if (fileInput.files.length === 0) {
        fileListContainer.innerHTML = '<p class="text-white-50 m-0">Selected files will appear here...</p>';
        return;
    }

    const list = document.createElement('ul');
    list.className = 'list-group';
    fileListContainer.appendChild(list);

    for (const file of fileInput.files) {
        const reader = new FileReader();

        reader.onload = (event) => {
            const fileContent = event.target.result;
            const lines = fileContent.split('\n');
            let subjectTitle = 'Unknown Subject';

            for (const line of lines) {
                if (line.includes('Subject Title')) {
                    subjectTitle = line.split(':')[1].trim();
                    break;
                }
            }
            
            const listItem = document.createElement('li');
            listItem.className = 'list-group-item list-group-item-dark';
            listItem.textContent = `${file.name} - (${subjectTitle})`;
            list.appendChild(listItem);
        };

        reader.readAsText(file);
    }
});