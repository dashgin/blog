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

