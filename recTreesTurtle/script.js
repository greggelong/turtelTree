let greg;
let mj;
let chuko;
let mybutton


function setup() {
  createCanvas(1000, 400);
  angleMode(DEGREES);
  background(255);
  mybutton = createButton("Generate Trees");
  mybutton.mousePressed(makeTrees)

  greg = new Gurtle(10,height/2,color(255,0,0));
  mj = new Gurtle(10, height-10, color(255,255,0));
  chuko = new Gurtle(10,height-10, color(0,255,0))
  //sqr(greg);
  //sqr(mj);
  //koch(greg, 5, 500);
  //koch(mj,3,500);
  //instru();

  // set up for tree
  greg.x = width/5
  greg.y = height;
  greg.angle = -90;
  chuko.x = width-width/5
  chuko.y = height;
  chuko.angle = -90;
  mj.x = width/2;
  mj.y = height;
  mj.angle = -90;
  // call tree
  //tree(greg,100, 20);
  makeTrees()
}

function makeTrees(){
  background(50);
  
  tree2(greg,100,8);
  tree1(mj,100,8);
  tree3(chuko,100,8);

}

 

function tree(t, size, angle){
  //background(255);
  // set the tree at the bottom
  
  if (size < 2){
     return;
  }else{
    // draw tree
    t.forward(size);
    t.right(angle);
    tree(t,size-15,angle);
    t.left(angle*2);
    tree(t,size-15,angle);
    t.right(angle);
    t.backward(size);
    
  }
   
}

function tree1(t, sz, n){
  // recursive tree exit condition is level
  let angoff =1
  let srink = 0.67
  if(n>0){
    // go forward
    t.forward(sz);
    // branch right
    t.right(20*angoff);
    tree1(t,sz*srink,n-1);
    // branch left
    t.left(40*angoff);
    tree1(t,sz*srink,n-1);
    // move angle back to center and go backwards
    t.right(20*angoff)
    t.backward(sz)

  }
}

function tree2(t, sz, n){
  // random recursive tree two or three branches
  let angoff = random(1.1,3,1)
  let srink = random(0.5,0.8)
  if(n>0){
    // go forward
    t.forward(sz);
    // branch right // always branch right
    t.right(20*angoff);
    tree2(t,sz*srink,n-1);
    if (random([0,0,1]) === 0){
      //three branches
      t.left(20*angoff);
      tree2(t,sz*srink,n-1);
      t.left(20*angoff);
      tree2(t,sz*srink,n-1);
    }else{
      // only two branches
      t.left(40*angoff);
      tree2(t,sz*srink,n-1);
    }
    // move angle back to center and go backwards
    t.right(20*angoff)
    t.backward(sz)

  }
}

function tree3(t, sz, n){
  // random recursive tree two or three branches
  let angoff = random(1.1,3,1)
  let srink = random(0.5,0.8)
  let choi = random([0,1])
  if(n>0){
    // go forward
    t.forward(sz);
    if(choi === 1){
      let onechoi = random([0,1,2])
      // only one branch left, right or straight
      if(onechoi === 0){
        // to the right
        t.right(20*angoff);
        tree3(t,sz*srink,n-1);
        t.left(20*angoff); // return to center
      }else if(onechoi ===1){
        // to the left
        t.left(20*angoff);
        tree3(t,sz*srink,n-1);
        t.right(20*angoff); // return to center
      }else{
        //straight
        tree3(t,sz*srink,n-1);

      }
    }else{
      // branch right // always branch right
      t.right(20*angoff);
      tree3(t,sz*srink,n-1);
      if (random([0,0,1]) === 0){
        //three branches
        t.left(20*angoff);
        tree3(t,sz*srink,n-1);
        t.left(20*angoff);
        tree2(t,sz*srink,n-1);
      }else{
        // only two branches
        t.left(40*angoff);
        tree3(t,sz*srink,n-1);
      }
      // move angle back to center and go backwards
      t.right(20*angoff)
  }
    t.backward(sz)

  }
}

