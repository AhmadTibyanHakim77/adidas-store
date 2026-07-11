<?php
require_once __DIR__ . '/../includes/config.php';
$page_title = 'Shop Adidas';
$page_description = 'Browse premium Adidas shoes, apparel and accessories.';
include __DIR__ . '/../includes/navbar.php';

$search = $_GET['search'] ?? '';
$category = $_GET['category'] ?? '';
$sort = $_GET['sort'] ?? 'featured';
$products = get_products(12, $category ? (int)$category : null, $search, $sort);
?>
<main class="py-5">
  <div class="container">
    <div class="row g-4">
      <div class="col-lg-3">
        <?php include __DIR__ . '/../includes/sidebar.php'; ?>
      </div>
      <div class="col-lg-9">
        <div class="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3">
          <div>
            <p class="eyebrow">Discover</p>
            <h1 class="fw-bold">Adidas Collection</h1>
          </div>
          <div class="text-muted">Showing <?= count($products) ?> products</div>
        </div>
        <div class="row g-4">
          <?php foreach ($products as $product): ?>
          <div class="col-md-6 col-lg-4" data-aos="fade-up">
            <article class="card-product h-100">
              <img src="<?= htmlspecialchars($product['thumbnail']) ?>" alt="<?= htmlspecialchars($product['name']) ?>" class="card-product-image" loading="lazy">
              <div class="p-4">
                <p class="small text-muted mb-2"><?= escape($product['category_name']) ?></p>
                <h5 class="fw-semibold mb-3"><?= escape($product['name']) ?></h5>
                <p class="text-muted small"><?= htmlspecialchars(substr($product['description'], 0, 90)) ?>...</p>
                <div class="d-flex justify-content-between align-items-center mt-3">
                  <div><strong><?= format_price($product['price'] - ($product['price'] * $product['discount_percent'] / 100)) ?></strong></div>
                  <a class="btn btn-dark btn-sm" href="<?= url('pages/product-detail.php?id=' . (int)$product['id']) ?>">View</a>
                </div>
              </div>
            </article>
          </div>
          <?php endforeach; ?>
        </div>
      </div>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
