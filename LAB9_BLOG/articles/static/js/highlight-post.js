// ЛР8: jQuery-эффекты для архива статей
// 1) Подсветка поста при наведении
// 2) Эффект только для логотипа

$(function () {
    $('.one-post').hover(
        function () {
            $(this).css('background-color', '#ebf5e7');
            $(this).css('border', '1px solid #0c3c2c');
        },
        function () {
            $(this).css('background-color', '#ffffff');
            $(this).css('border', '1px solid #dddddd');
        }
    );

    const $logo = $('.logo');
    if ($logo.length) {
        const originalWidth = $logo.width();
        const originalHeight = $logo.height();
        const ratio = originalHeight / originalWidth;

        $logo.hover(
            function () {
                $(this).stop(true, true).animate({
                    width: originalWidth + 20,
                    height: originalHeight + (20 * ratio)
                }, 150);
            },
            function () {
                $(this).stop(true, true).animate({
                    width: originalWidth,
                    height: originalHeight
                }, 150);
            }
        );
    }
});
