/**
 * Created by silbermane8514 on 4/17/2017.
 */
function shapes()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    canvas.beginPath();
    canvas.moveTo(70,90);
    canvas.lineTo(220,140);
    canvas.lineTo(250,0);
    canvas.lineTo(250,0);
    canvas.lineTo(300,140);
    canvas.lineTo(460,100);
    canvas.lineTo(350,200);
    canvas.lineTo(500,230);
    canvas.lineTo(350,280);
    canvas.lineTo(460,410);
    canvas.lineTo(300,320);
    canvas.lineTo(260,480);
    canvas.lineTo(220,320);
    canvas.lineTo(50,400);
    canvas.lineTo(180,270);
    canvas.lineTo(20,250);
    canvas.lineTo(180,200);
    canvas.lineTo(70,90);
    canvas.stroke();
    var gradient = canvas.createLinearGradient(0, 0 , 1000,1000);
    gradient.addColorStop(0,"blue");
    gradient.addColorStop(1,"yellow")
    canvas.fillStyle= gradient;
    canvas.fill();
}
window.addEventListener("load",shapes, false);
