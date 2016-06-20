/*    JavaScript    */

"use strict"; 



$(document).ready(function () 
{


  // rozmiary tapety

  var G_adres_tapety = $( '#TRESC > .BLOK1 > .tlo' ).css( 'background-image' );

  G_adres_tapety = G_adres_tapety.replace( 'url("', '' ).replace( '")', '' );

  pobierz.wymiary_grafiki(G_adres_tapety);




  // Wybierz filtr

  var G_numer_filtra = parseInt( $( '#FILTRY .lista > span' ).html() );

  if( G_numer_filtra )
  {
    zmiana.przelacznik_zakladek( '#FILTRY', G_numer_filtra );

    $(window).load(function()
    {
    
      $( '#FILTRY .zakladka_'+ G_numer_filtra +' .focus' ).focus();

    });
  }



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
      ruch.pokaz_produkt( adres );

    else if( guzik == 2 )
      window.open( adres, '_blank' );

  });


  /********* Ukrywanie produktu *********/

  $( '#PRODUKT > .tlo' ).click(function (event)
  {

    event.stopPropagation();
    var guzik = pobierz.ktory_guzik(event);

    if( guzik == 1 || guzik == 2 )
      ruch.ukryj_produkt();
  
  });


  /********* FILTRY - ZAKŁADKI *********/

  $( '.filtry > .lista > div' ).not( '.link' ).click(function () 
  {
  
    zmiana.przelacznik_zakladek( '#' + $(this).parent().parent().attr( 'id' ), $(this).data( 'numer' ) );

    wyslij.numer_filtra( $(this).data( 'numer' ) );
  
  });


  /********* SCROLLBAR - Przesunięcie guzikiem *********/

  $( '#TRESC .strzalka > .obrazek, #TRESC .strzalka > .podpis' ).mousedown(function () 
  {
  
    ruch.pozycja_scrollbara( $(this).parent().data( 'href' ) );
  
  });


  /********* NAGLOWEK - Dostosowanie wysokosci *********/

  $( 'body > div' ).scroll(function () 
  {
  
    var top = parseInt( $(this).scrollTop() );

    if( top != 0 )
      zmiana.zmniejsz_naglowek();

    else
      zmiana.zwieksz_naglowek();

  });

});





$(document).ready(function () {


  $(window).load(function () {

    var szerokosc_scrollbara = $( 'body > div' ).css( 'padding-right' ); 

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

  $( 'body > div' ).perfectScrollbar({
    wheelSpeed: 2,
    minScrollbarLength: 20
  });

  $( 'select[ multiple=multiple ]' ).perfectScrollbar({
    wheelSpeed: 2,
    minScrollbarLength: 20
  });

}); 

