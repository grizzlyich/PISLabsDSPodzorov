// ЛР9: jQuery Parallax для главной страницы
$(function () {
    const $icons = $('.icons-for-parallax img');
    const $logo = $('.logo');
    let ticking = false;

    function updateParallax() {
        const scrollTop = $(window).scrollTop();

        $icons.each(function (index) {
            const speed = [0.12, 0.20, 0.28][index] || 0.15;
            const offsetY = scrollTop * speed;
            $(this).css('transform', 'translate3d(0,' + offsetY + 'px,0)');
        });

        const logoOffset = scrollTop * 0.06;
        $logo.css('transform', 'translate3d(0,' + logoOffset + 'px,0)');
        ticking = false;
    }

    $(window).on('scroll', function () {
        if (!ticking) {
            window.requestAnimationFrame(updateParallax);
            ticking = true;
        }
    });

    updateParallax();
});
