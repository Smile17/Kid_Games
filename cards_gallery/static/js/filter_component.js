$(document).ready(function(){
  $("#text_filter").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#cards_container_inside >").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

$(document).ready(function(){
 var multipleCancelButtonTags = new Choices('#tags-filter', {
    removeItemButton: true,
    maxItemCount:5,
    searchResultLimit:5,
    renderChoiceLimit:5
  });
 var multipleCancelButtonPTags = new Choices('#ptags-filter', {
    removeItemButton: true,
    maxItemCount:5,
    searchResultLimit:5,
    renderChoiceLimit:5
  });
});

function filterByTags() {
ptags = $("#ptags-filter").val();
tags = $("#tags-filter").val();
const urlParams = new URLSearchParams(window.location.search);
urlParams.set('ptag', ptags);
urlParams.set('tag', tags);
window.location.search = urlParams;
}
function clearFilters() {
$('#filter_form').get(0).reset();
}
