<?php
require_once __DIR__ . '/../includes/config.php';
$page_title = 'Login';
$page_description = 'Sign in to your Adidas account.';
include __DIR__ . '/../includes/navbar.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    require_csrf();
    $email = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';
    $stmt = get_db()->prepare('SELECT * FROM users WHERE email = ? LIMIT 1');
    $stmt->execute([$email]);
    $user = $stmt->fetch();
    if ($user && password_verify($password, $user['password_hash'])) {
        $_SESSION['user'] = $user;
        redirect('index.php');
    }
    $error = 'Invalid credentials.';
}
?>
<main class="py-5">
  <div class="container py-5">
    <div class="row justify-content-center">
      <div class="col-lg-5">
        <div class="glass-card p-4">
          <h2 class="fw-bold mb-3">Login</h2>
          <?php if (!empty($error)): ?><div class="alert alert-danger"><?= escape($error) ?></div><?php endif; ?>
          <form method="post">
            <?= csrf_field() ?>
            <div class="mb-3"><label class="form-label">Email</label><input class="form-control" name="email" type="email" required></div>
            <div class="mb-3"><label class="form-label">Password</label><input class="form-control" name="password" type="password" required></div>
            <button class="btn btn-dark w-100" type="submit">Sign In</button>
          </form>
          <p class="text-muted mt-3 mb-0">No account? <a href="<?= url('pages/register.php') ?>">Create one</a></p>
        </div>
      </div>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
