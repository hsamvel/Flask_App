document.getElementById("copy-text").addEventListener("paste", myFunction);
function myFunction() {
  var yourdiv = document.getElementById("copy-text");
          setTimeout(() => {
          let elms = yourdiv.getElementsByTagName("img").item(0)
           console.log(elms.src)
        $.ajax({
            type: 'post',
            url: '/my_url_video',
            data: JSON.stringify(elms.src),
            contentType: "application/json; charset=utf-8",
            success: function (data) {
        }
});
        }, 0);
}
