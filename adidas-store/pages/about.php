<?php
require_once __DIR__ . '/../includes/config.php';
$page_title = 'About Adidas Store';
$page_description = 'Learn more about Adidas Store.';
include __DIR__ . '/../includes/navbar.php';
?>
<main class="py-5">
  <div class="container py-5">
    <div class="row g-5 align-items-center">
      <div class="col-lg-6">
        <p class="eyebrow">About</p>
        <h1 class="fw-bold mb-3">Crafted for the next generation of movement.</h1>
        <p class="text-muted">We blend innovation, comfort, and timeless design to deliver an elevated shopping experience for athletes and style enthusiasts alike.</p>
      </div>
      <div class="col-lg-6">
        <div class="glass-card p-4"><img src="https://images.unsplash.com/photo-1517649763962-0c623066013b?auto=format&fit=crop&w=1000&q=80" alt="About Adidas" class="img-fluid rounded-4"></div>
      </div>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
