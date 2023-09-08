let header = document.querySelector("header");
let main = document.querySelector("main");
main.style.paddingTop = header.offsetHeight + "px";
let link = document.querySelector(".links");

function menu() {
  link.classList.toggle("active");
}

function toggleDiv(a) {
  a = a.parentNode.parentNode.parentNode
  replyBox = a.querySelector('.comment-box')
  if (replyBox.style.display === "block") {
		replyBox.style.display = "none";
  } else {
		replyBox.style.display = "block";
  }
}