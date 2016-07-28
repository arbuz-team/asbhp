/*    JavaScript    */

"use strict"; 




// rozmiary tapety */

(function()
{
  var adres_tapety = $( '#TRESC > .BLOK1 > .tlo' ).css( 'background-image' );

  if( adres_tapety != 'none' )
  {
    adres_tapety = adres_tapety.replace( 'url("', '' ).replace( '")', '' );

    pobierz.wymiary_grafiki(adres_tapety);
  }
}());



// Wybierz filtr */

(function()
{
  var numer_filtra = parseInt( $( '#FILTRY .lista > span' ).html() );

  if( numer_filtra )
  {
    zmiana.przelacznik_zakladek_filtry( '#FILTRY', numer_filtra );

    $( '#FILTRY .zakladka_'+ numer_filtra +' .focus' ).focus();
  }
}());



//window.onpopstate = ruch.sprawdz_cofnij(event);

window.onpopstate = function(event) {
  ruch.sprawdz_cofnij( document.location, JSON.stringify(event.page) );
};



/********* Wysuwane MENU *********/

$( '.guzik_menu' ).click(function ()
{
    zmiana.pokaz_menu();
});



/********* DIV LINK *********/

$( '.link' ).mouseup(function (event)
{
  var adres = $(this).data( 'href' );
  var domena = $(this).data( 'domena' );

  var guzik = pobierz.ktory_guzik(event);

  if( guzik == 1 )
    ruch.przekieruj_do( domena, adres );

  else if( guzik == 2 )
    ruch.otworz_w_nowej_karcie( domena, adres );
});



/********* SELECT LINK *********/

$( '.link_select > select' ).change(function () 
{
  ruch.przekieruj_do( $(this).children( ':selected' ).data( 'domena' ), $(this).val() );
});



/********* SELECT POST *********/

$( '.post_select > select' ).change(function () 
{
  ruch.post_i_odswiez( $(this).parent().data( 'href' ), 
    { csrfmiddlewaretoken : $(this).parent().children( 'input[name=csrfmiddlewaretoken]' ).val(), 
      zawartosc : $(this).val() } );
});



/********* Pokazywanie produktu *********/

$( '.lista_produktow > ul > li.produkt' ).click(function (event)
{
  var adres = $(this).data( 'href' );
  var guzik = pobierz.ktory_guzik(event);

  if( guzik == 1 )
    ruch.pokaz_produkt( adres, true );

  else if( guzik == 2 )
    window.open( adres, '_blank' );
});



/********* Ukrywanie produktu *********/

$( '#PRODUKT > .tresc' ).click(function(event)
{
  var guzik = pobierz.ktory_guzik(event);

  if( guzik == 1 || guzik == 2 )
    ruch.ukryj_produkt();
});

$( '#PRODUKT > .tresc *' ).click(function(event)
{
  dostosuj.stopBubble(event);
});



/********* FILTRY - ZAKŁADKI *********/

$( '.filtry > .lista > div' ).not( '.link' ).click(function()
{
  dostosuj.stopBubble();

  if( !$(this).is( '.wybrana' ) )
  {
    zmiana.przelacznik_zakladek_filtry( '#' + $(this).parent().parent().attr( 'id' ), $(this).data( 'numer' ) );

    wyslij.numer_filtra( $(this).data( 'numer' ) );
  }
});



$( '.filtry > .lista > div' ).not( '.link' ).children( 'div' ).click(function()
{
  dostosuj.stopBubble();

  ruch.wyczysc_filtr( $(this).parent().data( 'numer' ) );
});



/********* BLOKI - ZAKŁADKI *********/

$( '#TRESC > .BLOK1 > .tresc > .zakladka_blok' ).click(function()
{
  console.log('klik');
  if( !$(this).is( '.wybrana' ) )
    zmiana.przelacznik_zakladek_bloki( $(this).data( 'numer' ) );
});



/********* SCROLLBAR - Przesunięcie guzikiem *********/

$( '.strzalka > .obrazek, .strzalka > .podpis' ).mouseup(function(event)
{
  ruch.pozycja_scrollbara( $(this).parent().data( 'href' ) );
});



/********* NAGLOWEK - Dostosowanie wysokosci *********/

$( '#BLOK_GLOWNY > div' ).scroll(function()
{
  var top = parseInt( $(this).scrollTop() );

  if( top > 30 )
    zmiana.zmniejsz_naglowek();

  else
    zmiana.zwieksz_naglowek();
});



/****************************************************************************/

$(window).resize(function()
{
  dostosuj.wysokosc_strony();
  dostosuj.strone_do_scrollbara();

  var szerokosc_strony = parseInt( $(window).width() ); 

  if( szerokosc_strony < 870 )
    zmiana.zmniejsz_naglowek();
});


