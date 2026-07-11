<?php
require_once __DIR__ . '/../includes/config.php';
$page_title = 'Register';
$page_description = 'Create your Adidas account.';
include __DIR__ . '/../includes/navbar.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    require_csrf();
    $full_name = trim($_POST['full_name'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $password = $_POST['password'] ?? '';
    $stmt = get_db()->prepare('SELECT id FROM users WHERE email = ? LIMIT 1');
    $stmt->execute([$email]);
    if ($stmt->fetch()) {
        $error = 'Email already exists.';
    } else {
        $hash = password_hash($password, PASSWORD_DEFAULT);
        $insert = get_db()->prepare('INSERT INTO users (full_name, email, password_hash, role) VALUES (?, ?, ?, ?)');
        $insert->execute([$full_name, $email, $hash, 'customer']);
        redirect('pages/login.php');
    }
}
?>
<main class="py-5">
  <div class="container py-5">
    <div class="row justify-content-center">
      <div class="col-lg-5">
        <div class="glass-card p-4">
          <h2 class="fw-bold mb-3">Create Account</h2>
          <?php if (!empty($error)): ?><div class="alert alert-danger"><?= escape($error) ?></div><?php endif; ?>
          <form method="post">
            <?= csrf_field() ?>
            <div class="mb-3"><label class="form-label">Full Name</label><input class="form-control" name="full_name" required></div>
            <div class="mb-3"><label class="form-label">Email</label><input class="form-control" name="email" type="email" required></div>
            <div class="mb-3"><label class="form-label">Password</label><input class="form-control" name="password" type="password" required></div>
            <button class="btn btn-dark w-100" type="submit">Create Account</button>
          </form>
          <p class="text-muted mt-3 mb-0">Already have an account? <a href="<?= url('pages/login.php') ?>">Login</a></p>
        </div>
      </div>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
