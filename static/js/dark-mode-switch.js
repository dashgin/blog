// let cssStyle = document.getElementById('style');
// let listStyles = ["css/mdb.min.css", "css/mdb.dark.min.css"];
// window.onload = function () {
//     if (localStorage && localStorage.getItem("style"))
//         cssStyle.href = localStorage.getItem("style");
// };
//
// function toggleStyle() {
//     let newStyle;
//     let previousStyle = cssStyle.href;
//
//     if (previousStyle.endsWith(listStyles[0])) {
//         newStyle = listStyles[1];
//     } else {
//         newStyle = listStyles[0];
//     }
//     cssStyle.href = newStyle;
//     if (localStorage)
//         localStorage.setItem("style", newStyle);
// }
//
// // data-target switcher
// var darkSwitch = document.getElementById("darkSwitch");
// window.addEventListener("load", function () {
//     if (darkSwitch) {
//         initTheme();
//         darkSwitch.addEventListener("change", function () {
//             resetTheme();
//         });
//     }
// });
//
// function initTheme() {
//     var darkThemeSelected =
//         localStorage.getItem("darkSwitch") !== null &&
//         localStorage.getItem("darkSwitch") === "dark";
//     darkSwitch.checked = darkThemeSelected;
//     darkThemeSelected
//         ? document.body.setAttribute("data-theme", "dark")
//         : document.body.removeAttribute("data-theme");
// }
//
//
// function resetTheme() {
//     if (darkSwitch.checked) {
//         document.body.setAttribute("data-theme", "dark");
//         localStorage.setItem("darkSwitch", "dark");
//     } else {
//         document.body.removeAttribute("data-theme");
//         localStorage.removeItem("darkSwitch");
//     }
// }
//
