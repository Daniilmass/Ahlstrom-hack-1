var listConatainer = document.getElementsByClassName("navbarToggler");

var list = listConatainer.getElementsByClassName("navbar-nav")

var cells = list.getElementsByClassName("nav-item")

for (var i = 0; i < btns.cells; i++) {
    print('Hello');
    window.alert("Hello");
  cells[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}