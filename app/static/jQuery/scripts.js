
//vars
//-----
//When turn is true: white player turn
//When turn is false: black player turn

var turn = true; 
var gameWon = false //Disable board after winning
var selectedPeg = null;
var selectedSqare = null;

$(document).ready(function()
{
  initBoard();

  // Changes the opacity of tile when it's clicked
  $("canvas").click(function()
  {
    
    //Set full opacity for all the tiles
    $("canvas").css('opacity', 1);

    
    //Mark selected sqare  
    $(this).css('opacity', '0.5');
    selectedSqare = $(this);
    
  });

 

  //Change the opacity of the selected peg
  $("img").click(function()
  {
    if ((((turn == true) && ($(this).attr('id').slice(1, 2) == 'w')) ||
              ((turn == false) && ($(this).attr('id').slice(1, 2) == 'b'))) && !(gameWon))
    {
      //Set all pegs to full opacity
      // $("img").css('opacity',1);
      $("img").css('-webkit-filter', 'invert(0%)');
    
      //Mark selected peg
      selectedPeg = $(this);
      // $(this).css('opacity', 0.8)
      $(this).css('-webkit-filter', 'invert(100%)');
    }

  });


  $("#play").click(function()
  {
    var newPegOnBoard;
    var old_j;
    var old_i;
    var collidedCanvasID = null;

    //Check that player selected a peg and a destination square
    if ((selectedPeg == null) || (selectedSqare == null))
    {
      alert("Please select a peg and a destination square, then click Play Move.")
      return
    }
    
    //Get coordinates of the destination square on the board
    var sqNum = selectedSqare.attr('id').slice(-2);
    var i=sqNum.slice(0, 1);
    var j=sqNum.slice(-1);
    
    
    //Get peg data
    var pegID = selectedPeg.attr('id');
    var pegClass = selectedPeg.attr('class');

    //Determine if the player place a new peg on the board or changes
    //the position of a peg on the board
    var colliders_selector = "#" + selectedPeg.attr('id')
    var obstacles_selector = "canvas";
    var hits = $(colliders_selector).collision(obstacles_selector);

    //Case we have no colisions- place new peg on the board
    if (hits.length == 0)
      newPegOnBoard = true;

    //We have collisions- player wants to move an existing peg on the board
    //Get the old square coordinates and the new square coordinates
    else
    {
      newPegOnBoard = false;
      collidedCanvasID = hits[hits.length-1].id;
      old_i = collidedCanvasID.slice(-2, -1)
      old_j = collidedCanvasID.slice(-1);
      
    }

    //Place new peg on the board
    if (newPegOnBoard)
    {
      console.log("Place peg " + pegID + " to cv" + i + j);
      $.ajax(
      {
        url:'/_place_new_peg_on_board/',
        method:'POST',
        data: {square_i: selectedSqare.attr('id').slice(-2, -1),
               square_j: selectedSqare.attr('id').slice(-1),
               peg:selectedPeg.attr('id')},
      
      
        success: function(data)
        {
          console.log(turn);
          if (data.result.toString() == "true")
            animatePeg(selectedSqare, selectedPeg);

          else
          {
            $("#status").attr('class','alert alert-danger')
            $("#status").text("Illegal Move!")
          }
            

          if (data.winner.toString() == "true")
          {
            // $("#status").text(getCurrentTurnColor().toString() + " won the game.")
            $("#status").text(flipColor().toString() + " won the game.")
            gameWon = true
          }
      }});//AJAX END


     }
    

    //Change position of existsing peg on the board
    else
    {
      console.log("Move " + pegID  + " form cv" + old_i + old_j + " to cv" + i + j);
      $.ajax(
      {
        url:'/_reposition_peg_on_board/',
        method:'POST',
        data: {square_new_i: selectedSqare.attr('id').slice(-2, -1),
               square_new_j: selectedSqare.attr('id').slice(-1),
               square_old_i: old_i,
               square_old_j: old_j},//OLD SQUARE IS NOT PRESENT SINCE WE MOVE THE TOP PEG
      
      
        success: function(data)
        {      
          if(data.result.toString() == "1")
            animatePeg(selectedSqare, selectedPeg);

          //Case that the player revealed opponent winning row/ col
          else if (data.result.toString() == "2")
          {
            liftPeg(selectedPeg, selectedSqare);
            turn = !(turn)
            gameWon = true;
            $("#status").text(flipColor().toString() + " won the game.")
          }
          else
            alert('Illegal move');

          if (data.winner.toString() == "true")
          {
            $("#status").text(flipColor().toString() + " won the game.")
            gameWon = true
          }

      }});//AJAX END
    }
  });


  $("#newGame").click(function()
  {
    //Reset the board and refresh page
    var answer = confirm("Are you sure you want to reset the game?");
    if (answer)
    {
      $.ajax(
        {
          url:'/_reset_board/',
          method:'POST',
          data: {},
        
        
          success: function(data)
          {
            location.reload();
        }});//AJAX END
    }
  });
});


function animatePeg(square, peg)
{
  var y_offset = 50;
  var pos = square.position();
  var x = pos.left;
  var y = pos.top;
  var x_offset = 0;
  var x_offsetMultiplier = square.attr('id').slice(-2, -1);  //Fixes animation in first column


  //Offset in case of pig beg
  if (peg.attr('id').slice(0, 1) == 'b')
    y_offset = 65;

  if (square.attr('id').slice(-2) % 10 == 0)
    x_offset = 100 + (100 * x_offsetMultiplier);
  
  
  //Make peg ready to move
  peg.css('position', 'absolute');
  peg.css('left', peg.position().left);
  peg.css('top', peg.position().top);
  
  

  peg.animate({'left':x + x_offset, 'top':y-y_offset}, {'duration':1000});

  //Clear selection
  peg.css('opacity', 1);
  peg.css('-webkit-filter','invert(0%)');
  square.css('opacity', 1);
  
  //Change status label content to say which player is is playing next
  turn = !(turn);
  
  var turnColor = "";
  if (turn)
    turnColor = "Brown";
  else
    turnColor = "Black";
  $("#status").attr('class','alert alert-success')
  $('#status').text(getCurrentTurnColor() + " player turn.")

  //Reset variables
  selectedSqare = null;
  selectedPeg = null;

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

function getCurrentTurnColor()
{
  if (turn == true)
    return "Brown"
  else
    return "Black"
}

function flipColor()
{
  if (turn == false)
    return "Brown"
  else
    return "Black"
}

function liftPeg(peg, square)
{
  peg.animate({'top':+10}, {'duration':1000});
}