document.addEventListener('DOMContentLoaded', () => {
  const searchForms = document.querySelectorAll('form[action*="shop.php"]');
  searchForms.forEach((form) => {
    form.addEventListener('submit', () => {
      const input = form.querySelector('input[name="search"]');
      if (input && !input.value.trim()) input.value = '';
    });
  });
});
