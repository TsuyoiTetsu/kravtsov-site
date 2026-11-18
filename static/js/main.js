// Часы в шапке сайта.
function updateClock() {
    const clock = document.getElementById("live-clock");
    if (!clock) return;
    clock.textContent = new Intl.DateTimeFormat("ru-RU", {
        hour: "2-digit", minute: "2-digit", second: "2-digit"
    }).format(new Date());
}
updateClock();
setInterval(updateClock, 1000);

// Текущий год в подвале.
const year = document.getElementById("year");
if (year) year.textContent = new Date().getFullYear();


// Анимированный переход между страницами через кнопки навигации.
document.querySelectorAll(".page-nav .nav-link").forEach((link) => {
    link.addEventListener("click", (event) => {
        // Не мешаем открытию ссылки в новой вкладке и стандартным действиям браузера.
        if (
            event.defaultPrevented ||
            event.button !== 0 ||
            event.metaKey || event.ctrlKey || event.shiftKey || event.altKey ||
            link.target === "_blank" ||
            link.hasAttribute("download")
        ) return;

        const destination = new URL(link.href, window.location.href);
        if (destination.origin !== window.location.origin) return;
        if (destination.pathname === window.location.pathname &&
            destination.search === window.location.search) return;

        event.preventDefault();
        link.classList.add("is-activating");
        document.body.classList.add("page-leaving");

        // Небольшая пауза нужна, чтобы анимация нажатия успела проиграться.
        window.setTimeout(() => {
            window.location.href = destination.href;
        }, 190);
    });
});
