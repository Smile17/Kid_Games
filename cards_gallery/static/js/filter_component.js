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

function updateCard(data, slug) {
      let parser = new DOMParser();
      let htmlDoc = parser.parseFromString(data, 'text/html');
      let id = "tags_" + slug;
      document.getElementById(id).innerHTML = htmlDoc.getElementById(id).innerHTML;
}
function deleteTags(slug, tag, form, e) {
    e.preventDefault();
    let is_populate = document.getElementById("populateCheck_" + slug).checked;
    var formData = {
      csrfmiddlewaretoken: csrftoken,
      slug: slug,
      tag: tag,
      is_populate: is_populate,
    };
    //var DELETE_URL = "{% url 'delete_tags' %}";
    var DELETE_URL = "delete_tags";
    $.ajax({
        url: DELETE_URL,
        type: "POST",
        headers: { 'x-method-override': 'DELETE' },
        data:   formData,
        success: function (data) {
          updateCard(data, slug);
          var x = document.getElementById("snackbar_del");
          x.classList.add("show");
          setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
        }
    }); // end ajax
    return false;
};

function saveTags(slug, form, e) {
    e.preventDefault();
    let tags = form.getElementsByClassName("new-tags")[0].value;
    let is_populate = form.getElementsByClassName("populate-checkbox")[0].checked;
    if (tags != '') {
        var formData = {
          csrfmiddlewaretoken: csrftoken,
          slug: slug,
          tags: tags,
          is_populate: is_populate,
        };
        //var POST_URL = "{% url 'save_tags' %}";
        var POST_URL = "save_tags";
        $.ajax({
            url: POST_URL,
            type: "POST",
            data:   formData,
            success: function (data) {
              updateCard(data, slug);
              var x = document.getElementById("snackbar");
              x.classList.add("show");
              setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
            }
        }); // end ajax
    }
    return false;
};
