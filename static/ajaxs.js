function autocompleteAjaxwithImage(searcher, inputId,url, input_label,input_img){
     
      $("#"+searcher).autocomplete({
        source: function(request, response) {
          $.ajax({
            url: url,
            dataType: "json",
            data: {
              pokemon_filter: request.term,
              limit: 10,
            },
            success: function(data) {
              response($.map(data.results, function(item) {
                return {
                  id : item.id,
                  label: item.name,
                  value:  capitalizeFirstLetter(item.name.replaceAll("-"," ")),
                  img: item.img
                }
              }));
            },
            
          });
        },
        minLength: 3,
        select: function(event,ui){
         
          $("#"+inputId).val(ui.item.id);
          if(input_label) {
            $("#"+input_label).text(ui.item.value);
            $("#"+input_label).css("display", "block");
          }
          if(input_img) {
            $("#"+input_img).attr("src",ui.item.img);
            $("#"+input_img).css("display", "block");
            $("#"+input_img).attr("alt",ui.item.value);
          }
        }

      });
     
      $("#"+searcher).autocomplete( "instance" )._renderItem = function( ul, item ) {
        return $( "<li><div><img src='"+item.img+"' style='max-width:30px; height:auto'><span>"+item.value+"</span></div></li>" ).appendTo( ul );
      };
}
function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}