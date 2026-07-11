<?php
require_once __DIR__ . '/../includes/config.php';
$page_title = 'Shopping Cart';
$page_description = 'Review and manage your Adidas cart.';
include __DIR__ . '/../includes/navbar.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    require_csrf();
    $action = $_POST['action'] ?? '';
    if ($action === 'add') add_to_cart((int)$_POST['product_id'], (int)($_POST['quantity'] ?? 1));
    elseif ($action === 'remove') remove_from_cart((int)$_POST['product_id']);
    redirect('pages/cart.php');
}

$cart = get_cart(); $items = []; foreach ($cart as $product_id => $qty) { $product = get_product($product_id); if ($product) $items[] = ['product' => $product, 'qty' => $qty]; }
$total = array_reduce($items, fn($sum, $item) => $sum + (($item['product']['price'] - ($item['product']['price'] * $item['product']['discount_percent'] / 100)) * $item['qty']), 0);
?>
<main class="py-5">
  <div class="container">
    <h1 class="fw-bold mb-4">Your Cart</h1>
    <?php if (!$items): ?>
      <div class="glass-card p-5 text-center">
        <h4 class="mb-3">Your bag is empty</h4>
        <a href="<?= url('pages/shop.php') ?>" class="btn btn-dark">Continue Shopping</a>
      </div>
    <?php else: ?>
      <div class="row g-4">
        <div class="col-lg-8">
          <?php foreach ($items as $item): ?>
          <div class="glass-card p-4 mb-3 d-flex justify-content-between align-items-center flex-wrap gap-3">
            <div class="d-flex align-items-center gap-3">
              <img src="<?= htmlspecialchars($item['product']['thumbnail']) ?>" alt="<?= escape($item['product']['name']) ?>" width="80" class="rounded-3">
              <div>
                <h5 class="fw-semibold mb-1"><?= escape($item['product']['name']) ?></h5>
                <p class="text-muted mb-0">Qty: <?= (int)$item['qty'] ?></p>
              </div>
            </div>
            <div class="d-flex align-items-center gap-3">
              <strong><?= format_price(($item['product']['price'] - ($item['product']['price'] * $item['product']['discount_percent'] / 100)) * $item['qty']) ?></strong>
              <form method="post" class="d-inline">
                <input type="hidden" name="action" value="remove">
                <input type="hidden" name="product_id" value="<?= (int)$item['product']['id'] ?>">
                <?= csrf_field() ?>
                <button class="btn btn-outline-dark btn-sm" type="submit">Remove</button>
              </form>
            </div>
          </div>
          <?php endforeach; ?>
        </div>
        <div class="col-lg-4">
          <div class="glass-card p-4">
            <h4 class="fw-semibold mb-4">Summary</h4>
            <div class="d-flex justify-content-between mb-2"><span>Subtotal</span><strong><?= format_price($total) ?></strong></div>
            <div class="d-flex justify-content-between mb-2"><span>Shipping</span><strong>Free</strong></div>
            <div class="d-flex justify-content-between mb-2"><span>Tax</span><strong><?= format_price($total * 0.08) ?></strong></div>
            <hr>
            <div class="d-flex justify-content-between mb-4"><span>Total</span><strong><?= format_price($total * 1.08) ?></strong></div>
            <a href="<?= url('pages/checkout.php') ?>" class="btn btn-dark w-100">Proceed to Checkout</a>
          </div>
        </div>
      </div>
    <?php endif; ?>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
