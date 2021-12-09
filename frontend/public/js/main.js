$(document).ready(function () {
    "use strict";


    $(window).on("scroll", function () {
        var fromTop = $(window).scrollTop();
        $('.navbar').toggleClass("py-0", (fromTop > 300));
    });
});

// add search icon to semantic search input
$(function () {
    "use strict";
    $("i.search").addClass("fas fa-search");
});

$(function () {
    "use strict";


    $(".submenu").before('<i class="icon-arrow-down switch"></i>');
    $(".vertical-menu li i.switch").on('click', function () {
        var $submenu = $(this).next(".submenu");
        $submenu.slideToggle(200);
        $submenu.parent().toggleClass("openmenu");
    });

    $("button.burger-menu").on('click', function () {
        $(".canvas-menu").toggleClass("open");
        $(".main-overlay").toggleClass("active");
    });

    $(".canvas-menu .btn-close, .main-overlay").on('click', function () {
        $(".canvas-menu").removeClass("open");
        $(".main-overlay").removeClass("active");
    });

    $("button.search").on('click', function () {
        $(".search-popup").addClass("visible");
    });

    $(".search-popup .btn-close").on('click', function () {
        $(".search-popup").removeClass("visible");
    });

    $(document).keyup(function (e) {
        if (e.key === "Escape") {
            $(".search-popup").removeClass("visible");
        }
    });


    // loader tab pane
    $('button[data-bs-toggle="tab"]').on('click', function () {
        $(".tab-pane").addClass("loading");
        $(".lds-dual-ring").addClass("loading");
        setTimeout(function () {
            $(".tab-pane").removeClass("loading");
            $(".lds-dual-ring").removeClass("loading");
        }, 500);
    });
    // share toggle button
    $(".post button.toggle-button").each(function () {
        $(this).on('click', function (e) {
            $(this).next('.social-share .icons').toggleClass("visible");
            $(this).toggleClass("icon-close").toggleClass("icon-share");
        });
    });

    var list = document.getElementsByClassName('spacer');
    for (var i = 0; i < list.length; i++) {
        var size = list[i].getAttribute('data-height');
        list[i].style.height = "" + size + "px";
    }

    var list = document.getElementsByClassName('data-bg-image');

    for (var i = 0; i < list.length; i++) {
        var bgimg = list[i].getAttribute('data-bg-image');
        list[i].style.backgroundImage = "url('" + bgimg + "')";
    }


});