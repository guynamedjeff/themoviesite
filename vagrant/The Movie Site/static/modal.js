// Code Credit: https://www.w3schools.com/howto/howto_css_modal_images.asp
//
// User changes include the addition of the 'click elsewhere to close' function to the modal.
// Also, added was the closure for setting a click listener to
// each image as well as functionality for each image.

// Create a list of image elements.
var images = document.getElementsByClassName("poster");
var currentImage = null;

// Initiate modal access.
var modalImg = document.getElementById("img01");
var modal = document.getElementById('myModal');

// Set click listener for each image via closure.
for (i = 0; i < images.length; i++) {
  image = images[i];
  image.addEventListener('click', (function(imageCopy) {
    return function() {
      currentImage = imageCopy;
      modal.style.display = "block";
      modalImg.src = currentImage.src;
    };
  })(image));
}

// Get the <span> element that closes the modal.
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal.
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks elsewhere, close the modal.
var img01 = document.getElementById('myModal');
img01.onclick = function(e) {
  if (e.target != document.getElementById('img01')) {
    modal.style.display = "none";
  }
}