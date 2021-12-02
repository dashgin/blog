const DarkMode = () => {
    let clickedClass = "clicked"
    const body = document.body
    const lightTheme = "light"
    const darkTheme = "dark"
    let theme
    if (localStorage) {
        theme = localStorage.getItem("theme")
    }
    if (theme === lightTheme || theme === darkTheme) {
        body.classList.add(theme)

    } else {
        body.classList.add(lightTheme)
    }
    const switchTheme = e => {

        if (theme !== darkTheme) {
            body.classList.replace(lightTheme, darkTheme)
            e.target.classList.add(clickedClass)
            localStorage.setItem("theme", "dark")
            theme = darkTheme
        } else {
            body.classList.replace(darkTheme, lightTheme)
            e.target.classList.remove(clickedClass)
            localStorage.setItem("theme", "light")
            theme = lightTheme
        }
    }

    return (
        <div>
            <button style={{zIndex:9}}
                className={`icon-button px-3 d-none d-lg-inline-flex ms-2 ${theme === "dark" ? clickedClass : ""}`}
                onClick={e => switchTheme(e)}>
                <i className="fas fa-sun"></i>
            </button>

        </div>
    )
}

export default DarkMode