$(".jumbotron").css({ height: $(window).width() + "px" });

$(window).on("resize", function() {
  $(".jumbotron").css({ height: $(window).width() + "*3768/7478px" });
});
