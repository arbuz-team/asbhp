/*    JavaScript    */



function przekieruj_do(domena, adres)
{

  if( domena == 'inna' )
    window.location.href = adres;
  else if( domena == 'ta' )
    window.location.href = DOMENA + adres;

}



var dostosuj = (function()
{


  var _wysokosc_strony = function()
  {

    var wysokosc = $(window).height();    // Wysokość okna
    var wysokosc_n = $('#NAGLOWEK').outerHeight();  // Wysokość nagłówka
    var wysokosc_s = $('#STOPKA').outerHeight();  // Wysokość stopki

    // Suma marginesów i paddingów top i bottom
    var margin_padding = parseInt( $('#TRESC').css('padding-bottom') )
        + parseInt( $('#TRESC').css('padding-top') )
        + parseInt( $('#TRESC').css('margin-top') )
        + parseInt( $('#TRESC').css('margin-top') );

    $('#TRESC').css( 'min-height', (wysokosc - wysokosc_n - wysokosc_s - margin_padding) );

  };



  var _strone_do_scrollbara = function( szerokosc_scrollbara )
  {

    $('body > div').perfectScrollbar('update');

    var display_scrollbar = $('.ps-container > .ps-scrollbar-y-rail').css('display');  // Wysokość stopki
    var czy_dostosowane = parseInt( $('body > div').css('padding-right') );

    if( display_scrollbar == 'none' && czy_dostosowane != 0 )
    {
      $('body > div').css( 'padding-right', '0px' );
      $('#NAGLOWEK > div').css( 'right', '0px' );
    }
    else if( display_scrollbar == 'block' && czy_dostosowane != szerokosc_scrollbara )
    {
      $('body > div').css( 'padding-right', szerokosc_scrollbara );
      $('#NAGLOWEK > div').css( 'right', szerokosc_scrollbara );
    }

  };



  var udostepnione = 
  {

    wysokosc_strony : _wysokosc_strony,
    strone_do_scrollbara : _strone_do_scrollbara

  }

  return udostepnione;

})();

