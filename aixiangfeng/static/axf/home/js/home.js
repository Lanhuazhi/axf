$(function(){

    initTopSwiper();

    initMenuSwiper();

})


function initTopSwiper(){

    var swiper = new Swiper("#topSwiper", {
        loop: true,
        direction:'horizontal',
        speed:500,
        autoplay:2000,
        pagination:".swiper-pagination",
        control:true,
    })
}


function initMenuSwiper(){

    var swiper = new Swiper("#swiperMenu", {
        slidesPerView: 3
    })
}