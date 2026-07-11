<?php
require_once __DIR__ . '/../includes/config.php';
require_login();
$page_title = 'My Profile';
$page_description = 'View your Adidas account and orders.';
include __DIR__ . '/../includes/navbar.php';

$user = $_SESSION['user'];
$stmt = get_db()->prepare('SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC');
$stmt->execute([$user['id']]);
$orders = $stmt->fetchAll();
?>
<main class="py-5">
  <div class="container">
    <h1 class="fw-bold mb-4">My Profile</h1>
    <div class="glass-card p-4 mb-4">
      <h4 class="fw-semibold mb-2"><?= escape($user['full_name']) ?></h4>
      <p class="text-muted mb-0"><?= escape($user['email']) ?></p>
    </div>
    <div class="glass-card p-4">
      <h4 class="fw-semibold mb-3">Order History</h4>
      <?php if (!$orders): ?>
        <p class="text-muted">No orders yet.</p>
      <?php else: ?>
        <div class="list-group">
          <?php foreach ($orders as $order): ?>
            <div class="list-group-item d-flex justify-content-between align-items-center">
              <div>
                <h6 class="mb-1">Order #<?= (int)$order['id'] ?></h6>
                <small class="text-muted">Status: <?= escape($order['status']) ?></small>
              </div>
              <div class="text-end">
                <div class="fw-semibold"><?= format_price($order['total_amount']) ?></div>
                <small class="text-muted"><?= date('M d, Y', strtotime($order['created_at'])) ?></small>
              </div>
            </div>
          <?php endforeach; ?>
        </div>
      <?php endif; ?>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
