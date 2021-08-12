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
        <label className='switch mx-auto ms-sm-1 me-sm-0'
            htmlFor='darkSwitch'>
            <input id="darkSwitch" type='checkbox'
                className={theme === "dark" ? clickedClass : ""}
                onClick={e => switchTheme(e)}>
            </input>
            <span className='slider round'></span>
            <span className='toggle-moon'><i className='fa fa-sun text-white'></i></span>
            <span className='toggle-sun'><i className='fa fa-moon text-dark'></i>️</span>
        </label>
    )
}

export default DarkMode