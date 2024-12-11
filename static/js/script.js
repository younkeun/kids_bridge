document.addEventListener("DOMContentLoaded", function () {
    // 모바일 메뉴 토글
    const menuToggle = document.querySelector(".menu-toggle");
    const navMenu = document.querySelector("nav ul");

    if (menuToggle && navMenu) {
        menuToggle.addEventListener("click", function () {
            navMenu.classList.toggle("show");
        });
    }

    // 스크롤 애니메이션
    const animatedElements = document.querySelectorAll(".animate-on-scroll");

    const handleScrollAnimation = () => {
        animatedElements.forEach((element) => {
            const rect = element.getBoundingClientRect();
            if (rect.top < window.innerHeight - 100) {
                element.classList.add("visible");
            }
        });
    };

    document.addEventListener("scroll", handleScrollAnimation);
    handleScrollAnimation(); // 초기 스크롤 상태 확인

    // 부드러운 스크롤 효과
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute("href"));
            if (target) {
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });

    // 맨 위로 이동 버튼
    const scrollToTopBtn = document.querySelector(".scroll-to-top");

    if (scrollToTopBtn) {
        const toggleScrollToTopBtn = () => {
            if (window.scrollY > 300) {
                scrollToTopBtn.classList.add("visible");
            } else {
                scrollToTopBtn.classList.remove("visible");
            }
        };

        scrollToTopBtn.addEventListener("click", function () {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });

        window.addEventListener("scroll", toggleScrollToTopBtn);
        toggleScrollToTopBtn(); // 초기 상태 확인
    }
});
