function animation() {
    
}
jQuery(function ($) {
    setTimeout(function() {
        $('.no-slider .left').addClass('init');
        $('.no-slider .right').addClass('init');
    }, 1000)
    var fullSlider = new Swiper('.full-slider', {
        autoplay: {
            delay: 3000,
            disableOnInteraction: true,
        },
        loop: true,
        slidesPerView: 1,
        spaceBetween: 0,
        navigation: false,
        pagination: {
            el: '.full-slider .swiper-pagination',
            clickable: true
        },
        keyboard: {
            enabled: true,
            onlyInViewport: false
        },
        on: {
            init: function() {
                animation('.full-slider');
                let pagination = $('.full-slider .swiper-pagination');
                pagination.hide();

                setTimeout(function() {
                    pagination.show();
                }, 2000)

            },
            slideChange: function() {
                animation('.full-slider')
            },
            sliderMove: function() {
                let slider = $('.full-slider');
                if (slider.hasClass('animation')) {
                    $('.full-slider .swiper-slide-next .left').addClass('off')
                    $('.full-slider .swiper-slide-next .right').addClass('off');
                    $('.full-slider .swiper-slide-prev .left').addClass('off')
                    $('.full-slider .swiper-slide-prev .right').addClass('off');
                }
            }
        }
    })
})