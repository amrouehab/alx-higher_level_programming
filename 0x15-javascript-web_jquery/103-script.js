$(document).ready(function () {
  function fetchHello () {
    const langCode = $('#language_code').val();
    if (langCode) {
      $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function (data) {
        $('#hello').text(data.hello);
      });
    }
  }

  $('#btn_translate').click(fetchHello);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // Enter key
      fetchHello();
    }
  });
});

