// let result = "";

// fetch("https://pokeapi.co/api/v2/pokemon/ditto")
//   .then((response) => response.json())
//   .then((data) => (result = data.name));
document.getElementById("home-run").addEventListener("click", showResult);
console.log(result);

document.getElementById("home-run").addEventListener("click", showResult);
const content = document.getElementById("home-for-source-code-typings");

async function showResult() {
  let code = document.getElementById("home-for-source-code-typings").value;

  console.log(code);

  const response = await fetch(`http://127.0.0.1:5000/helloworld/${code}`);
  const data = await response.json();

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
}
//test revisions