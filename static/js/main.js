let theme = document.getElementById("theme-link");
let darkSwitch = document.getElementById("darkSwitch");
window.addEventListener("load", function () {
    if (darkSwitch) {
        initTheme();
        darkSwitch.addEventListener("change", function () {
            resetTheme();
        });
    }
});

function initTheme() {
    let darkThemeSelected = localStorage.getItem("darkSwitch") !== null && localStorage.getItem("darkSwitch") === "dark";
    darkSwitch.checked = darkThemeSelected;
    if (darkThemeSelected) {
        document.body.setAttribute("data-theme", "dark");
        theme.href = "/static/css/mdb.dark.min.css";
    } else {
        document.body.removeAttribute("data-theme");
        theme.href = "/static/css/mdb.min.css";
    }
}

function resetTheme() {
    if (darkSwitch.checked) {
        document.body.setAttribute("data-theme", "dark");
        localStorage.setItem("darkSwitch", "dark");
        theme.href = "/static/css/mdb.dark.min.css";
    } else {
        document.body.removeAttribute("data-theme");
        localStorage.removeItem("darkSwitch");
        theme.href = "/static/css/mdb.min.css";
    }
}

// Auto close alerts
let alert = document.getElementsByClassName("alert");
setTimeout(function () {
    if (alert && alert.length) {
        alert[0].classList.add('d-none');
    }
}, 3000);

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
