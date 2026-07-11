<?php
require_once __DIR__ . '/../includes/config.php';
if (!is_admin()) redirect('pages/login.php');
$page_title = 'Manage Orders';
$page_description = 'Manage Adidas orders';
include __DIR__ . '/../includes/navbar.php';
$stmt = get_db()->query('SELECT o.*, u.full_name FROM orders o LEFT JOIN users u ON o.user_id = u.id ORDER BY o.created_at DESC');
$orders = $stmt->fetchAll();
?>
<main class="py-5">
  <div class="container">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h1 class="fw-bold">Orders</h1>
      <a href="<?= url('admin/index.php') ?>" class="btn btn-outline-dark">Back</a>
    </div>
    <div class="table-responsive glass-card p-3">
      <table class="table align-middle">
        <thead><tr><th>Order</th><th>Customer</th><th>Total</th><th>Status</th></tr></thead>
        <tbody>
          <?php foreach ($orders as $order): ?>
          <tr><td>#<?= (int)$order['id'] ?></td><td><?= escape($order['full_name']) ?></td><td><?= format_price($order['total_amount']) ?></td><td><?= escape($order['status']) ?></td></tr>
          <?php endforeach; ?>
        </tbody>
      </table>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
