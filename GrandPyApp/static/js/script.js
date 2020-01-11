var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

$(window).load(function() {
  $messages.mCustomScrollbar();
  setTimeout(function() {
    firstGrandPyMessage();
  }, 100);
});


function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

function grandPyMessage(message) {
  $('<div class="message loading new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure><span></span></div>').appendTo($('.mCSB_container'));
  updateScrollbar();
  setTimeout(function() {
    $('.message.loading').remove();
    $('<div class="message new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure>' + message + '</div>').appendTo($('.mCSB_container')).addClass('new');
    setDate();
    updateScrollbar();
  }, 3000);
}

function setDate(){
  d = new Date()
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
    $('<div class="checkmark-sent-delivered">&check;</div>').appendTo($('.message:last'));
    $('<div class="checkmark-read">&check;</div>').appendTo($('.message:last'));
  }
}

function insertMessage() {
  msg = $('.message-input').val();
  if ($.trim(msg) == '') {
    return false;
  }
  escapeHtml(msg);
  $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  $('.message-input').val(null);
  updateScrollbar();
  getMessageGrandPy(msg);
};

function escapeHtml(msg) {
  return msg
  .replace(/&/g, "&amp;")
  .replace(/</g, "&lt;")
  .replace(/>/g, "&gt;")
  .replace(/"/g, "&quot;")
  .replace(/'/g, "&#039;");
};

function getMessageGrandPy(msg) {
  $.ajax({
    data : {messageInput : msg},
    type : 'POST',
    url : '/process',
    dataType: "json",
    success: function(data) {
      data.messages.forEach(function(message) {
        grandPyMessage(message);
      });
      updateScrollbar();
      setTimeout(function() {
        mapGrandPyMessage(data.position);
      }, 3000);
      setTimeout(function() {
        lastGrandPyMessage();
      }, 3000);
    },
  });
};

function mapGrandPyMessage(position) {
  var cnt = 0;
  for(i=1;i<=cnt;i++){
  let id_count = document.getElementById('map'+i).value()};
  $('<div class="message loading new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure><span></span></div>').appendTo($('.mCSB_container'));
  $('<div class="message new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure>' + '<div id="showMap"><div id="'+ id_count +'"></div></div>' + '</div>').appendTo($('.mCSB_container')).addClass('new');;
  $('.message.loading').remove();
  initMap(position, id_count);
  /*$('<div class="message new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure><div id="showMap"><div id=' + "map"+i +'></div></div></div>').appendTo($('.mCSB_container')).addClass('new');*/
    setDate();
  updateScrollbar();
};

function initMap(position, i) {
  map = new google.maps.Map(document.getElementById(i),{
    center: position,
    zoom: 18,
  });
  marker = new google.maps.Marker({
    position: position,
    map: map,
  });
};

$('.message-submit').click(function() {
  insertMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  };
});
last = "Voilà petit fou! Une autre Question a me soumetre ?"
function firstGrandPyMessage() {
  if ($('.message-input').val() != '') {
    return false;
  }
  msg = "Salut coquinou, je suis GrandPy, J'aime bien"+
  " trouver des lieux mais je suis un peut rouillé"+
  " alors sois gentil avec moi,j'aime bien radotter sur"+
  " ce qui est la vie, mais en quoi je puis t'aider?ZZZzzz "

  grandPyMessage(msg);
};
function lastGrandPyMessage() {
  if ($('.message-input').val() != '') {
    return false;
  }
  last = "Voilà petit fou! Une autre question a me soumetre ? Profite je suis de bonne humeur!"
  grandPyMessage(last);
};

$('.button').click(function(){
  $('.menu .items span').toggleClass('active');
  $('.menu .button').toggleClass('active');
});
