document.getElementById("home-run").addEventListener("click", showResult);
console.log(result);

document.getElementById("home-run").addEventListener("click", showResult);
const content = document.getElementById("home-for-source-code-typings");

async function showResult() {
  let code = document.getElementById("home-for-source-code-typings").value;

  console.log(code);

  const response = await fetch("http://127.0.0.1:8000/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code: code }),
  });
  const data = await response.json();
  console.log(data);

  if (data.error === false) {
    document.getElementById("ht05").innerText = "LEXEMES:";
    document.getElementById("ht06").innerText = "TOKENS:";
    let lexeme = data.lexeme;
    let token = data.token;

    const lexemeDisplay = document.getElementById("home-text05");

    while (lexemeDisplay.firstChild) {
      lexemeDisplay.removeChild(lexemeDisplay.firstChild);
    }

    for (let i = 0; i < lexeme.length; i++) {
      let listItem = document.createElement("li");
      listItem.setAttribute("class", "list-item");

      listItem.textContent = lexeme[i];

      lexemeDisplay.appendChild(listItem);
    }

    const tokenDisplay = document.getElementById("home-text06");

    while (tokenDisplay.firstChild) {
      tokenDisplay.removeChild(tokenDisplay.firstChild);
    }

    for (let i = 0; i < token.length; i++) {
      let listItem = document.createElement("li");
      listItem.setAttribute("class", "list-item");

      listItem.textContent = token[i];

      tokenDisplay.appendChild(listItem);
    }
  } else {
    let errors = data.errors;
    let lexemes = data.lexemes;
    console.log("nag true");
    const lexemeDisplay = document.getElementById("home-text05");

    while (lexemeDisplay.firstChild) {
      lexemeDisplay.removeChild(lexemeDisplay.firstChild);
    }

    for (let i = 0; i < errors.length; i++) {
      let listItem = document.createElement("li");
      listItem.setAttribute("class", "list-item");

      listItem.textContent = errors[i];

      lexemeDisplay.appendChild(listItem);
    }

    const tokenDisplay = document.getElementById("home-text06");

    while (tokenDisplay.firstChild) {
      tokenDisplay.removeChild(tokenDisplay.firstChild);
    }

    for (let i = 0; i < lexemes.length; i++) {
      let listItem = document.createElement("li");
      listItem.setAttribute("class", "list-item");

      listItem.textContent = lexemes[i];

      tokenDisplay.appendChild(listItem);
    }
    document.getElementById("ht05").innerText = "ERRORS:";
    document.getElementById("ht06").innerText = "INVALID LEXEMES:";
  }
}
