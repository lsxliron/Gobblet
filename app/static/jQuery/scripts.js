$(document).ready(function(){


  //vars

  var selectedPeg = null;
  var selectedSqare = null;

  initBoard();

  
 

  // Changes the opacity of tile when it's clicked
  $("canvas").click(function(){
    
    //Set full opacity for all the tiles
    $("canvas").css('opacity',1);

    
    //Mark selected sqare  
    $(this).css('opacity','0.5');
    selectedSqare = $(this);
    
  });

 

  //Change the opacity of the selected peg
  $("img").click(function()
  {
    //Set all pegs to full opacity
    // $("img").css('opacity',1);
    $("img").css('-webkit-filter','invert(0%)');
    
    //Mark selected peg
    selectedPeg = $(this);
    // $(this).css('opacity', 0.8)
    $(this).css('-webkit-filter','invert(100%)');

  });


  $("#play").click(function(){

    var newPegOnBoard;
    var old_j;
    var old_i;
    
    //Get coordinates of the destination square on the board
    var sqNum = selectedSqare.attr('id').slice(-2);
    var i=sqNum.slice(0,1);
    var j=sqNum.slice(-1);
    
    
    //Get peg data
    var pegID = selectedPeg.attr('id');
    var pegClass = selectedPeg.attr('class')

    //Determine if the player place a new peg on the board or changes
    //the position of a peg on the board
    var colliders_selector = "#"+selectedPeg.attr('id')
    var obstacles_selector = "canvas";
    var hits = $(colliders_selector).collision(obstacles_selector)

    //Case we have no colisions- place new peg on the board
    if (hits.length == 0)
    {
      newPegOnBoard = true;
      animatePeg(selectedSqare,selectedPeg)

    }

    //We have collisions- player wants to move an existing peg on the board
    else
    {
      for (var t=0; t<hits.length; t++)
        console.log(hits[t])
      newPegOnBoard = false;
      var collidedCanvasID = hits[hits.length-1].id
      old_i = collidedCanvasID.slice(0,1)
      old_j = collidedCanvasID.slice(-1)
      animatePeg(selectedSqare,selectedPeg)
    }


    if (newPegOnBoard)
    {
      console.log("Place peg " + pegID + " on cv"+i+j);

     
    }

    else
      console.log("Move "+pegID +" form cv" +old_j+old_j + " to cv"+i+j);
    
    



  });


//GET THE COLISIONS TO DECIDE IF TO USE MAKE MOVE OR MOVE PEG ON THE BOARD
  $("#newGame").click(function(){
    var colliders_selector = ".mediumPegs";
    var obstacles_selector = "canvas";
    var hits = $(colliders_selector).collision(obstacles_selector)
    for (var i=0; i<hits.length; i++)
    {
      console.log($(hits[i]).attr('id'))
    }
    console.log("SSS")
    alert(hits.length)

  });
  
  







  // $("#t1").click(function(){
  //   el="#cv13"
  //   var pos = $(el).position();
  //   var w  = $(el).width();
    
    
  //   c1 = pos.left
  //   c2 = pos.top;
  //   $(this).animate({'left':c1, 'top':c2-50}, {'duration':1000});

    
  // });

  // $("#t2").click(function(){
  //   el="#cv9"
  //   var pos = $(el).position();
  //   var w  = $(el).width();
    
  //   c1 = pos.left
  //   c2 = pos.top;
  //   $(this).animate({'left':c1, 'top':c2-50}, {'duration':1000});

    
  // });
  


});


function animatePeg(square, peg)
{
  var offset=50;
  var pos = square.position();
  var x = pos.left;
  var y = pos.top;
  peg.css('position','absolute');

  if (peg.attr('id').slice(0,1) == 'b')
    offset = 65;
  console.log(offset)
  peg.animate({'left':x, 'top':y-offset}, {'duration':1000});

  //Clear selection
  peg.css('opacity',1);
  peg.css('-webkit-filter','invert(0%)');
  square.css('opacity',1)
}


//Draw the board to the display
function initBoard()
{
  var color1 = "#3399CC";
  var color2 = "#3366CC";
  
  for (var i=0 ;i<4; i++)
  {
    for (var j=0; j<4; j++)
    {
      if (j%2 == 0) 
        createParallelogram("cv" + i + j, color1);
      
      else
        createParallelogram("cv" + i + j, color2);

    }
      //Swap colors in the next row
      var temp = color1;
      color1 = color2;  
      color2 = temp; 

  }

}

function createParallelogram(canvasID, color)
{
  var canvas = document.getElementById(canvasID).getContext('2d');
  canvas.fillStyle= color;
  canvas.beginPath();
  canvas.moveTo(0, 0);
  canvas.lineTo(200, 0);
  canvas.lineTo(300, 100);
  canvas.lineTo(100, 100);
  canvas.fill()
}