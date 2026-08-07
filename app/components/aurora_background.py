import streamlit.components.v1 as components


def show():

    components.html(
        """
<!DOCTYPE html>
<html>

<head>

<style>

html,
body{

margin:0;

padding:0;

overflow:hidden;

background:transparent;

}

canvas{

position:fixed;

top:0;

left:0;

width:100vw;

height:100vh;

pointer-events:none;

z-index:-999;

}

</style>

</head>

<body>

<canvas id="aurora"></canvas>

<script>

const canvas=document.getElementById("aurora");

const ctx=canvas.getContext("2d");

let w=window.innerWidth;
let h=window.innerHeight;

canvas.width=w;
canvas.height=h;

window.addEventListener("resize",()=>{

w=window.innerWidth;
h=window.innerHeight;

canvas.width=w;
canvas.height=h;

});

let mouse={

x:w/2,
y:h/2

};

window.addEventListener("mousemove",(e)=>{

mouse.x=e.clientX;
mouse.y=e.clientY;

});

class Blob{

constructor(){

this.reset();

}

reset(){

this.x=Math.random()*w;

this.y=Math.random()*h;

this.r=180+Math.random()*120;

this.dx=(Math.random()-.5)*0.3;

this.dy=(Math.random()-.5)*0.3;

this.color=Math.random()>.5

? "139,92,246"

: "6,182,212";

}

move(){

this.x+=this.dx;

this.y+=this.dy;

this.x+=(mouse.x-this.x)*0.002;

this.y+=(mouse.y-this.y)*0.002;

}

draw(){

let g=ctx.createRadialGradient(

this.x,

this.y,

0,

this.x,

this.y,

this.r

);

g.addColorStop(

0,

`rgba(${this.color},0.18)`

);

g.addColorStop(

1,

`rgba(${this.color},0)`

);

ctx.fillStyle=g;

ctx.beginPath();

ctx.arc(

this.x,

this.y,

this.r,

0,

Math.PI*2

);

ctx.fill();

}

}

const blobs=[];

for(let i=0;i<6;i++){

blobs.push(new Blob());

}

function animate(){

ctx.clearRect(0,0,w,h);

blobs.forEach(blob=>{

blob.move();

blob.draw();

});

requestAnimationFrame(animate);

}

animate();

</script>

</body>

</html>
        """,
        height=0,
        width=0,
    )