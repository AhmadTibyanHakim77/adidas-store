document.addEventListener('DOMContentLoaded', () => {
  const sliders = document.querySelectorAll('.swiper');
  sliders.forEach((el) => {
    new Swiper(el, {slidesPerView: 1, spaceBetween: 20, loop: true, autoplay: {delay: 3500}, pagination: {el: el.querySelector('.swiper-pagination'), clickable: true}});
  });
});
