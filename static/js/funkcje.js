/*    JavaScript    */



/*********************** POBIERANIE DANYCH ***********************/


var pobierz = (function()
{

  function _zmienne_wysokosc()
  {

    var obiekt = 
    {
      strona : $(window).height(),
      naglowek : $('#NAGLOWEK').outerHeight(),
      stopka : $('#STOPKA').outerHeight(),

      padding : parseInt( $('#TRESC').css('padding-top') )
        + parseInt( $('#TRESC').css('padding-bottom') ),
      margin : parseInt( $('#TRESC').css('margin-top') )
        + parseInt( $('#TRESC').css('margin-bottom') )
    }

    return obiekt;

  }



  var udostepnione = 
  {

    zmienne_wysokosc : _zmienne_wysokosc

  }

  return udostepnione;

})();




/*********************** RUCH ***********************/



var ruch = (function()
{


  function _przekieruj_do( domena, adres )
  {

    if( domena == 'inna' )
      window.location.href = adres;

    else
    {
      var url = DOMENA + adres;

      $.ajax({
        type: 'HEAD',
        url: url,

        success: function() {
          window.location.href = url;
        },

        error: function() {
          console.warn( 'Taki adres nie istnieje. - ' + url );
          window.location.href = DOMENA + '/404/';
        }

      });
    }

  }



  function _pozycja_scrollbara( element )
  {

    var wysokosc_naglowka = $( '#NAGLOWEK' ).outerHeight();
    var aktualna_pozycja = $( 'body > div' ).scrollTop();
    var pozycja_elementu = $( element ).position();

    $( 'body > div' ).stop().animate({scrollTop: pozycja_elementu.top }, '500');

  }



  var udostepnione = 
  {

    przekieruj_do : _przekieruj_do,
    pozycja_scrollbara : _pozycja_scrollbara

  }

  return udostepnione;

})();




/*********************** DOSTOSUJ ***********************/


var dostosuj = (function()
{


  var _wysokosc_strony = function()
  {

    var wysokosc = pobierz.zmienne_wysokosc();

    $('#TRESC').css( 'min-height', (wysokosc.strona - wysokosc.naglowek - wysokosc.stopka - wysokosc.margin) );

    $('#TRESC > .BLOK1').css( 'min-height', (wysokosc.strona - wysokosc.naglowek - wysokosc.margin) );

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




/*********************** DOSTOSUJ ***********************/


var inna = (function()
{


  var udostepnione = 
  {


  }

  return udostepnione;

})();

