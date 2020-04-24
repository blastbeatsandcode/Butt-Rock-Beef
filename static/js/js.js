function SwitchToSearchBar() {
  var searchBar = document.getElementById("SearchBar");
  var unorderedList = document.getElementById("NavUL");
  //var searchButton = document.getElementById("SearchButton");
  searchBar.style.display = "inline";
  searchBar.style.marginRight = "2em";
  searchBar.style.marginLeft = "8em";
  searchBar.style.width = "100%";
  unorderedList.style.width = "100%";
  unorderedList.classList.remove("ml-auto");
  //searchButton.style.display = "none";
}

$(function() {
  // Collapse navbar on mobile when user clicks link
  //$(".navbar-nav li a:not('.dropdown-toggle')").on('click', function () {
  //  $('.navbar-collapse').collapse('hide');
  //});

  $("#search-button").click(function() { SwitchToSearchBar(); });

});
