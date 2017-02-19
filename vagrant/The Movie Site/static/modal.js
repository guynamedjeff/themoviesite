// Create a list of image elements.
var images = document.getElementsByClassName("poster");
var currentImage = null;

// Initiate modal access.
var modalVid = document.getElementById("vid01");
var captionText = document.getElementById("caption");
var modal = document.getElementById('myModal');

// Set click listener for each image via closure.
for (i = 0; i < images.length; i++) {
  image = images[i];
  image.addEventListener('click', (function(imageCopy) {
    return function() {
      var src = imageCopy.id;
      currentImage = imageCopy;
      modal.style.display = "block";
      modalVid.setAttribute("src", src);
      captionText.innerHTML = '[Click To Close]';
    };
  })(image));
}

// Get the <span> element that closes the modal.
var span = document.getElementById("caption");

// When the user clicks on <span> (x), close the modal.
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks elsewhere, close the modal.
var img01 = document.getElementById('myModal');
img01.onclick = function(e) {
  if (e.target != document.getElementById('vid01')) {
    document.getElementById('vid01').setAttribute('src', '');
    modal.style.display = "none";
  }
}