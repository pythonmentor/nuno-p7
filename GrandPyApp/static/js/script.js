var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

$(window).load(function() {
  $messages.mCustomScrollbar();
  setTimeout(function() {
    grandPyMessage("none");
  }, 100);
});


function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
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
  console.log(msg);
  if ($.trim(msg) == '') {
    return false;
  }
  $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  getMessageGrandPy(msg)
  $('.message-input').val(null);
  updateScrollbar();
  setTimeout(function() {
    grandPyMessage();
  },
  1000 + (Math.random() * 20) * 100);
};

function getMessageGrandPy(msg) {
   $.ajax({
    data : {messageInput : msg},
    type : 'POST',
    url : '/process',
    dataType: "json",
    success: function(data) {
      grandPyMessage(data.message);
    },
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


function grandPyMessage(msg) {
  if ($('.message-input').val() != '') {
    return false;
  }
  if (msg == "none") {
    msg = "Salut coquinou, je suis GrandPy, J'aime bien"+
    " trouver des lieux mais je suis un peut rouillé"+
    " alors sois gentil avec moi,j'aime bien radotter sur"+
    " ce qui est la vie, mais en quoi je puis t'aider?ZZZzzz"

    $('<div class="message loading new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure><span></span></div>').appendTo($('.mCSB_container'));
    updateScrollbar();
    setTimeout(function() {
      $('.message.loading').remove();
      $('<div class="message new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure>' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
      setDate();
      updateScrollbar();
    }, 1000 + (Math.random() * 20) * 100);
  };
  if (Array.isArray(msg)) {
    msg.forEach((item) => { $('<div class="message loading new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure><span></span></div>').appendTo($('.mCSB_container'));
    updateScrollbar();
    setTimeout(function() {
      $('.message.loading').remove();
      $('<div class="message new"><figure class="avatar"><img src="../static/images/papy.gif" /></figure>' + item + '</div>').appendTo($('.mCSB_container')).addClass('new');
      setDate();
      updateScrollbar();
    }, 1000 + (Math.random() * 20) * 100);
    });
  };
};

$('.button').click(function(){
  $('.menu .items span').toggleClass('active');
   $('.menu .button').toggleClass('active');
});