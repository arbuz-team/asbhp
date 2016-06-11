/*    JavaScript    */

"use strict"; 



$(document).ready(function () 
{


  //window.onpopstate = ruch.sprawdz_cofnij(event);

  window.onpopstate = function(event) {
    ruch.sprawdz_cofnij( document.location, JSON.stringify(event.page) );
  };




  /********* DIV LINK *********/

  $( '.link' ).click(function () 
  {
  
    var adres = $(this).data( 'href' );
    var domena = $(this).data( 'domena' );

    if( event.which == 1 )
      ruch.przekieruj_do( domena, adres );

    else if( event.which == 2 )
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

    if( event.which == 1 )
      ruch.pokaz_produkt( adres );

    else if( event.which == 2 )
      window.open( adres,'_blank' );

  });


  /********* Ukrywanie produktu *********/

  $( '#PRODUKT > .tlo' ).click(function (event)
  {

    event.stopPropagation();

    if( event.which == 1 || event.which == 2 )
      ruch.ukryj_produkt();
  
  });


  /********* FILTRY - ZAKŁADKI *********/

  $( '.filtry > .lista > div' ).click(function () 
  {
  
    zmiana.przelacznik_zakladek( '#' + $(this).parent().parent().attr( 'id' ), $(this).data( 'href' ) );
  
  });


  /********* SCROLLBAR - Przesunięcie guzikiem *********/

  $( '#TRESC .strzalka > .obrazek, #TRESC .strzalka > .podpis' ).click(function () 
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

}); 

