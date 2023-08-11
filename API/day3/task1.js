// Wykorzystaj endpoint https://reqres.in/api/users?page=1 do pobrania listy użytkowników. Wynik powinen wyświetlić się w konsoli w sposób sformatowany

fetch('https://reqres.in/api/users?page=1 ')
    .then(res => res.json())
    .then((data) => {
        let users = data.data
        for (let i=0; i < users.length; i++){
            console.log("First name: " + users[i].first_name)
            console.log("Last name: " + users[i].last_name)
            console.log("Email: " + users[i].email)
            console.log("Avatar: " + users[i].avatar)
        }
    })
