var w = 1000;
var h = 500;

var pie = 0;       //to store the value of pi
var N = 0;         //number of iterations (can be dropped and just replaced by a while loop to have it run indefinitely)
var count = 0;     //number of points that fall under the Gaussian
var dom = 5;       //the x-domain

function setup() {
  createCanvas(w, h);
  background(0);
  noFill();
  stroke(255,0,0);
  strokeWeight(5);
  for (i=0;i<=10*dom;i++){
    line(0.1*i*w/dom,h*(1-Gauss(i*0.1)),0.1*(i-1)*w/dom,h*(1-Gauss((i-1)*0.1)));
  }
  frameRate(70);
  pie = createDiv('');
}

function draw() {
  stroke(255);
  var x = Math.random()*dom;
  var y = Math.random();
  if (y < Gauss(x)){
    count++;
    stroke(255,0,0);
    point(x*w/dom,(1-y)*h);
  }

  point(x*w/dom,(1-y)*h);
  N++;
  pie.html("Pi =  "+(4*(count*dom/N)*(count*dom/N)));
}

function Gauss(x){return Math.exp(-x*x)} //defining the Gaussian
