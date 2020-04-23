// Collapse navbar on mobile when user clicks link
$(".navbar-nav li a:not('.dropdown-toggle')") .on('click', function () {
    $('.navbar-collapse').collapse('hide');
});

var i = 0;
function move() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("progressbar");
    var width = 1;
    var id = setInterval(frame, 1);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
      } else {
        width++;
        elem.style.width = width + "%";
	elem.innerHTML = width + "%";
      }
    }
  }
}
