// main.js
import { createShape } from './shape.js';

// Get the canvas element and its context
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

const sliders = document.querySelectorAll('.control-slider')
const valueDisplay = document.getElementById('value')


function grn(x, y) {
    return Math.floor(Math.random() * (y - x + 1)) + x;
}


let shapes = []
function genShapeAttr(numShapes) {
    for (let i =0;i<numShapes;i++) {
        let w = grn(10,10)
        let l = w
        let newShape=createShape(canvas.width/2, canvas.height/2,w,l, grn(-20,20),grn(-20,20))
        shapes.push(newShape)
    }
}
genShapeAttr(2)
console.log(shapes)

function getShapeMatrix() {
    let shapeMatrix =[]
    for(let i=0;i<shapes.length;i++)
    shapeMatrix.push([x,])

}
// function stats() {

//     document.getElementById("shapeX").textContent = `shapeX = ${shapeX}`
//     document.getElementById("shapeY").textContent = `shapeY = ${shapeY}`
//     document.getElementById("speedX").textContent = `speedX = ${Math.abs(speedX)}`
//     document.getElementById("speedY").textContent = `speedY = ${Math.abs(speedY)}`

// }

function updatePosition() {
    shapes.forEach(shape => {
        shape.move()
        console.log(shape.getPoints())

    })

    
}


// function updateValue() {
//     console.log("updateValue")
//     speedX = parseFloat(document.querySelector('[control="speedX"]').value);
//     shapeWidth = parseFloat(document.querySelector('[control="shapeWidth"]').value);
//     speedY = parseFloat(document.querySelector('[control="speedY"]').value);
//     shapeHeight = parseFloat(document.querySelector('[control="shapeHeight"]').value);
//     //valueDisplay.textContent = value;
// }



function drawShape() {        
    //ctx.clearRect(0,0, canvas.width, canvas.height); // Clear the canvas
    //genShapeAttr(1)
    shapes.forEach(shape =>{
        ctx.fillStyle = shape.color
        ctx.strokeStyle = 'red'
        // ctx.strokeRect(shape.x, shape.y, shape.width, shape.height)
        ctx.fillRect(shape.x, shape.y, shape.width, shape.height); // Draw the rectangle
    }

    )
}
const fps = 120;

function animate() {

    //console.log('animate')
    updatePosition()
    //updateValue()
    drawShape()
    setTimeout(() => {
        requestAnimationFrame(animate);
      }, 1000 / fps);
    //stats()
}





animate();

// sliders.forEach(input => {
//     console.log('listener added')
//     input.addEventListener('input', updateValue)
    
// });

