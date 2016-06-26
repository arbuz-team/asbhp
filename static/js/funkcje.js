/*    JavaScript    */

"use strict"; 


var DOMENA = location.protocol + '//' + location.hostname + ':' + location.port;


/*********************** WYSYŁANIE ***********************/


var wyslij = (function()
{

  function _numer_filtra( numer )
  {

    $.get( DOMENA +'/oferta/f_'+ numer +'/');

  }



  var udostepnione = 
  {

    numer_filtra : _numer_filtra

  }

  return udostepnione;

})();




/*********************** POBIERANIE DANYCH ***********************/


var pobierz = (function()
{

  function _zmienne_wysokosc()
  {

    var obiekt = 
    {
      strona : $(window).height(),
      naglowek : $( '#NAGLOWEK' ).outerHeight(),
      tresc : $( '#TRESC' ).outerHeight(),
      stopka : $( '#STOPKA' ).outerHeight(),

      padding : parseInt( $( '#TRESC' ).css( 'padding-top' ) )
        + parseInt( $( '#TRESC' ).css( 'padding-bottom' ) ),
      margin : parseInt( $( '#TRESC' ).css( 'margin-top' ) )
        + parseInt( $( '#TRESC' ).css( 'margin-bottom' ) )
    }

    return obiekt;

  }



  function _ktory_guzik(evt)
  {

    var e = evt;
    var code = e.keyCode || e.which;

    return code;

  }



  function _wymiary_grafiki( adres )
  {

    var img = new Image();
    
    img.onload = function()
    {

      var obiekt = {
          width : this.width,
          height : this.height
        };

      dostosuj.tapete( obiekt );

      $(window).resize(function()
      {
        
        dostosuj.tapete( obiekt );

      });

    }

    img.src = adres;


  }



  var udostepnione = 
  {

    zmienne_wysokosc : _zmienne_wysokosc,
    ktory_guzik : _ktory_guzik,
    wymiary_grafiki : _wymiary_grafiki

  }

  return udostepnione;

})();




/*********************** ZMIANA ***********************/



var zmiana = (function()
{


  function _zmniejsz_naglowek()
  {

    var $naglowek = $( '#NAGLOWEK > div' );

    var wysokosc_naglowka = parseInt( $naglowek.parent().css( 'max-height' ) );
    var wysokosc_rzeczywista = $naglowek.outerHeight();


    if( wysokosc_naglowka == wysokosc_rzeczywista && wysokosc_rzeczywista != 70 )
    {

      var $pole_menu = $naglowek.children( '.menu' );
      var $wyszukiwarka = $naglowek.children( '.wyszukiwarka' );
      var $logo = $naglowek.children( '.tytul' );
      var $after = $logo.children();
      
      var logo_wysokosc = wysokosc_naglowka - 30;
      var logo_szerokosc = logo_wysokosc * ($logo.outerWidth() / wysokosc_naglowka);
      var after_wysokosc = wysokosc_naglowka - 30;
      var after_szerokosc = after_wysokosc * ($after.outerWidth() / wysokosc_naglowka);

      $naglowek.height( wysokosc_naglowka - 30 );
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

    var wysokosc_naglowka = parseInt( $naglowek.parent().css( 'max-height' ) );
    var wysokosc_rzeczywista = $naglowek.outerHeight();


    if( wysokosc_naglowka != wysokosc_rzeczywista && wysokosc_naglowka != 70 )
    {

      var $pole_menu = $naglowek.children( '.menu' );
      var $wyszukiwarka = $naglowek.children( '.wyszukiwarka' );
      var $logo = $naglowek.children( '.tytul' );
      var $after = $logo.children();

      $naglowek.height( '' );
      $pole_menu.css( 'top', '' );
      $wyszukiwarka.css( 'top', '' );

      $logo.height( '' )
           .width( '' );
      $after.height( '' )
            .width( '' )
            .css( 'background-size', '' )
            .css( 'left', '' );

    }

  }



  function _przelacznik_zakladek( element, numer )
  {

    var $filtry = $(element);
    var $lista = $filtry.children( '.lista' );
    var $zakladki = $filtry.children( '.zakladka' );

    $lista.children( '.wybrana' ).removeClass( 'wybrana' );
    $lista.children( '[data-numer="'+ numer +'"]' ).addClass( 'wybrana' );
    
    $filtry.children( '.zakladka.wybrana' ).removeClass( 'wybrana' ).fadeOut(200, 
      function() 
      {
        $filtry.children( '.zakladka_' + numer ).fadeIn(200).addClass( 'wybrana' );
      });

  }



  function _pokaz_produkt( dane )
  {

    var $produkt = $( '#PRODUKT' );
    var $tresc = $produkt.children( '.tresc' );
    
    $tresc.html( dane ).parent().addClass( 'pelny' ).show(200);

  }



  function _ukryj_produkt( dane )
  {

    var $produkt = $( '#PRODUKT' );
    var $tresc = $produkt.children( '.tresc' );
    
    $tresc.html( '' ).parent().removeClass( 'pelny' ).hide(200);

  }



  function _pokaz_menu()
  {

    var $menu = $( '#MENU' );

    $menu.children( '.nakladka' ).fadeIn(100);
    $menu.animate({ right : '0px' }, 200, function()
    {
    
      $( '#MENU > .nakladka' ).click(function ()
      {
      
        zmiana.ukryj_menu();

      });

    });

  }



  function _ukryj_menu()
  {

    var $menu = $( '#MENU' );

    $menu.children( '.nakladka' ).fadeOut(100);
    $menu.animate({ right : '-300px' }, 200);

  }



  function _ukryj_ladowanie()
  {

    var $body = $( '#BLOK_GLOWNY' );

    $body.fadeIn(300);

  }



  var udostepnione = 
  {
    zmniejsz_naglowek : _zmniejsz_naglowek,
    zwieksz_naglowek : _zwieksz_naglowek,
    przelacznik_zakladek : _przelacznik_zakladek,
    pokaz_produkt : _pokaz_produkt,
    ukryj_produkt : _ukryj_produkt,
    pokaz_menu : _pokaz_menu,
    ukryj_menu : _ukryj_menu,
    ukryj_ladowanie : _ukryj_ladowanie
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

    $( '#TRESC > .BLOK1' ).css( 'min-height', (wysokosc.strona - wysokosc.naglowek - wysokosc.stopka - wysokosc.margin) );
    $( '#TRESC.start > .BLOK1' ).css( 'min-height', (wysokosc.strona - wysokosc.naglowek - wysokosc.margin) );

  };



  function _tapete( tapeta )
  {

    var miejsce = '#TRESC > .BLOK1 > .tlo';
    var okno = {
        width : $(window).width(),
        height : $(window).height() - $( '#NAGLOWEK' ).outerHeight()
      };

    if( okno.width / okno.height >= tapeta.width / tapeta.height )
      $( miejsce ).css( 'background-size', '100% auto' );

    else if( okno.width / okno.height < tapeta.width / tapeta.height )
      $( miejsce ).css( 'background-size', 'auto 100%' );

  }



  var udostepnione = 
  {

    wysokosc_strony : _wysokosc_strony
    , tapete : _tapete


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
      window.location.href = url;
    }

  }


  function _otworz_w_nowej_karcie( domena, adres )
  {

    if( domena == 'inna' )
      window.open( adres, '_blank' );

    else
    {
      var url = DOMENA + adres;
      window.open( url, '_blank' );
    }

  }



  function _pokaz_produkt( adres )
  {

    var url = DOMENA + adres;

    $.ajax({
      type: 'GET',
      url: url,

      success: function(dane)
      {

        window.history.pushState(
          { page : url },
          url,
          url);
        zmiana.pokaz_produkt(dane);
      
      },

      error: function() 
      {
      
        console.warn( 'Taki produkt nie istnieje.' );
        //window.location.href = DOMENA + '/404/';
      
      }

    });

  }



  function _ukryj_produkt()
  {

    window.history.back();
    zmiana.ukryj_produkt();

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

    var aktualna_pozycja = $( '#BLOK_GLOWNY' ).scrollTop();
    var pozycja_elementu = $( element ).position();

    $( '#BLOK_GLOWNY' ).nanoScroller();

    $( '#BLOK_GLOWNY' ).nanoScroller({ 
      scrollTo: $( element )
      ,flash: true
      ,flashDelay: 1000
    });

  }



  function _sprawdz_cofnij( url, dane )
  {

    console.log( "location: " + url + ", state: " + dane );

  };



  var udostepnione = 
  {

    przekieruj_do : _przekieruj_do,
    otworz_w_nowej_karcie : _otworz_w_nowej_karcie,
    pokaz_produkt : _pokaz_produkt,
    ukryj_produkt : _ukryj_produkt,
    post_i_odswiez : _post_i_odswiez,
    pozycja_scrollbara : _pozycja_scrollbara,
    sprawdz_cofnij : _sprawdz_cofnij

  }

  return udostepnione;

})();

