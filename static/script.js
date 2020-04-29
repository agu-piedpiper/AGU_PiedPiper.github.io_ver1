$(".navbar-toggler").click(function () {
  console.log("おした！");
  $("#bg-bk").toggleClass("bg-bk");
  $("#main").toggleClass("blur");
  $(".nav-item>a").toggleClass("c-w");
  $(".nav-item>a:after").toggleClass("bg-w");
  $(".navbar-toggler>.navbar-toggler-icon").toggleClass("navbar-icon-w");
});
// .nav-item >a{color:#fff;} .nav-item>a:after{background-color:#fff;}
