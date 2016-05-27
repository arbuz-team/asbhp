/*    JavaScript    */



var DOMENA = location.protocol + '//' + location.hostname + ':' + location.port;



$(document).ready(function () 
{

  $('.link').click(function () 
  {
  
    ruch.przekieruj_do( $(this).data('domena'), $(this).data('href') );
  
  });



  $('#TRESC .strzalka > .obrazek, #TRESC .strzalka > .podpis').click(function () 
  {
  
    ruch.pozycja_scrollbara( $(this).parent().data('href') );
  
  });

});



$(document).ready(function () {
  $(window).load(function () {

    var szerokosc_scrollbara = $('body > div').css( 'padding-right'); 

    dostosuj.wysokosc_strony();
    dostosuj.strone_do_scrollbara( szerokosc_scrollbara );

    $(window).resize(function(){
    
      dostosuj.wysokosc_strony();
      dostosuj.strone_do_scrollbara( szerokosc_scrollbara );
    
    });

  }); 
}); 



jQuery(document).ready(function ($) { 
  "use strict"; 
  $('body > div').perfectScrollbar();
}); 

