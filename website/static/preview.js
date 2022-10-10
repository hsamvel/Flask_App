document.addEventListener('DOMContentLoaded', function() {
const theArray = {{ theArray|safe }}
let text = ""
for (let i = 0; i < theArray.length; i++) {
    text += " " + theArray[i];
}
    var div = document.createElement('div');
    div.id = "container";
    div.innerHTML = text;
    document.body.appendChild(div);
}, false);
