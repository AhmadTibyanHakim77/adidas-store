<?php
require_once __DIR__ . '/../includes/config.php';
if (!is_admin()) redirect('pages/login.php');
$page_title = 'Manage Products';
$page_description = 'Manage Adidas products';
include __DIR__ . '/../includes/navbar.php';
$products = get_products(100);
?>
<main class="py-5">
  <div class="container">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h1 class="fw-bold">Products</h1>
      <a href="<?= url('admin/index.php') ?>" class="btn btn-outline-dark">Back</a>
    </div>
    <div class="table-responsive glass-card p-3">
      <table class="table align-middle">
        <thead><tr><th>Product</th><th>Category</th><th>Price</th><th>Stock</th></tr></thead>
        <tbody>
          <?php foreach ($products as $product): ?>
          <tr><td><?= escape($product['name']) ?></td><td><?= escape($product['category_name']) ?></td><td><?= format_price($product['price']) ?></td><td><?= (int)$product['stock'] ?></td></tr>
          <?php endforeach; ?>
        </tbody>
      </table>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
