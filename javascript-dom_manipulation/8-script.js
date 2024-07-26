document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(obj => displayObject(obj));

  function displayObject(obj) {
    document.querySelector('#hello').textContent = obj.hello;
  }
});
