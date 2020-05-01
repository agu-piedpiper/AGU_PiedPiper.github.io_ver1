$(".navbar-toggler").click(function () {
  //   console.log("おした！");
  $("#bg-bk").toggleClass("bg-bk");
  $("#main").toggleClass("blur");
  $(".nav-item>a").toggleClass("c-w");
  $(".nav-item>a:after").toggleClass("bg-w");
  $(".navbar-toggler>.navbar-toggler-icon").toggleClass("navbar-icon-w");
});

$(document).click(function () {
  // クリックイベントが発生すると毎回ここ通る
  if ($(event.target).closest(".nav-link").length) {
  } else if ($(event.target).closest(".bg-bk,.show").length) {
    $(".navbar-toggler").trigger("click");
  } else {
  }
});

$(".section_top__logo>img").click(function () {
  $(this).addClass("animated jello");
});
$(".section_top__logo>img").on("animationend", function () {
  $(this).removeClass("animated jello");
});
$(function () {
  if (window.matchMedia("(max-width: 575px)").matches) {
    $("[ data-wow-delay]").attr("data-wow-delay", "0.3s");

    $(".section_top_text>.display-3").attr("data-wow-delay", "0.8s");
    $(".section_top_text>.h5").attr("data-wow-delay", "1.1s");
  }
});

// .nav-item >a{color:#fff;} .nav-item>a:after{background-color:#fff;}
