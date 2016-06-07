/*    JavaScript    */



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

  $('body > div').perfectScrollbar({
    wheelSpeed: 2,
    minScrollbarLength: 20
  });

}); 



/************************* XMLHttpRequest dla IE *************************/

if (typeof XMLHttpRequest == "undefined")
{
  XMLHttpRequest = function() {

    //IE wykorzystuje biblioteki ActiveX do tworzenia obiektu XMLHttpRequest
    return new ActiveXObject(

      //IE5 używa innego obektu XMLHTTP niż IE6 i wyższe
      navigator.userAgent.indexOf("MSIE 5") >=0 ? "Microsoft.XMLHTTP" : "Msxml2.XMLHTTP"

    );
  }
}

/********** Stworzenie obiektu XMLHttpRequest **********/
var xml = new XMLHttpRequest();

