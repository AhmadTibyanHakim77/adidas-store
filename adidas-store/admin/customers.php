<?php
require_once __DIR__ . '/../includes/config.php';
if (!is_admin()) redirect('pages/login.php');
$page_title = 'Manage Customers';
$page_description = 'Manage Adidas customers';
include __DIR__ . '/../includes/navbar.php';
$stmt = get_db()->query('SELECT * FROM users ORDER BY created_at DESC');
$customers = $stmt->fetchAll();
?>
<main class="py-5">
  <div class="container">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h1 class="fw-bold">Customers</h1>
      <a href="<?= url('admin/index.php') ?>" class="btn btn-outline-dark">Back</a>
    </div>
    <div class="table-responsive glass-card p-3">
      <table class="table align-middle">
        <thead><tr><th>Name</th><th>Email</th><th>Role</th></tr></thead>
        <tbody>
          <?php foreach ($customers as $customer): ?>
          <tr><td><?= escape($customer['full_name']) ?></td><td><?= escape($customer['email']) ?></td><td><?= escape($customer['role']) ?></td></tr>
          <?php endforeach; ?>
        </tbody>
      </table>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
