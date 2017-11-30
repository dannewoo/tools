var doc = app.activeDocument;
var p = doc.pathItems;
//Range -200*PI - 200*PI 
var delta = 400*Math.PI/40000;
var mag = 100;    
 for ( var j=0; j<40; j++)
 {
    var shape = p .add();
    shape.strokeWidth = 0.3;
    shape.closed = false;
    shape.filled = false;
    var pathPoints = [];
    $.writeln(j);
    for ( var i =0; i< 1000; i++)
    {
        var t = -200*Math.PI + delta*(j*1000+i);
        X_t = Math.sin(4.01*t) + Math.sin(3*t);
        Y_t = Math.sin(2.005*t) + Math.sin(1.01*t);
        X_t = mag*X_t;
        Y_t = mag*Y_t;
        var currentPoint = [X_t, Y_t];
        pathPoints.push(currentPoint);
    }
    shape.setEntirePath(pathPoints);
    shape.translate(300, -300);
}