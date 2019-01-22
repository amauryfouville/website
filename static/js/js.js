$(".jumbotron").css({ height: $(window).width() + "px" });

$(window).on("resize", function() {
  $(".jumbotron").css({ height: $(window).width() + "*2931/7478px" });
});
