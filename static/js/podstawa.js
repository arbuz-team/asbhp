/*    JavaScript    */

"use strict"; 



var DOMENA = location.protocol + '//' + location.hostname + ':' + location.port;



$(document).ready(function () 
{

  $('.link').click(function () 
  {
  
    ruch.przekieruj_do( $(this).data('domena'), $(this).data('href') );
  
  });



  $('.link_select > select').change(function () 
  {
  
    ruch.przekieruj_do( $(this).children(':selected').data('domena'), $(this).val() );
  
  });



  $('.wyszukiwarka > button').mouseenter(function () 
  {

    $(this).parent().children( 'input' ).focus();
  
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



  autosize( $( 'textarea' ) );

  $(window).load(function () {
  
    autosize.update( $( 'textarea' ));

  })

}); 



jQuery(document).ready(function ($) { 

  $('body > div').perfectScrollbar({
    wheelSpeed: 2,
    minScrollbarLength: 20
  });

}); 

