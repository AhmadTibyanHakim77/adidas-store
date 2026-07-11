<?php
require_once __DIR__ . '/../includes/config.php';
$page_title = 'Wishlist';
$page_description = 'Save your favorite Adidas products.';
include __DIR__ . '/../includes/navbar.php';

if (isset($_GET['action']) && $_GET['action'] === 'add' && isset($_GET['product_id'])) {
    add_to_wishlist((int)$_GET['product_id']);
    redirect('pages/wishlist.php');
}
if (isset($_GET['action']) && $_GET['action'] === 'remove' && isset($_GET['product_id'])) {
    remove_from_wishlist((int)$_GET['product_id']);
    redirect('pages/wishlist.php');
}
$items = get_wishlist_products();
?>
<main class="py-5">
  <div class="container">
    <h1 class="fw-bold mb-4">Wishlist</h1>
    <?php if (!$items): ?>
      <div class="glass-card p-5 text-center">
        <h4 class="mb-3">No saved items yet</h4>
        <a href="<?= url('pages/shop.php') ?>" class="btn btn-dark">Browse Products</a>
      </div>
    <?php else: ?>
      <div class="row g-4">
        <?php foreach ($items as $product): ?>
        <div class="col-md-6 col-lg-4">
          <div class="card-product h-100">
            <img src="<?= htmlspecialchars($product['thumbnail']) ?>" alt="<?= escape($product['name']) ?>" class="card-product-image" loading="lazy">
            <div class="p-4">
              <h5 class="fw-semibold mb-3"><?= escape($product['name']) ?></h5>
              <div class="d-flex justify-content-between align-items-center">
                <strong><?= format_price($product['price']) ?></strong>
                <a class="btn btn-outline-dark btn-sm" href="<?= url('pages/wishlist.php?action=remove&product_id=' . (int)$product['id']) ?>">Remove</a>
              </div>
            </div>
          </div>
        </div>
        <?php endforeach; ?>
      </div>
    <?php endif; ?>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
