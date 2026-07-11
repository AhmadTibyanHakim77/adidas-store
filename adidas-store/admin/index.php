<?php
require_once __DIR__ . '/../includes/config.php';
if (!is_admin()) redirect('pages/login.php');
$page_title = 'Admin Dashboard';
$page_description = 'Adidas admin dashboard';
include __DIR__ . '/../includes/navbar.php';
?>
<main class="py-5">
  <div class="container">
    <h1 class="fw-bold mb-4">Admin Dashboard</h1>
    <div class="row g-4">
      <div class="col-md-4"><div class="glass-card p-4"><h5 class="fw-semibold">Products</h5><p class="text-muted">Manage your catalog</p><a href="<?= url('admin/products.php') ?>" class="btn btn-dark">Go</a></div></div>
      <div class="col-md-4"><div class="glass-card p-4"><h5 class="fw-semibold">Orders</h5><p class="text-muted">Review customer purchases</p><a href="<?= url('admin/orders.php') ?>" class="btn btn-dark">Go</a></div></div>
      <div class="col-md-4"><div class="glass-card p-4"><h5 class="fw-semibold">Customers</h5><p class="text-muted">Monitor account activity</p><a href="<?= url('admin/customers.php') ?>" class="btn btn-dark">Go</a></div></div>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
