/* Meta Pixel — White Irbis. ID меняется только здесь. */
(function () {
  var PIXEL_ID = '2983552958672062';
  if (!/^\d+$/.test(PIXEL_ID)) return; /* ID ещё не вставлен */
  if (/claude|localhost|^$/.test(location.hostname)) return;
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
  n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
  document,'script','https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', PIXEL_ID);
  fbq('track', 'PageView');

  /* Клик по WhatsApp / Telegram / телефону / почте = Contact */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var h = a.getAttribute('href') || '', ch = null;
    if (/wa\.me|whatsapp/.test(h)) ch = 'whatsapp';
    else if (/t\.me\//.test(h)) ch = 'telegram';
    else if (/^tel:/.test(h)) ch = 'phone';
    else if (/^mailto:/.test(h)) ch = 'email';
    else if (/instagram\.com|ig\.me|m\.me/.test(h)) ch = 'instagram';
    if (ch) fbq('track', 'Contact', { channel: ch, page: location.pathname });
  }, true);
})();
