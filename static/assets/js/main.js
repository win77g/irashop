$(document).ready(function () {


//подсчет сум товаров и вывод в итого в корзине и оплате
  function calculatingBasketAmount(){
      var total_order_amount = 0;

      $('.tot').each(function () {

          // console.log($(this).text());

          total_order_amount += parseInt($(this).text());
      });
         $('.total_order_amount').text(total_order_amount.toFixed(2));

  };

  // подсчет количества и суммы в корзине и оплате
  $(document).on('change', "#qty",function () {

      var current_nmb = $(this).val();
      // console.log(current_nmb);
      var current_tr = $(this).closest('tr');
      var current_price = parseInt(current_tr.find('.product-price').text());
      var total_amount = current_nmb * current_price;
      current_tr.find('.tot').text(total_amount.toFixed(2));


      calculatingBasketAmount();
  });
// searchbar
           var sp = document.querySelector('.search-open');
           var searchbar = document.querySelector('.search-inline');
           var shclose = document.querySelector('.search-close');
           function changeClass() {
               searchbar.classList.add('search-visible');
           }
           function closesearch() {
               searchbar.classList.remove('search-visible');
           }
           sp.addEventListener('click', changeClass);
           shclose.addEventListener('click', closesearch);



          


});
