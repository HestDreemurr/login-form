let res = document.querySelector("#res")

function entrar() {
  let email = document.querySelector("#email").value
  let senha = document.querySelector("#senha").value
  fetch("/auth", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email: email,
      senha: senha
    })
  })
    .then(response => response.json())
    .then(data => {
      if (data["auth"]) {
        res.innerHTML = "<p>Login realizado com sucesso!</p>"
      } else {
        res.innerHTML = "<p>E-mail ou senha incorretos! Tente novamente. </p>"
      }
    })
}