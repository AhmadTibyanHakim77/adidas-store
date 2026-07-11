<?php
require_once __DIR__ . '/../includes/config.php';
$page_title = 'Contact Us';
$page_description = 'Contact Adidas Store support.';
include __DIR__ . '/../includes/navbar.php';
?>
<main class="py-5">
  <div class="container py-5">
    <div class="row g-4">
      <div class="col-lg-6">
        <p class="eyebrow">Contact</p>
        <h1 class="fw-bold mb-3">We'd love to hear from you.</h1>
        <p class="text-muted">Reach out for support, collaborations, or order assistance.</p>
      </div>
      <div class="col-lg-6">
        <div class="glass-card p-4">
          <form>
            <div class="mb-3"><label class="form-label">Name</label><input class="form-control" type="text"></div>
            <div class="mb-3"><label class="form-label">Email</label><input class="form-control" type="email"></div>
            <div class="mb-3"><label class="form-label">Message</label><textarea class="form-control" rows="4"></textarea></div>
            <button class="btn btn-dark" type="submit">Send Message</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
