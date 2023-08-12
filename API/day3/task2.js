// 2. Wykorzystaj endpoint https://reqres.in/api/users do wysłania zapytania POST i dodania nowego użytkownika, ciało zapytania czyli payload może być ustawiony na sztywno w kodzie.

fetch('https://reqres.in/api/users', {
    method: 'POST',
    headers: {
        'Content-Type':'application/json'
    },
    body: JSON.stringify ({
            "email": "john.lennon@reqres.in",
            "first_name": "John",
            "last_name": "Lennon",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        })
    }).then(res => {
        return res.json()
    })
    .then(data => console.log(data))
    .catch(error => console.log('ERROR'))