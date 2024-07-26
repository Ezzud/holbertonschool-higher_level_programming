fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(obj => displayObject(obj));

function displayObject(obj) {
  document.querySelector('#character').textContent = `${obj.name}`;
}
