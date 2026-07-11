<?php
require_once __DIR__ . '/../includes/config.php';
$id = (int)($_GET['id'] ?? 0);
$product = get_product($id);
if (!$product) redirect('pages/shop.php');
mark_recently_viewed($id);
$page_title = $product['name'];
$page_description = $product['description'];
include __DIR__ . '/../includes/navbar.php';
?>
<main class="py-5">
  <div class="container">
    <div class="row g-5 align-items-start">
      <div class="col-lg-6" data-aos="fade-right">
        <div class="glass-card p-4">
          <img src="<?= htmlspecialchars($product['thumbnail']) ?>" alt="<?= escape($product['name']) ?>" class="img-fluid rounded-4">
        </div>
      </div>
      <div class="col-lg-6" data-aos="fade-left">
        <p class="eyebrow"><?= escape($product['category_name']) ?></p>
        <h1 class="fw-bold mb-3"><?= escape($product['name']) ?></h1>
        <p class="text-muted mb-4"><?= escape($product['description']) ?></p>
        <div class="d-flex gap-2 text-warning mb-3">
          <?php for ($i = 0; $i < (int)$product['rating']; $i++): ?><i class="fa-solid fa-star"></i><?php endfor; ?>
          <span class="text-dark ms-2"><?= number_format($product['rating'], 1) ?> · <?= (int)$product['reviews_count'] ?> reviews</span>
        </div>
        <div class="d-flex align-items-center gap-3 mb-4">
          <h3 class="fw-bold m-0"><?= format_price($product['price'] - ($product['price'] * $product['discount_percent'] / 100)) ?></h3>
          <?php if ($product['discount_percent'] > 0): ?><span class="text-muted text-decoration-line-through"><?= format_price($product['price']) ?></span><?php endif; ?>
        </div>
        <ul class="list-unstyled text-muted mb-4">
          <li><strong>Sizes:</strong> <?= escape($product['sizes']) ?></li>
          <li><strong>Colors:</strong> <?= escape($product['colors']) ?></li>
          <li><strong>Stock:</strong> <?= (int)$product['stock'] ?></li>
        </ul>
        <form method="post" action="<?= url('pages/cart.php') ?>" class="d-flex flex-wrap gap-2">
          <input type="hidden" name="action" value="add">
          <input type="hidden" name="product_id" value="<?= (int)$product['id'] ?>">
          <?= csrf_field() ?>
          <button class="btn btn-dark btn-lg" type="submit">Add to Cart</button>
          <a href="<?= url('pages/wishlist.php?action=add&product_id=' . (int)$product['id']) ?>" class="btn btn-outline-dark btn-lg">Add to Wishlist</a>
        </form>
      </div>
    </div>
    <section class="mt-5">
      <h3 class="fw-bold mb-3">Related Products</h3>
      <div class="row g-4">
        <?php foreach (get_related_products($product['category_id'], $product['id']) as $item): ?>
        <div class="col-md-6 col-lg-3" data-aos="fade-up">
          <article class="card-product h-100">
            <img src="<?= htmlspecialchars($item['thumbnail']) ?>" alt="<?= escape($item['name']) ?>" class="card-product-image" loading="lazy">
            <div class="p-4">
              <h5 class="fw-semibold mb-3"><?= escape($item['name']) ?></h5>
              <a href="<?= url('pages/product-detail.php?id=' . (int)$item['id']) ?>" class="btn btn-outline-dark btn-sm">View</a>
            </div>
          </article>
        </div>
        <?php endforeach; ?>
      </div>
    </section>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
