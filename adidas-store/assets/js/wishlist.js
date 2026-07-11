document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('a[href*="wishlist.php"]').forEach((link) => {
    link.addEventListener('click', () => {
      link.innerHTML = '<i class="fa-solid fa-heart"></i>';
    });
  });
});
