$(document).ready(function(){
  $("#text_filter").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#cards_container_inside >").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});