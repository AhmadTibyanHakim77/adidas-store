<?php
require_once __DIR__ . '/../includes/config.php';
require_login();
$page_title = 'Checkout';
$page_description = 'Complete your premium Adidas checkout.';
include __DIR__ . '/../includes/navbar.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    require_csrf();
    $user = $_SESSION['user'];
    $total = get_cart_total() * 1.08;
    $stmt = get_db()->prepare('INSERT INTO orders (user_id, total_amount, status, shipping_address, payment_method) VALUES (?, ?, ?, ?, ?)');
    $stmt->execute([$user['id'], $total, 'pending', $_POST['address'] ?? '', $_POST['payment_method'] ?? 'card']);
    $order_id = get_db()->lastInsertId();
    foreach (get_cart() as $product_id => $qty) {
        $product = get_product($product_id);
        if ($product) {
            $discounted = $product['price'] - ($product['price'] * $product['discount_percent'] / 100);
            $itemStmt = get_db()->prepare('INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)');
            $itemStmt->execute([$order_id, $product_id, $qty, $discounted]);
        }
    }
    $_SESSION['cart'] = [];
    redirect('pages/profile.php?order=' . $order_id);
}
?>
<main class="py-5">
  <div class="container">
    <h1 class="fw-bold mb-4">Checkout</h1>
    <div class="row g-4">
      <div class="col-lg-7"><div class="glass-card p-4">
        <form method="post">
          <?= csrf_field() ?>
          <div class="mb-3"><label class="form-label">Shipping Address</label><textarea class="form-control" name="address" rows="4" required></textarea></div>
          <div class="mb-3"><label class="form-label">Payment Method</label><select class="form-select" name="payment_method"><option value="card">Credit Card</option><option value="paypal">PayPal</option><option value="cod">Cash on Delivery</option></select></div>
          <button class="btn btn-dark" type="submit">Place Order</button>
        </form>
      </div></div>
      <div class="col-lg-5"><div class="glass-card p-4"><h4 class="fw-semibold mb-3">Order Summary</h4><p class="text-muted">Fast shipping and premium packaging included.</p><div class="d-flex justify-content-between mb-2"><span>Subtotal</span><strong><?= format_price(get_cart_total()) ?></strong></div><div class="d-flex justify-content-between mb-2"><span>Tax</span><strong><?= format_price(get_cart_total() * 0.08) ?></strong></div><hr><div class="d-flex justify-content-between mb-3"><span>Total</span><strong><?= format_price(get_cart_total() * 1.08) ?></strong></div></div></div>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
