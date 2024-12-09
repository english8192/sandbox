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
        let w = grn(100,100)
        let l = w
        let newShape=createShape(canvas.width/2, canvas.height/2,w,l, grn(-20,20),grn(-20,20))
        shapes.push(newShape)
    }
}
genShapeAttr(2)
//console.log(shapes)

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
        let linelist = []
        let intersectlist=[]
        shapes.forEach(shape => {

            // shape.move()
            let points = shape.getPoints()
            let line1 = [points[0],points[1]]
            let line2 = [points[1],points[2]]
            let line3 = [points[2],points[3]]
            let line4 = [points[3],points[0]]
            let lines = [line1,line2,line3,line4]
            // console.log(lines)
            linelist.push(line1)
            linelist.push(line2)
            linelist.push(line3)
            linelist.push(line4)
            for (let x of lines){
                for (let i of linelist ) {
                    if (i != line1 && i != line2 && i != line3 && i != line4) {

                    let currentcheck = checkForIntersection(x,i)
                    //console.log(currentcheck)
                    if (currentcheck ==true) {
                        intersectlist.push(currentcheck)
                    }

                    
                }
            }
            }
            if (intersectlist.length > 0) {
                shape.move(true)
            } else {
                shape.move(false)
            }
        }
    )
}

    
    

function checkForIntersection(points1,points2) {
    // console.log("points1")
    // console.log(points1)
    // console.log("points2")
    // console.log(points2)
    let xa1 = points1[0].x
    let ya1 = points1[0].y
    
    let xa2 = points1[1].x
    let ya2 = points1[1].y
    
    let xb1 = points2[0].x
    let yb1 = points2[0].y
    
    let xb2 = points2[1].x
    let yb2 = points2[1].y
    console.log("points")
    console.log(xa1,ya1)
    console.log(xa2,ya2)
    console.log(xb1,yb1)
    console.log(xb2,yb2)

    function getOrientation(x1,y1,x2,y2,x3,y3) {
        let orival = ((y2-y1)*(x3-x2))-((x2-x1)*(y3-y2))
        // console.log(orival)
        return orival
    }

    let O1 = getOrientation(xa1,ya1,xa2,ya2,xb1,yb1)
    let O2 = getOrientation(xa1,ya1,xa2,ya2,xb2,yb2)
    let O3 = getOrientation(xb1,yb1,xb2,yb2,xa1,ya1)
    let O4 = getOrientation(xb1,yb1,xb2,yb2,xa2,ya2)
    // console.log(`O1: ${O1}`)
    // console.log(`O2: ${O2}`)
    // console.log(`O3: ${O3}`)
    // console.log(`O4: ${O4}`)

    // console.log(O1 * O2)
    // console.log(O3*O4)        
    return ((O1 * O2 < 0) && (O3 * O4 < 0)) 

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
    ctx.clearRect(0,0, canvas.width, canvas.height); // Clear the canvas
    //genShapeAttr(1)
    shapes.forEach(shape =>{
        ctx.fillStyle = shape.color
        ctx.strokeStyle = 'red'
        // ctx.strokeRect(shape.x, shape.y, shape.width, shape.height)
        ctx.fillRect(shape.x, shape.y, shape.width, shape.height); // Draw the rectangle
    }

    )
}
const fps = 30;

function animate() {

    //console.log('animate')
    updatePosition()
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

