document.getElementById('auth-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Previne comportamentul implicit de trimitere a formularului

    // Obține elementele de input pentru username si parola
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    // Trimite datele de autentificare ca un payload JSON folosind o cerere POST
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // Specifica tipul de continut ca fiind JSON
        },
        body: JSON.stringify({username: usernameInput.value, password: passwordInput.value}) // Trimite username-ul si parola
    })
        .then(function(response){
            if (response.redirected) { // Daca raspunsul indica o redirectionare, se acceseaza noua adresa URL
                window.location.href = response.url;
            } else {
                return response.json() // Parseaaza raspunsul de eroare ca JSON
                    .then(errorData => {
                        // Goleste campurile de input si pune focus pe campul username
                        usernameInput.value = '';
                        passwordInput.value = '';
                        usernameInput.focus();

                        // Arunca eroarea cu mesajul din raspuns
                        throw new Error(errorData.error_message);
                    });
            }
        })
        .catch(
            error => document.getElementById('error-message').innerText = error.message // Afișeaza mesajul de eroare
        );
});
