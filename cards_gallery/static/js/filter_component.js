const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

$(document).ready(function(){
    let showTags = sessionStorage.getItem("showTags", false);

    if (showTags == "true") {
        $(".tags").show();
        $("#showTags").prop('checked', true);
    }
    else {
        $(".tags").hide();
        $("#showTags").prop('checked', false);
    }
    let showFilters = sessionStorage.getItem("showFilters", false);
    if (showFilters == "true") {
        $("#filter-navbar").show();
    }
    else {
        $("#filter-navbar").hide();
    }

  $("#text_filter").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#cards_container_inside >").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

$("#showTags").change(function() {
    if(this.checked) {
        $(".tags").show();
    }
    else {
        $(".tags").hide();
    }
    sessionStorage.setItem("showTags", this.checked);
});

$("#filter_button").click(function() {
    $("#filter-navbar").toggle();
    sessionStorage.setItem("showFilters", $('#filter-navbar').css('display') != 'none');
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

