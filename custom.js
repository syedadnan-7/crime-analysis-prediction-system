(function($) {

  // Add smooth scrolling to in-page anchors only; guard if target missing
  $(".navbar a, a.btn-appoint, .quick-info li a, .overlay-detail a").on('click', function(event) {
    var href = $(this).attr('href') || '';
    // Only handle pure fragment links ("#id") or links pointing to the same page with a fragment
    var isFragmentOnly = href.charAt(0) === '#';
    var isSamePage = !isFragmentOnly && (this.pathname === location.pathname && (!this.hostname || this.hostname === location.hostname));
    if ((isFragmentOnly || isSamePage) && this.hash) {
      var $target = $(this.hash);
      if ($target.length) {
        event.preventDefault();
        $('html, body').animate({
          scrollTop: $target.offset().top
        }, 900, function() {
          // update hash without jumping immediately
          history.replaceState && history.replaceState(null, null, this.hash || href);
        }.bind(this));
      }
    }
  });

  $(".navbar-collapse a").on('click', function() {
    $(".navbar-collapse.collapse").removeClass('in');
  });

  //jQuery to collapse the navbar on scroll
  $(window).scroll(function() {
    if ($(".navbar-default").offset().top > 50) {
      $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
      $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
  });

})(jQuery);
