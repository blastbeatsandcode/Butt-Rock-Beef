function SwitchToSearchBar() {
  var searchBar = document.getElementById("SearchBar");
  var unorderedList = document.getElementById("NavUL");
  var searchBarContents = document.getElementById("SearchBarContents");
  //var searchButton = document.getElementById("SearchButton");
  searchBar.style.display = "inline";
  searchBar.style.marginRight = "2em";
  searchBar.style.marginLeft = "8em";
  searchBar.style.width = "100%";
  unorderedList.style.width = "100%";
  unorderedList.classList.remove("ml-auto");
  //searchButton.style.display = "none";
  searchBarContents.focus();
  searchBarContents.select();
}

function SearchForArtist() {
  var searchBar = document.getElementById("SearchBar");
  var searchBarContents = document.getElementById("SearchBarContents");

  if (!(window.getComputedStyle(searchBar).display === "none") && !(searchBarContents.value === "") && /\S/.test(searchBarContents.value))
  {
    window.location.href="/search/" + searchBarContents.value;
  }
}

$(function() {
  $("#search-button").click(function() {
    SearchForArtist();
    SwitchToSearchBar();
  });

  $('#SearchBarContents').keypress(function(event){
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){
      SearchForArtist();
    }
  });

});
