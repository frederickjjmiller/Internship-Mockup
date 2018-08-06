/* Taken from W3 Schools - */

// Get the modal
var modal = document.getElementById('APModal');

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById('APImg');
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function(){
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}


// Get the second modal
var second_modal = document.getElementById('FPModal');

// Get the image and insert it inside the modal - use its "alt" text as a caption
var second_img = document.getElementById('FPImg');
var second_modalImg = document.getElementById("img02");
var second_captionText = document.getElementById("second_caption");
second_img.onclick = function(){
    second_modal.style.display = "block";
    second_modalImg.src = this.src;
    second_captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var second_span = document.getElementsByClassName("second_close")[0];

// When the user clicks on <span> (x), close the modal
second_span.onclick = function() {
  second_modal.style.display = "none";
}
