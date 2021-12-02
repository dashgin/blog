// Auto close alerts
// let alert = document.getElementsByClassName("alert");
// setTimeout(function () {
//     if (alert && alert.length) {
//         alert[0].classList.add('d-none');
//     }
// }, 3000);
// CKEditor

// const watchdog = new CKSource.Watchdog();
//
// window.watchdog = watchdog;
//
// watchdog.setCreator((element, config) => {
//     return CKSource.Editor
//         .create(element, config)
//         .then(editor => {
//
//
//             return editor;
//         })
// });
//
// watchdog.setDestructor(editor => {
//
//
//     return editor.destroy();
// });
//
// watchdog.on('error', handleError);
//
// watchdog
//     .create(document.querySelector('#id_content'), {
//
//         toolbar: {
//             items: [
//                 'fontFamily',
//                 'heading',
//                 '|',
//                 'bold',
//                 'italic',
//                 'link',
//                 'fontSize',
//                 'fontBackgroundColor',
//                 'fontColor',
//                 'highlight',
//                 '|',
//                 'codeBlock',
//                 'removeFormat',
//                 'outdent',
//                 'indent',
//                 '|',
//                 'horizontalLine',
//                 'imageUpload',
//                 'blockQuote',
//                 'insertTable',
//                 'mediaEmbed',
//                 'undo',
//                 'redo',
//                 'bulletedList',
//                 'numberedList',
//                 'imageInsert',
//                 'restrictedEditingException',
//                 'specialCharacters',
//                 'CKFinder'
//             ]
//         },
//         language: 'en',
//         image: {
//             toolbar: [
//                 'imageTextAlternative',
//                 'imageStyle:full',
//                 'imageStyle:side',
//                 'linkImage'
//             ]
//         },
//         table: {
//             contentToolbar: [
//                 'tableColumn',
//                 'tableRow',
//                 'mergeTableCells'
//             ]
//         },
//         licenseKey: '',
//
//     })
//     .catch(handleError);
//
// function handleError(error) {
//     console.error('Oops, something went wrong!');
//     console.error('Please, report the following error on https://github.com/ckeditor/ckeditor5/issues with the build id and the error stack trace:');
//     console.warn('Build id: vw0a3cwporq3-um7key5cupya');
//     console.error(error);
// }

$(document).ready(function () {
    "use strict";


    // var $header = $(".header-default"),
        // $clone = $header.before($header.addClass("fixedd"));

    $(window).on("scroll", function () {
        var fromTop = $(window).scrollTop();
        $('header').toggleClass("fixed", (fromTop > 130));
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