$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (films) {
  for (const film of films.results) {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  }
});
