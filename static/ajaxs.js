function pokemonAjax(idInput){

      $("#"+idInput).autocomplete({
        source: function(request, response) {
          $.ajax({
            url: "http://127.0.0.1:8000/pokemons/",
            dataType: "json",
            data: {
              pokemon_filter: request.term,
              limit: 10,
            },
            success: function(data) {
              console.log(data);
              response($.map(data.results, function(item) {
                console.log(item)
                return {
                  label: item.name,
                  value: item.id
                }
              }));
            },
            change: function (event, ui) {
                if(!ui.item){
                    $(event.target).val("");
                }
            },
            focus: function (event, ui) {
                return false;
            }
          });
        },
        minLength: 5,
        select: function(event, ui) {
          if (ui.item) {}
        }
      });
}