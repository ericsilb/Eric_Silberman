/**
 * Created by eric on 4/28/17.
 */
function drag(){
    ball = document.getElementById("TennisBall");
    leftbox = document.getElementById("leftBox");

    ball.addEventListener("dragstart", startDrag, false);
    ball.addEventListener("dragend", endDrag, false);

    leftbox.addEventListener("dragenter",dragEnter,false);
    leftbox.addEventListener("dragleave",dragLeave,false);
    leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
    leftbox.addEventListener("drop",drop,false);
}
 function startDrag(e) {
     var pic = '<img id = "TennisBall" src = "http://tennisweek.com/wp-content/uploads/2014/03/Tennis-Ball.jpg">';
     e.dataTransfer.setData('Picture', pic);

 }
 function dragEnter(e){
    e.preventDefault();
    leftbox.style.background="886574";
    leftbox.style.border = "3px solid green";
 }
 function dragLeave(e){
     e.preventDefault();
     leftbox.style.background = "white";
     leftbox.style.border = "3px solid purple";
 }
 function drop(e) {
     e.preventDefault();
     leftbox.innerHTML = e.dataTransfer.getData('Picture');
     
 }
 function endDrag (e) {
     pic = e.target;
     pic.style.visibility = "hidden";

 }
 window.addEventListener("load", drag, false);