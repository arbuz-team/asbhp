/*    JavaScript    */

"use strict"; 


var DOMENA = location.protocol + '//' + location.hostname + ':' + location.port;


/*********************** WYSYŁANIE ***********************/

var wyslij = (function()
{

  function _numer_filtra( numer )
  {
    //$.get( DOMENA +'/oferta/f_'+ numer +'/');
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
    var $filtry = $(element)
      , $lista = $filtry.children( '.lista' )
      , $zakladki = $filtry.children( '.zakladka' )

    $lista.children( '.wybrana' ).removeClass( 'wybrana' );
    $lista.children( '[data-numer="'+ numer +'"]' ).addClass( 'wybrana' );
    
    $filtry.children( '.zakladka.wybrana' ).removeClass( 'wybrana' ).fadeOut(200, function() 
    {
      $filtry.children( '.zakladka_' + numer ).fadeIn(200).addClass( 'wybrana' );
    });
  }



  function _pokaz_produkt( dane, plynnosc )
  {
    var $produkt = $( '#PRODUKT' )
      , $tresc = $produkt.find( '.tresc div:first-child' )
      , $tabela = $tresc.children( '.tabela' )
      , certyfikaty = ''
      , zagrozenia = ''
      , zawody = ''
    

    for( var x in dane.certyfikaty )
      certyfikaty = certyfikaty +'<div class="piktogram" title="'+ dane.certyfikaty[x] +'" style="background-image: url(/static/img/zawody/'+ ( parseInt( x ) + 1 ) +'.png)"></div>';
    
    for( var x in dane.zagrozenia )
      zagrozenia = zagrozenia +'<div class="piktogram" title="'+ dane.zagrozenia[x] +'" style="background-image: url(/static/img/zagrozenia/'+ ( parseInt( x ) + 1 ) +'.png)"></div>';
    
    for( var x in dane.zawody )
      zawody = zawody +'<div class="piktogram" title="'+ dane.zawody[x] +'" style="background-image: url(/static/img/zawody/'+ ( parseInt( x ) + 1 ) +'.png)"></div>';

      
    $tresc.children( '.producent' ).html( dane.producent );
    $tresc.children( '.nazwa' ).html( dane.nazwa );
    $tresc.find( '.zdjecie > img' ).attr( 'src', dane.zdjecie ).attr( 'alt', dane.nazwa );

    $tabela.find( '.opis > div' ).eq(1).html( dane.opis );
    $tabela.find( '.kolor > div' ).eq(1).html( dane.kolor );
    $tabela.find( '.rozmiar > div' ).eq(1).html( dane.rozmiar );

    $tabela.find( '.certyfikaty > div' ).eq(1).html( dane.certyfikaty );
    $tabela.find( '.zagrozenia > div' ).eq(1).html( zagrozenia );
    $tabela.find( '.zawody > div' ).eq(1).html( zawody );

    $tabela.children().removeClass( 'wypelniony' );

    $tabela.find( 'div > div:nth-child(2)' ).each(function()
    {
      if( $(this).html() != '' )
        $(this).parent().addClass( 'wypelniony' );
    });

    if( plynnosc )
      $produkt.addClass( 'pelny' ).fadeIn(300).children( '.tresc' ).scrollTop( '0px' );
    else
    {
      $produkt.addClass( 'pelny' ).show();
      zmiana.ukryj_ladowanie();
    }
  }



  function _ukryj_produkt( dane )
  {
    var $produkt = $( '#PRODUKT' );
    
    $produkt.removeClass( 'pelny' ).fadeOut(200);
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
    $menu.animate({ right : '-250px' }, 200);
  }



  function _ukryj_ladowanie()
  {
    var $body = $( '#BLOK_GLOWNY' );

    $body.fadeIn(300);

    autosize( $( 'textarea' ) );
    autosize.update( $( 'textarea' ));
    dostosuj.wysokosc_strony();
    dostosuj.strone_do_scrollbara();
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



  var _strone_do_scrollbara = function()
  {
    var wysokosci = pobierz.zmienne_wysokosc()
      , strona = wysokosci.strona
      , tresc = wysokosci.naglowek + wysokosci.tresc + wysokosci.stopka
      , right = parseInt( $( '#NAGLOWEK > div' ).css( 'right' ) )

    if( strona < tresc && right == 0 )
      $( '#NAGLOWEK > div' ).css( 'right', '15px' );

    else if( right != 0 )
      $( '#NAGLOWEK > div' ).css( 'right', '0px' );
  };



  function _stopBubble(e) 
  {
    if(!e)
      var e = window.event;

    e.cancelBubble = true; 

    if(e.stopPropagation)
      e.stopPropagation();
  }


  var udostepnione = 
  {
    wysokosc_strony : _wysokosc_strony
    , tapete : _tapete
    , strone_do_scrollbara :  _strone_do_scrollbara
    , stopBubble : _stopBubble
  }

  return udostepnione;
})();




/*********************** RUCH ***********************/

var ruch = (function()
{

  var stary_adres;



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



  function _pokaz_produkt( adres, plynnosc )
  {
    var czy_oferta = window.location.pathname.split( '/' )[1]
      , id = adres.split( '/' )[2]
      , url = DOMENA +'/produkt/szczegoly/'+ id +'/'

    if( czy_oferta == 'oferta' )
    {
      stary_adres = window.location.href

      window.history.pushState(
        { page : adres },
        adres,
        adres
      );
    }
    else
      stary_adres = DOMENA +'/oferta/'

    $.get( url, function(dane)
    {
      $( 'head' ).append( '<script>'+ dane +'zmiana.pokaz_produkt( dane_produktu, '+ plynnosc +' ); </script>' );
    });
  }



  function _ukryj_produkt()
  {
    window.history.pushState(
      { page : stary_adres },
      stary_adres,
      stary_adres
    );

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

    $( '#BLOK_GLOWNY > div' ).animate( { 'scrollTop': (pozycja_elementu.top + 30) }, 400 );
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

