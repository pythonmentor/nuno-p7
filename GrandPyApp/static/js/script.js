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
  }, 2000);
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
      setTimeout(function() {
        mapGrandPyMessages(data.messages, data.position, data.tag);
      }, 3000);
    },
  });
};

var id_tags = Array();
function mapGrandPyMessages(messages, position, tag) {
  if(id_tags.includes(tag)){
    var message_ups = "Petit coquin, a faire des blagues a PaPy.., Cherche plus haut dans la conversation je te l'ai déja trouvé!! Ha les jeauneaux..Renenons a nos mouttons.. Que veux-tu que je te trouve encore?"
    grandPyMessage(message_ups);
  } else{
    id_tags.push(tag);
    grandPyMessage(data.messages[0]);
    grandPyMessage(data.messages[1]);
    grandPyMessage(data.messages[2]);
    $('<div class="message loading new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure><span></span></div>').appendTo($('.mCSB_container'));
    updateScrollbar();
    setTimeout(function() {
      $('.message.loading').remove();
      $('<div class="message new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure><div id="showMap_'+tag+'"></div></div>').appendTo($('.mCSB_container')).addClass('new');
      var elmt = document.getElementById('showMap_'+tag);
      var mq = window.matchMedia("screen and (min-width: 1024px");
      if (mq.matches) {
        elmt.style.height= "300px";
        elmt.style.width= "700px";
      } else {
        elmt.style.height= "200px";
        elmt.style.width= "260px";
      }
      initMap(position, tag);
      setDate();
      updateScrollbar();
    }, 2000);
    grandPyMessage(data.messages[3]);
    setTimeout(function() {
      lastGrandPyMessage();
    }, 2000);
  };
};

var tag;
var marker;
function initMap(position, tag) {
  tag = new google.maps.Map(document.getElementById('showMap_'+ tag ),{
    center: position,
    zoom: 18,
  });
  marker = new google.maps.Marker({
    position: position,
    map: tag,
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
