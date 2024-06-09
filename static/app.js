// app.js
document.getElementById('guestbook-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const author = document.getElementById('author').value;
    const content = document.getElementById('content').value;
    const response = await fetch('/guestbook', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ author, content })
    });
    const result = await response.json();
    if (response.ok) {
        addGuestbookEntry(result);
        document.getElementById('guestbook-form').reset();
    } else {
        alert('Error: ' + result.detail);
    }
});

async function fetchGuestbookEntries() {
    const response = await fetch('/guestbook');
    const entries = await response.json();
    entries.forEach(addGuestbookEntry);
}

function addGuestbookEntry(entry) {
    const entryDiv = document.createElement('div');
    entryDiv.classList.add('guestbook-entry');
    entryDiv.innerHTML = `
        <strong>${entry.author}</strong> (${entry.timestamp}):<br>
        ${entry.content}
        <button onclick="deleteGuestbookEntry(${entry.id})">삭제</button>
    `;
    document.getElementById('guestbook-entries').appendChild(entryDiv);
}

async function deleteGuestbookEntry(id) {
    const response = await fetch(`/guestbook/${id}`, {
        method: 'DELETE'
    });
    if (response.ok) {
        document.location.reload();
    } else {
        alert('Error: ' + (await response.json()).detail);
    }
}

window.onload = fetchGuestbookEntries;