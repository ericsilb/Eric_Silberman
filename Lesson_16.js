/**
 * Created by eric on 4/26/17.
 */
function mouse(){
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    window.addEventListener("mousemove",icon, false);

}
function icon(e) {
canvas.clearRect(0,0,1000,1000);
var xPos = e.clientX;
var yPos = e.clientY;
var pic = new Image();
pic.src = "http://clipartix.com/wp-content/uploads/2016/10/Tennis-ball-clip-art-free-vector-in-open-office-drawing-svg.jpg";
canvas.drawImage(pic, xPos - 100, yPos - 100,200,200)

}
window.addEventListener("load",mouse, false);

pic.addEventListener("load", function() { canvas.drawImage(pic,0,0,x.width,x.height)},false);