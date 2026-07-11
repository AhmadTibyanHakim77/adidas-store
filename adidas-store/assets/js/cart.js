document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('form[action*="cart.php"]').forEach((form) => {
    form.addEventListener('submit', () => {
      const button = form.querySelector('button[type="submit"]');
      if (button) button.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i>';
    });
  });
});
