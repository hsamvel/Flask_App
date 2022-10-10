const btn = document.getElementById('btn');
// ✅ Change button text on click
btn.addEventListener('click', function handleClick() {
  const initialText = 'Click me';
  btn.innerHTML = `<span style="background-color: salmon">Please wait...<span>`;
});

const btn_1 = document.getElementById('btn1');
// ✅ Change button text on click
btn.addEventListener('click', function handleClick1() {
  const initialText = 'Click me';
  btn.innerHTML = `<span style="background-color: salmon">Please wait...<span>`;
});


const btn_2 = document.getElementById('btn2');
// ✅ Change button text on click
btn.addEventListener('click', function handleClick2() {
  const initialText = 'Click me';
  btn.innerHTML = `<span style="background-color: salmon">Please wait...<span>`;
});


function toggleText(){
  var x = document.getElementById("hide");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
function download() {
    var iframe = document.getElementById('invisible');
    iframe.src = "file.doc";
}
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}