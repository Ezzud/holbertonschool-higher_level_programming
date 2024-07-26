fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(obj => displayObject(obj));

function displayObject(obj) {
  obj.results.forEach(movie => {
    document.querySelector('#list_movies').insertAdjacentHTML(
      'beforeend',
      `<li>${movie.title}</li>`
    );
  });
}
