/*    JavaScript    */

"use strict"; 


var DOMENA = location.protocol + '//' + location.hostname + ':' + location.port;


/*********************** POBIERANIE DANYCH ***********************/


var pobierz = (function()
{

  function _zmienne_wysokosc()
  {

    var obiekt = 
    {
      strona : $(window).height(),
      naglowek : $( '#NAGLOWEK' ).outerHeight(),
      stopka : $( '#STOPKA' ).outerHeight(),

      padding : parseInt( $( '#TRESC' ).css( 'padding-top' ) )
        + parseInt( $( '#TRESC' ).css( 'padding-bottom' ) ),
      margin : parseInt( $( '#TRESC' ).css( 'margin-top' ) )
        + parseInt( $( '#TRESC' ).css( 'margin-bottom' ) )
    }

    return obiekt;

  }



  var udostepnione = 
  {

    zmienne_wysokosc : _zmienne_wysokosc

  }

  return udostepnione;

})();




/*********************** ZMIANA ***********************/



var zmiana = (function()
{


  function _zmniejsz_naglowek()
  {

    var $naglowek = $( '#NAGLOWEK > div' );

    var wysokosc = parseInt( $naglowek.parent().css( 'max-height' ) );
    var wysokosc_rzeczywista = $naglowek.outerHeight();


    if( wysokosc == wysokosc_rzeczywista )
    {

      var $pole_menu = $naglowek.children( '.menu' );
      var $wyszukiwarka = $naglowek.children( '.wyszukiwarka' );
      var $logo = $naglowek.children( '.tytul' );
      var $after = $logo.children();
      
      var logo_wysokosc = wysokosc - 30;
      var logo_szerokosc = logo_wysokosc * ($logo.outerWidth() / wysokosc);
      var after_wysokosc = wysokosc - 30;
      var after_szerokosc = after_wysokosc * ($after.outerWidth() / wysokosc);

      $naglowek.parent().height( wysokosc - 30 );
      $pole_menu.css({ 'position' : 'relative', 'top' : '-30px' });
      $wyszukiwarka.css({ 'position' : 'relative', 'top' : '-30px' });

      $logo.height( logo_wysokosc )
           .width( logo_szerokosc );
      $after.height( after_wysokosc )
            .width( after_szerokosc )
            .css( 'background-size', logo_szerokosc +'px auto' )
            .css( 'left', logo_szerokosc );

    }

  }



  function _zwieksz_naglowek()
  {

    var $naglowek = $( '#NAGLOWEK > div' );

    var wysokosc = parseInt( $naglowek.parent().css( 'max-height' ) );
    var wysokosc_rzeczywista = $naglowek.outerHeight();


    if( wysokosc != wysokosc_rzeczywista )
    {

      var $pole_menu = $naglowek.children( '.menu' );
      var $wyszukiwarka = $naglowek.children( '.wyszukiwarka' );
      var $logo = $naglowek.children( '.tytul' );
      var $after = $logo.children();
      
      var logo_wysokosc = wysokosc;
      var logo_szerokosc = wysokosc * ($logo.outerWidth() / $logo.outerHeight());
      var after_wysokosc = wysokosc;
      var after_szerokosc = after_wysokosc * ($after.outerWidth() / $after.outerHeight());

      $naglowek.parent().height( wysokosc );
      $pole_menu.css({ 'position' : 'relative', 'top' : '0px' });
      $wyszukiwarka.css({ 'position' : 'relative', 'top' : '0px' });

      $logo.height( logo_wysokosc )
           .width( logo_szerokosc );
      $after.height( after_wysokosc )
            .width( after_szerokosc )
            .css( 'background-size', logo_szerokosc +'px auto' )
            .css( 'left', logo_szerokosc );

    }

  }



  var udostepnione = 
  {

    zmniejsz_naglowek : _zmniejsz_naglowek,
    zwieksz_naglowek : _zwieksz_naglowek,

  }

  return udostepnione;

})();




/*********************** DOSTOSUJ ***********************/


var dostosuj = (function()
{


  var _wysokosc_strony = function()
  {

    var wysokosc = pobierz.zmienne_wysokosc();

    $( '#TRESC' ).css( 'min-height', (wysokosc.strona - wysokosc.naglowek - wysokosc.stopka - wysokosc.margin) );

    $( '#TRESC > .BLOK1' ).css( 'min-height', (wysokosc.strona - wysokosc.naglowek - wysokosc.margin) );

  };



  var _strone_do_scrollbara = function( szerokosc_scrollbara )
  {

    $( 'body > div' ).perfectScrollbar( 'update' );

    var display_scrollbar = $( '.ps-container > .ps-scrollbar-y-rail' ).css( 'display' );  // Wysokość stopki
    var czy_dostosowane = parseInt( $( 'body > div' ).css( 'padding-right' ) );

    if( display_scrollbar == 'none' && czy_dostosowane != 0 )
    {
      $( 'body > div' ).css( 'padding-right', '0px' );
      $( '#NAGLOWEK > div' ).css( 'right', '0px' );
    }
    else if( display_scrollbar == 'block' && czy_dostosowane != szerokosc_scrollbara )
    {
      $( 'body > div' ).css( 'padding-right', szerokosc_scrollbara );
      $( '#NAGLOWEK > div' ).css( 'right', szerokosc_scrollbara );
    }

  };



  var udostepnione = 
  {

    wysokosc_strony : _wysokosc_strony,
    strone_do_scrollbara : _strone_do_scrollbara

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


  function _post_i_odswiez( adres, dane )
  {

    $.post( DOMENA + adres, dane, function() {
      location.reload();
    })


    .fail(function() 
    {
      console.warn( 'Wystąpił błąd podczas przesyłania danych - ' + url );
    })

  }



  function _pozycja_scrollbara( element )
  {

    var aktualna_pozycja = $( 'body > div' ).scrollTop();
    var pozycja_elementu = $( element ).position();

    $( 'body > div' ).stop().animate({ scrollTop : pozycja_elementu.top  }, '500' );

  }



  var udostepnione = 
  {

    przekieruj_do : _przekieruj_do,
    post_i_odswiez : _post_i_odswiez,
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

    $( '#TRESC' ).css( 'min-height', (wysokosc.strona - wysokosc.naglowek - wysokosc.stopka - wysokosc.margin) );

    $( '#TRESC > .BLOK1' ).css( 'min-height', (wysokosc.strona - wysokosc.naglowek - wysokosc.margin) );

  };



  var _strone_do_scrollbara = function( szerokosc_scrollbara )
  {

    $( 'body > div' ).perfectScrollbar( 'update' );

    var display_scrollbar = $( '.ps-container > .ps-scrollbar-y-rail' ).css( 'display' );  // Wysokość stopki
    var czy_dostosowane = parseInt( $( 'body > div' ).css( 'padding-right' ) );

    if( display_scrollbar == 'none' && czy_dostosowane != 0 )
    {
      $( 'body > div' ).css( 'padding-right', '0px' );
      $( '#NAGLOWEK > div' ).css( 'right', '0px' );
    }
    else if( display_scrollbar == 'block' && czy_dostosowane != szerokosc_scrollbara )
    {
      $( 'body > div' ).css( 'padding-right', szerokosc_scrollbara );
      $( '#NAGLOWEK > div' ).css( 'right', szerokosc_scrollbara );
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

