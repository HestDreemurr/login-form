let res = document.querySelector("#res")

function cadastrar() {
  let nome = document.querySelector("#nome").value
  let email = document.querySelector("#email").value
  let senha = document.querySelector("#senha").value
  fetch("/criar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      nome: nome,
      email: email,
      senha: senha
    })
  })
    .then(response => response.text())
    .then(data => {
      res.innerHTML = `<p>${data}</p>`
    })
}