$( document ).ready(function() {

  $( ".cross1" ).hide();
  $( ".menu1" ).hide();
  $( ".burger" ).click(function() {
  $( ".menu1" ).slideToggle( "slow", function() {
  // $( ".burger" ).hide();
  $( ".cross1" ).show();
  });
  });
  
  $( ".cross1" ).click(function() {
  $( ".menu1" ).slideToggle( "slow", function() {
  $( ".cross1" ).hide();
  $( ".burger" ).show();
  });
  });
  
  });
  $( document ).ready(function() {

    $( ".cross2" ).hide();
    $( ".menu2" ).hide();
    $( ".config" ).click(function() {
    $( ".menu2" ).slideToggle( "slow", function() {
    // $( ".burger" ).hide();
    $( ".cross2" ).show();
    });
    });
    
    $( ".cross2" ).click(function() {
    $( ".menu2" ).slideToggle( "slow", function() {
    $( ".cross2" ).hide();
    $( ".config" ).show();
    });
    });
    
    });
    $( document ).ready(function() {

      $( ".cross3" ).hide();
      $( ".menu3" ).hide();
      $( ".banginfo" ).click(function() {
      $( ".menu3" ).slideToggle( "slow", function() {
      // $( ".burger" ).hide();
      $( ".cross3" ).show();
      });
      });
      
      $( ".cross3" ).click(function() {
      $( ".menu3" ).slideToggle( "slow", function() {
      $( ".cross3" ).hide();
      $( ".banginfo" ).show();
      });
      });
      
      });