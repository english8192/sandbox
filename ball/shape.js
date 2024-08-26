export function createShape(x, y, width, height, speedX, speedY, color) {
    const canvas = document.getElementById('myCanvas');

    return {
        x: x,
        y: y,
        rect :[(x,y),(x+width,y),(x,y+height),(x+width,y+height)],
        width: width,
        height: height,
        speedX: speedX,
        speedY: speedY,
        color : `#${Math.floor(Math.random() * 16777215).toString(16)}`,

        move: function() {
            // Check if the shape hits the canvas boundaries horizontally
            if (this.x + this.width >= canvas.width || this.x  <= 0) {
                this.speedX = -this.speedX;
            }
            
            // Check if the shape hits the canvas boundaries vertically
            if (this.y + this.height  >= canvas.height || this.y  <= 0) {
                this.speedY = -this.speedY;
            }

            // Update position
            this.x += this.speedX;
            this.y += this.speedY;
        },
        getPoints: function() {
            let vectors = []
            let points  = [{x:this.x,y:this.y},{x:this.x+this.width,y:this.y},{x:this.x,y:this.y+this.height},{x:this.x+this.width,y:this.y+this.height}]

            for (let i = 0; i <= points.length - 1; i++) {
                const p1 = points[i];
                const p2 = points[(i+1) % points.length];

                const vector = {
                    x:p2.x - p1.x,
                    y:p2.y - p1.y
                };
                vectors.push(vector)
        }
        return [points,vectors]
    }
}
}