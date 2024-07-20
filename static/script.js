let res = document.querySelector("#res")

function entrar() {
  let email = document.querySelector("#email").value
  let senha = document.querySelector("#senha").value
  if (email.length == 0 || senha.length == 0) {
    res.innerHTML = `<p style='color: red; font-weight: bolder;'>Preencha todos os campos!</p>`
    return
  }
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
        res.innerHTML = "<p style='color: red; font-weight: bolder;'>E-mail ou senha incorretos! Tente novamente.</p>"
      }
    })
}