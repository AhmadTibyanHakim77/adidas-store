from pathlib import Path
import os

root = Path(r'c:/Users/USER/Downloads/ADIDAS/adidas-store')
root.mkdir(parents=True, exist_ok=True)

folders = [
    'assets/css', 'assets/js', 'assets/images/hero', 'assets/images/products', 'assets/images/banner', 'assets/images/icons', 'assets/fonts',
    'includes', 'database', 'admin', 'pages', 'uploads'
]
for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

files = {}

files['index.php'] = r'''<?php
require_once __DIR__ . '/includes/config.php';
$page_title = 'Adidas Store | Premium Sportswear';
$page_description = 'Discover premium Adidas collections with futuristic design, fast shipping, and exclusive drops.';
include __DIR__ . '/includes/navbar.php';
?>

<main id="main-content" class="pt-5">
  <section class="hero-section position-relative overflow-hidden py-5">
    <video autoplay muted loop playsinline class="hero-video" poster="<?= asset('images/hero/hero-1.jpg') ?>">
      <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
    </video>
    <div class="hero-overlay"></div>
    <div class="container position-relative z-2 py-5">
      <div class="row align-items-center min-vh-100">
        <div class="col-lg-7 text-white" data-aos="fade-right">
          <p class="eyebrow mb-3">Adidas Originals · 2026 Drop</p>
          <h1 class="display-3 fw-bold mb-4">Feel the future in every stride.</h1>
          <p class="lead mb-4 text-light">Premium sneakers, performance apparel, and elevated essentials crafted for the modern athlete.</p>
          <div class="typing-wrap mb-4"><span class="typing-text"></span></div>
          <div class="d-flex flex-wrap gap-3">
            <a href="<?= url('pages/shop.php') ?>" class="btn btn-accent btn-lg">Explore Collection</a>
            <a href="<?= url('pages/shop.php?sort=new') ?>" class="btn btn-outline-light btn-lg">New Arrival</a>
          </div>
          <div class="d-flex gap-4 mt-5 flex-wrap">
            <div><h4 class="fw-bold mb-0">4.9/5</h4><small class="text-light">Rated by 80k+ customers</small></div>
            <div><h4 class="fw-bold mb-0">24h</h4><small class="text-light">Express Delivery</small></div>
            <div><h4 class="fw-bold mb-0">100%</h4><small class="text-light">Authentic Products</small></div>
          </div>
        </div>
        <div class="col-lg-5" data-aos="fade-left">
          <div class="glass-card p-4 floating-card">
            <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80" alt="Premium Adidas sneaker" class="img-fluid rounded-4 shadow-lg" loading="lazy">
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="py-5 bg-dark text-white">
    <div class="container">
      <div class="row g-4">
        <?php foreach (get_categories() as $category): ?>
        <div class="col-6 col-md-4 col-lg-2">
          <a href="<?= url('pages/shop.php?category=' . (int)$category['id']) ?>" class="text-decoration-none text-white">
            <div class="glass-card p-3 text-center h-100">
              <h6 class="mb-1 fw-semibold"><?= htmlspecialchars($category['name']) ?></h6>
              <small class="text-secondary">Sport essentials</small>
            </div>
          </a>
        </div>
        <?php endforeach; ?>
      </div>
    </div>
  </section>

  <section class="py-5">
    <div class="container">
      <div class="section-heading d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3">
        <div>
          <p class="eyebrow">Featured</p>
          <h2 class="fw-bold">Best Seller Picks</h2>
        </div>
        <a href="<?= url('pages/shop.php') ?>" class="btn btn-outline-dark">View More</a>
      </div>
      <div class="row g-4">
        <?php foreach (get_products(8) as $product): ?>
        <div class="col-md-6 col-lg-3" data-aos="fade-up">
          <article class="card-product h-100">
            <div class="product-badge"><?= $product['discount_percent'] > 0 ? '-' . $product['discount_percent'] . '%' : 'New' ?></div>
            <img src="<?= htmlspecialchars($product['thumbnail']) ?>" alt="<?= htmlspecialchars($product['name']) ?>" class="card-product-image" loading="lazy">
            <div class="p-4">
              <p class="text-muted small mb-2"><?= htmlspecialchars($product['category_name']) ?></p>
              <h5 class="fw-semibold mb-3"><?= htmlspecialchars($product['name']) ?></h5>
              <div class="d-flex align-items-center gap-2 text-warning mb-3">
                <i class="fa-solid fa-star"></i><span><?= number_format($product['rating'], 1) ?></span>
              </div>
              <div class="d-flex justify-content-between align-items-center">
                <div>
                  <strong><?= format_price($product['price'] - ($product['price'] * $product['discount_percent'] / 100)) ?></strong>
                  <?php if ($product['discount_percent'] > 0): ?><small class="text-muted text-decoration-line-through ms-2"><?= format_price($product['price']) ?></small><?php endif; ?>
                </div>
                <a href="<?= url('pages/product-detail.php?id=' . (int)$product['id']) ?>" class="btn btn-dark btn-sm">View</a>
              </div>
            </div>
          </article>
        </div>
        <?php endforeach; ?>
      </div>
    </div>
  </section>

  <section class="py-5 bg-light">
    <div class="container">
      <div class="row align-items-center g-4">
        <div class="col-lg-6" data-aos="fade-right">
          <p class="eyebrow">Flash Sale</p>
          <h2 class="fw-bold mb-3">Limited drops every week.</h2>
          <p class="text-muted">Exclusive sneakers and gear at discounted rates while stock lasts.</p>
          <div class="countdown mt-4" data-deadline="2026-12-31T23:59:59"></div>
        </div>
        <div class="col-lg-6" data-aos="fade-left">
          <div class="glass-card p-4">
            <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=1000&q=80" alt="Adidas flash sale" class="img-fluid rounded-4" loading="lazy">
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="py-5">
    <div class="container">
      <div class="section-heading mb-4">
        <p class="eyebrow">Reviews</p>
        <h2 class="fw-bold">Trusted by athletes and style lovers</h2>
      </div>
      <div class="row g-4">
        <?php $reviews = get_reviews(3); foreach ($reviews as $review): ?>
        <div class="col-lg-4" data-aos="zoom-in">
          <div class="glass-card p-4 h-100">
            <div class="d-flex align-items-center gap-2 text-warning mb-3">
              <?php for ($i = 0; $i < (int)$review['rating']; $i++): ?><i class="fa-solid fa-star"></i><?php endfor; ?>
            </div>
            <p class="mb-3">“<?= htmlspecialchars($review['comment']) ?>”</p>
            <div class="fw-semibold"><?= htmlspecialchars($review['customer_name']) ?></div>
          </div>
        </div>
        <?php endforeach; ?>
      </div>
    </div>
  </section>

  <section class="py-5 bg-dark text-white">
    <div class="container">
      <div class="row align-items-center g-4">
        <div class="col-lg-7">
          <p class="eyebrow">Newsletter</p>
          <h2 class="fw-bold">Stay ahead of every release.</h2>
        </div>
        <div class="col-lg-5">
          <form class="d-flex flex-wrap gap-2">
            <input type="email" class="form-control form-control-lg" placeholder="Enter your email" aria-label="Email address">
            <button class="btn btn-accent btn-lg" type="submit">Subscribe</button>
          </form>
        </div>
      </div>
    </div>
  </section>
</main>

<?php include __DIR__ . '/includes/footer.php'; ?>
'''

files['includes/config.php'] = r'''<?php
session_start();

$host = '127.0.0.1';
$db = 'adidas_store';
$user = 'root';
$pass = '';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

try {
    $pdo = new PDO($dsn, $user, $pass, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES => false,
    ]);
} catch (PDOException $e) {
    try {
        $pdo = new PDO("mysql:host=$host;charset=$charset", $user, $pass, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        ]);
        $pdo->exec("CREATE DATABASE IF NOT EXISTS `$db` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci");
        $pdo->exec("USE `$db`");
    } catch (PDOException $e2) {
        die('Database connection failed: ' . $e2->getMessage());
    }
}

if (!defined('APP_ROOT')) define('APP_ROOT', dirname(__DIR__));
if (!defined('BASE_URL')) define('BASE_URL', '/adidas-store');

function asset($path) { return BASE_URL . '/assets/' . ltrim($path, '/'); }
function url($path) { return BASE_URL . '/' . ltrim($path, '/'); }

require_once APP_ROOT . '/includes/functions.php';

if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}

function csrf_token() { return $_SESSION['csrf_token']; }
function csrf_field() { return '<input type="hidden" name="csrf_token" value="' . htmlspecialchars(csrf_token()) . '">'; }
function require_csrf() { if (!hash_equals($_SESSION['csrf_token'] ?? '', $_POST['csrf_token'] ?? '')) throw new Exception('Invalid CSRF token.'); }
'''

files['includes/functions.php'] = r'''<?php
require_once __DIR__ . '/config.php';

function get_db() { global $pdo; return $pdo; }
function redirect($path) { header('Location: ' . url($path)); exit; }
function escape($value) { return htmlspecialchars((string)$value, ENT_QUOTES, 'UTF-8'); }
function get_categories() { $stmt = get_db()->query('SELECT * FROM categories ORDER BY name ASC'); return $stmt->fetchAll(); }
function get_product($id) { $stmt = get_db()->prepare('SELECT p.*, c.name AS category_name FROM products p LEFT JOIN categories c ON p.category_id = c.id WHERE p.id = ?'); $stmt->execute([$id]); return $stmt->fetch(); }
function get_products($limit = 12, $category = null, $search = null, $sort = null) { $sql = 'SELECT p.*, c.name AS category_name FROM products p LEFT JOIN categories c ON p.category_id = c.id WHERE 1=1'; $params = []; if ($category) { $sql .= ' AND p.category_id = ?'; $params[] = $category; } if ($search) { $sql .= ' AND (p.name LIKE ? OR p.description LIKE ?)'; $params[] = '%' . $search . '%'; $params[] = '%' . $search . '%'; } switch ($sort) { case 'price_asc': $sql .= ' ORDER BY p.price ASC'; break; case 'price_desc': $sql .= ' ORDER BY p.price DESC'; break; case 'new': $sql .= ' ORDER BY p.created_at DESC'; break; case 'rating': $sql .= ' ORDER BY p.rating DESC'; break; default: $sql .= ' ORDER BY p.featured DESC, p.created_at DESC'; break; } $sql .= ' LIMIT ?'; $params[] = (int)$limit; $stmt = get_db()->prepare($sql); $stmt->execute($params); return $stmt->fetchAll(); }
function get_related_products($category_id, $current_id) { $stmt = get_db()->prepare('SELECT * FROM products WHERE category_id = ? AND id != ? ORDER BY created_at DESC LIMIT 4'); $stmt->execute([$category_id, $current_id]); return $stmt->fetchAll(); }
function get_banners() { $stmt = get_db()->query('SELECT * FROM banners WHERE active = 1 ORDER BY created_at DESC'); return $stmt->fetchAll(); }
function get_reviews($limit = 3) { $stmt = get_db()->prepare('SELECT r.*, u.full_name AS customer_name FROM reviews r LEFT JOIN users u ON r.user_id = u.id ORDER BY r.created_at DESC LIMIT ?'); $stmt->bindValue(1, (int)$limit, PDO::PARAM_INT); $stmt->execute(); return $stmt->fetchAll(); }
function get_cart() { if (!isset($_SESSION['cart'])) $_SESSION['cart'] = []; return $_SESSION['cart']; }
function add_to_cart($product_id, $quantity = 1) { $cart = get_cart(); $cart[$product_id] = ($cart[$product_id] ?? 0) + $quantity; $_SESSION['cart'] = $cart; }
function remove_from_cart($product_id) { $cart = get_cart(); unset($cart[$product_id]); $_SESSION['cart'] = $cart; }
function get_wishlist() { if (!isset($_SESSION['wishlist'])) $_SESSION['wishlist'] = []; return $_SESSION['wishlist']; }
function add_to_wishlist($product_id) { $wishlist = get_wishlist(); if (!in_array($product_id, $wishlist, true)) $wishlist[] = $product_id; $_SESSION['wishlist'] = $wishlist; }
function remove_from_wishlist($product_id) { $wishlist = get_wishlist(); $_SESSION['wishlist'] = array_values(array_filter($wishlist, fn($item) => (int)$item !== (int)$product_id)); }
function is_logged_in() { return !empty($_SESSION['user']); }
function require_login() { if (!is_logged_in()) redirect('pages/login.php'); }
function is_admin() { return is_logged_in() && ($_SESSION['user']['role'] ?? 'customer') === 'admin'; }
function format_price($price) { return '$' . number_format((float)$price, 2); }
function get_cart_count() { return array_sum(get_cart()); }
function get_cart_total() { $total = 0; foreach (get_cart() as $product_id => $qty) { $product = get_product($product_id); if ($product) { $discounted = $product['price'] - ($product['price'] * $product['discount_percent'] / 100); $total += $discounted * $qty; } } return $total; }
function get_wishlist_products() { $ids = get_wishlist(); if (!$ids) return []; $placeholders = implode(',', array_fill(0, count($ids), '?')); $stmt = get_db()->prepare('SELECT * FROM products WHERE id IN (' . $placeholders . ')'); $stmt->execute($ids); return $stmt->fetchAll(); }
function get_recently_viewed() { if (empty($_SESSION['recently_viewed'])) return []; $ids = array_slice(array_reverse($_SESSION['recently_viewed']), 0, 4); $placeholders = implode(',', array_fill(0, count($ids), '?')); $stmt = get_db()->prepare('SELECT * FROM products WHERE id IN (' . $placeholders . ')'); $stmt->execute($ids); return $stmt->fetchAll(); }
function mark_recently_viewed($product_id) { if (!isset($_SESSION['recently_viewed'])) $_SESSION['recently_viewed'] = []; $_SESSION['recently_viewed'] = array_values(array_unique(array_merge([(int)$product_id], $_SESSION['recently_viewed']))); }
'''

files['includes/navbar.php'] = r'''<?php
$cart_count = get_cart_count();
$wishlist_count = count(get_wishlist());
?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="<?= escape($page_description ?? 'Adidas premium e-commerce experience') ?>">
  <meta name="theme-color" content="#0b0b0d">
  <meta property="og:title" content="<?= escape($page_title ?? 'Adidas Store') ?>">
  <meta property="og:description" content="<?= escape($page_description ?? 'Premium Adidas store') ?>">
  <meta property="og:type" content="website">
  <meta property="twitter:card" content="summary_large_image">
  <meta name="robots" content="index,follow">
  <title><?= escape($page_title ?? 'Adidas Store') ?></title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet">
  <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" rel="stylesheet">
  <link rel="stylesheet" href="<?= asset('css/style.css') ?>">
  <link rel="stylesheet" href="<?= asset('css/responsive.css') ?>">
  <link rel="stylesheet" href="<?= asset('css/animation.css') ?>">
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"Store","name":"Adidas Store","url":"https://example.com","logo":"https://example.com/assets/images/logo.png"}</script>
</head>
<body class="bg-white text-dark">
  <header class="sticky-top shadow-sm bg-white/90 backdrop-blur">
    <nav class="navbar navbar-expand-lg container py-3" aria-label="Primary navigation">
      <a class="navbar-brand fw-bold d-flex align-items-center gap-2" href="<?= url('index.php') ?>">
        <img src="<?= asset('images/logo.png') ?>" alt="Adidas Store logo" width="42" height="42">
        <span class="brand-text">ADIDAS</span>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent" aria-controls="navbarContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarContent">
        <ul class="navbar-nav mx-auto mb-2 mb-lg-0 gap-lg-3">
          <li class="nav-item"><a class="nav-link" href="<?= url('index.php') ?>">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="<?= url('pages/shop.php') ?>">Shop</a></li>
          <li class="nav-item"><a class="nav-link" href="<?= url('pages/about.php') ?>">About</a></li>
          <li class="nav-item"><a class="nav-link" href="<?= url('pages/contact.php') ?>">Contact</a></li>
        </ul>
        <div class="d-flex align-items-center gap-2">
          <form class="d-flex align-items-center search-bar" action="<?= url('pages/shop.php') ?>" method="get">
            <input class="form-control" type="search" name="search" placeholder="Search products" aria-label="Search products">
            <button class="btn btn-dark" type="submit"><i class="fa-solid fa-magnifying-glass"></i></button>
          </form>
          <a class="btn btn-outline-dark position-relative" href="<?= url('pages/wishlist.php') ?>" aria-label="Wishlist"><i class="fa-regular fa-heart"></i><span class="count-badge"><?= $wishlist_count ?></span></a>
          <a class="btn btn-dark position-relative" href="<?= url('pages/cart.php') ?>" aria-label="Shopping cart"><i class="fa-solid fa-bag-shopping"></i><span class="count-badge"><?= $cart_count ?></span></a>
          <?php if (is_logged_in()): ?>
            <a class="btn btn-outline-dark" href="<?= url('pages/profile.php') ?>">Profile</a>
          <?php else: ?>
            <a class="btn btn-outline-dark" href="<?= url('pages/login.php') ?>">Login</a>
          <?php endif; ?>
        </div>
      </div>
    </nav>
  </header>
'''

files['includes/footer.php'] = r'''  <footer class="py-5 bg-dark text-white">
    <div class="container">
      <div class="row g-4">
        <div class="col-lg-4">
          <h4 class="fw-bold mb-3">ADIDAS STORE</h4>
          <p class="text-secondary">Premium performance footwear and apparel built with innovation and modern craft.</p>
        </div>
        <div class="col-lg-2">
          <h6 class="fw-semibold mb-3">Shop</h6>
          <ul class="list-unstyled text-secondary">
            <li><a href="<?= url('pages/shop.php') ?>" class="text-secondary text-decoration-none">All Products</a></li>
            <li><a href="<?= url('pages/shop.php?category=1') ?>" class="text-secondary text-decoration-none">Running</a></li>
            <li><a href="<?= url('pages/shop.php?category=2') ?>" class="text-secondary text-decoration-none">Football</a></li>
          </ul>
        </div>
        <div class="col-lg-2">
          <h6 class="fw-semibold mb-3">Support</h6>
          <ul class="list-unstyled text-secondary">
            <li><a href="<?= url('pages/contact.php') ?>" class="text-secondary text-decoration-none">Contact</a></li>
            <li><a href="<?= url('pages/about.php') ?>" class="text-secondary text-decoration-none">About</a></li>
            <li><a href="<?= url('pages/profile.php') ?>" class="text-secondary text-decoration-none">Account</a></li>
          </ul>
        </div>
        <div class="col-lg-4">
          <h6 class="fw-semibold mb-3">Follow</h6>
          <div class="d-flex gap-3 fs-5">
            <a href="#" class="text-white"><i class="fa-brands fa-instagram"></i></a>
            <a href="#" class="text-white"><i class="fa-brands fa-facebook"></i></a>
            <a href="#" class="text-white"><i class="fa-brands fa-twitter"></i></a>
          </div>
        </div>
      </div>
      <div class="border-top border-secondary mt-4 pt-4 text-secondary small d-flex justify-content-between flex-wrap gap-2">
        <span>© 2026 Adidas Store. All rights reserved.</span>
        <span><a href="<?= url('robots.txt') ?>" class="text-secondary">Robots</a> · <a href="<?= url('sitemap.xml') ?>" class="text-secondary">Sitemap</a></span>
      </div>
    </div>
  </footer>
  <button class="btn btn-accent back-to-top" id="backToTop" aria-label="Back to top"><i class="fa-solid fa-arrow-up"></i></button>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
  <script src="<?= asset('js/app.js') ?>"></script>
  <script src="<?= asset('js/slider.js') ?>"></script>
  <script src="<?= asset('js/cart.js') ?>"></script>
  <script src="<?= asset('js/wishlist.js') ?>"></script>
  <script src="<?= asset('js/search.js') ?>"></script>
</body>
</html>
'''

files['includes/sidebar.php'] = r'''<aside class="glass-card p-4 sticky-top" style="top: 100px;">
  <h5 class="fw-semibold mb-3">Filters</h5>
  <form method="get" action="<?= url('pages/shop.php') ?>" class="d-grid gap-3">
    <div>
      <label class="form-label">Category</label>
      <select class="form-select" name="category">
        <option value="">All</option>
        <?php foreach (get_categories() as $cat): ?>
        <option value="<?= (int)$cat['id'] ?>" <?= (($_GET['category'] ?? '') == $cat['id']) ? 'selected' : '' ?>><?= escape($cat['name']) ?></option>
        <?php endforeach; ?>
      </select>
    </div>
    <div>
      <label class="form-label">Sort</label>
      <select class="form-select" name="sort">
        <option value="featured" <?= (($_GET['sort'] ?? '') == 'featured') ? 'selected' : '' ?>>Featured</option>
        <option value="new" <?= (($_GET['sort'] ?? '') == 'new') ? 'selected' : '' ?>>Newest</option>
        <option value="price_asc" <?= (($_GET['sort'] ?? '') == 'price_asc') ? 'selected' : '' ?>>Price: Low to High</option>
        <option value="price_desc" <?= (($_GET['sort'] ?? '') == 'price_desc') ? 'selected' : '' ?>>Price: High to Low</option>
        <option value="rating" <?= (($_GET['sort'] ?? '') == 'rating') ? 'selected' : '' ?>>Highest Rated</option>
      </select>
    </div>
    <div>
      <label class="form-label">Search</label>
      <input class="form-control" name="search" value="<?= escape($_GET['search'] ?? '') ?>" placeholder="Search by name">
    </div>
    <button class="btn btn-dark" type="submit">Apply Filters</button>
  </form>
</aside>
'''

files['pages/shop.php'] = r'''<?php
require_once __DIR__ . '/../includes/config.php';
$page_title = 'Shop Adidas';
$page_description = 'Browse premium Adidas shoes, apparel and accessories.';
include __DIR__ . '/../includes/navbar.php';

$search = $_GET['search'] ?? '';
$category = $_GET['category'] ?? '';
$sort = $_GET['sort'] ?? 'featured';
$page = max(1, (int)($_GET['page'] ?? 1));
$limit = 12;
$products = get_products($limit, $category ? (int)$category : null, $search, $sort);
?>
<main class="py-5">
  <div class="container">
    <div class="row g-4">
      <div class="col-lg-3">
        <?php include __DIR__ . '/../includes/sidebar.php'; ?>
      </div>
      <div class="col-lg-9">
        <div class="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3">
          <div>
            <p class="eyebrow">Discover</p>
            <h1 class="fw-bold">Adidas Collection</h1>
          </div>
          <div class="text-muted">Showing <?= count($products) ?> products</div>
        </div>
        <div class="row g-4">
          <?php foreach ($products as $product): ?>
          <div class="col-md-6 col-lg-4" data-aos="fade-up">
            <article class="card-product h-100">
              <img src="<?= htmlspecialchars($product['thumbnail']) ?>" alt="<?= htmlspecialchars($product['name']) ?>" class="card-product-image" loading="lazy">
              <div class="p-4">
                <p class="small text-muted mb-2"><?= escape($product['category_name']) ?></p>
                <h5 class="fw-semibold mb-3"><?= escape($product['name']) ?></h5>
                <p class="text-muted small"><?= htmlspecialchars(substr($product['description'], 0, 90)) ?>...</p>
                <div class="d-flex justify-content-between align-items-center mt-3">
                  <div><strong><?= format_price($product['price'] - ($product['price'] * $product['discount_percent'] / 100)) ?></strong></div>
                  <a class="btn btn-dark btn-sm" href="<?= url('pages/product-detail.php?id=' . (int)$product['id']) ?>">View</a>
                </div>
              </div>
            </article>
          </div>
          <?php endforeach; ?>
        </div>
      </div>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
'''

files['pages/product-detail.php'] = r'''<?php
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
'''

files['pages/cart.php'] = r'''<?php
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
'''

files['pages/checkout.php'] = r'''<?php
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
'''

files['pages/wishlist.php'] = r'''<?php
require_once __DIR__ . '/../includes/config.php';
$page_title = 'Wishlist';
$page_description = 'Save your favorite Adidas products.';
include __DIR__ . '/../includes/navbar.php';

if (isset($_GET['action']) && $_GET['action'] === 'add') { add_to_wishlist((int)$_GET['product_id']); redirect('pages/wishlist.php'); }
if (isset($_GET['action']) && $_GET['action'] === 'remove') { remove_from_wishlist((int)$_GET['product_id']); redirect('pages/wishlist.php'); }
$products = get_wishlist_products();
?>
<main class="py-5">
  <div class="container">
    <h1 class="fw-bold mb-4">Wishlist</h1>
    <?php if (!$products): ?>
      <div class="glass-card p-5 text-center">
        <h4 class="mb-3">No favorites yet</h4>
        <a href="<?= url('pages/shop.php') ?>" class="btn btn-dark">Browse Products</a>
      </div>
    <?php else: ?>
      <div class="row g-4">
        <?php foreach ($products as $product): ?>
        <div class="col-md-6 col-lg-4">
          <article class="card-product h-100">
            <img src="<?= htmlspecialchars($product['thumbnail']) ?>" alt="<?= escape($product['name']) ?>" class="card-product-image" loading="lazy">
            <div class="p-4">
              <h5 class="fw-semibold mb-3"><?= escape($product['name']) ?></h5>
              <div class="d-flex justify-content-between">
                <a href="<?= url('pages/product-detail.php?id=' . (int)$product['id']) ?>" class="btn btn-dark btn-sm">View</a>
                <a href="<?= url('pages/wishlist.php?action=remove&product_id=' . (int)$product['id']) ?>" class="btn btn-outline-dark btn-sm">Remove</a>
              </div>
            </div>
          </article>
        </div>
        <?php endforeach; ?>
      </div>
    <?php endif; ?>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
'''

files['pages/login.php'] = r'''<?php
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
        redirect(is_admin() ? 'admin/dashboard.php' : 'index.php');
    } else {
        $error = 'Invalid credentials';
    }
}
?>
<main class="py-5">
  <div class="container py-5">
    <div class="row justify-content-center">
      <div class="col-lg-5">
        <div class="glass-card p-4">
          <h2 class="fw-bold mb-3">Welcome back</h2>
          <p class="text-muted">Access your account and track orders.</p>
          <?php if (!empty($error)): ?><div class="alert alert-danger"><?= escape($error) ?></div><?php endif; ?>
          <form method="post">
            <?= csrf_field() ?>
            <div class="mb-3"><label class="form-label">Email</label><input type="email" name="email" class="form-control" required></div>
            <div class="mb-3"><label class="form-label">Password</label><input type="password" name="password" class="form-control" required></div>
            <button class="btn btn-dark w-100" type="submit">Login</button>
          </form>
          <p class="mt-3 mb-0 text-center"><a href="<?= url('pages/register.php') ?>">Create an account</a></p>
        </div>
      </div>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
'''

files['pages/register.php'] = r'''<?php
require_once __DIR__ . '/../includes/config.php';
$page_title = 'Register';
$page_description = 'Create an Adidas account.';
include __DIR__ . '/../includes/navbar.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    require_csrf();
    $stmt = get_db()->prepare('INSERT INTO users (full_name, email, password_hash, role, phone) VALUES (?, ?, ?, ?, ?)');
    $stmt->execute([$_POST['full_name'] ?? '', $_POST['email'] ?? '', password_hash($_POST['password'] ?? '', PASSWORD_DEFAULT), 'customer', $_POST['phone'] ?? '']);
    redirect('pages/login.php');
}
?>
<main class="py-5">
  <div class="container py-5">
    <div class="row justify-content-center">
      <div class="col-lg-6"><div class="glass-card p-4"><h2 class="fw-bold mb-3">Create account</h2><form method="post"><?= csrf_field() ?><div class="row g-3"><div class="col-md-6"><label class="form-label">Full name</label><input type="text" name="full_name" class="form-control" required></div><div class="col-md-6"><label class="form-label">Phone</label><input type="text" name="phone" class="form-control"></div></div><div class="mb-3 mt-3"><label class="form-label">Email</label><input type="email" name="email" class="form-control" required></div><div class="mb-3"><label class="form-label">Password</label><input type="password" name="password" class="form-control" required></div><button class="btn btn-dark w-100" type="submit">Register</button></form></div></div>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
'''

files['pages/profile.php'] = r'''<?php
require_once __DIR__ . '/../includes/config.php';
require_login();
$page_title = 'My Profile';
$page_description = 'Manage your Adidas profile and orders.';
include __DIR__ . '/../includes/navbar.php';
$user = $_SESSION['user'];
$stmt = get_db()->prepare('SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC');
$stmt->execute([$user['id']]);
$orders = $stmt->fetchAll();
?>
<main class="py-5">
  <div class="container">
    <h1 class="fw-bold mb-4">Hello, <?= escape($user['full_name']) ?></h1>
    <div class="row g-4">
      <div class="col-lg-4"><div class="glass-card p-4"><h4 class="fw-semibold">Account</h4><p class="mb-1"><strong>Email:</strong> <?= escape($user['email']) ?></p><p class="mb-0"><strong>Phone:</strong> <?= escape($user['phone']) ?></p></div></div>
      <div class="col-lg-8"><div class="glass-card p-4"><h4 class="fw-semibold">Recent Orders</h4><?php foreach ($orders as $order): ?><div class="border-bottom py-3"><div class="d-flex justify-content-between"><strong>#<?= (int)$order['id'] ?></strong><span><?= escape($order['status']) ?></span></div><div class="text-muted">Total: <?= format_price($order['total_amount']) ?></div></div><?php endforeach; ?></div></div>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
'''

files['pages/contact.php'] = r'''<?php
require_once __DIR__ . '/../includes/config.php';
$page_title = 'Contact Adidas';
$page_description = 'Contact the Adidas Store team.';
include __DIR__ . '/../includes/navbar.php';
?>
<main class="py-5">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-6"><p class="eyebrow">Support</p><h1 class="fw-bold mb-3">Contact our team</h1><p class="text-muted">Ask about products, returns, sizing, and premium support.</p><ul class="list-unstyled text-muted"><li><i class="fa-solid fa-envelope me-2"></i>support@adidas-store.test</li><li><i class="fa-solid fa-phone me-2"></i>+1 800 123 4567</li><li><i class="fa-solid fa-location-dot me-2"></i>New York, USA</li></ul></div>
      <div class="col-lg-6"><div class="glass-card p-4"><form><div class="mb-3"><input class="form-control" placeholder="Your name"></div><div class="mb-3"><input class="form-control" placeholder="Your email"></div><div class="mb-3"><textarea class="form-control" rows="4" placeholder="Message"></textarea></div><button class="btn btn-dark" type="submit">Send</button></form></div></div>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
'''

files['pages/about.php'] = r'''<?php
require_once __DIR__ . '/../includes/config.php';
$page_title = 'About Adidas Store';
$page_description = 'Learn about the premium Adidas Store experience.';
include __DIR__ . '/../includes/navbar.php';
?>
<main class="py-5">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-6"><p class="eyebrow">Crafted for performance</p><h1 class="fw-bold mb-3">A modern shopping experience for the next generation.</h1><p class="text-muted">Our store blends premium design, advanced comfort, and authentic Adidas collections into a fluid digital journey.</p></div>
      <div class="col-lg-6"><div class="glass-card p-4"><img src="https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?auto=format&fit=crop&w=1000&q=80" alt="Adidas sports lifestyle" class="img-fluid rounded-4" loading="lazy"></div></div>
    </div>
  </div>
</main>
<?php include __DIR__ . '/../includes/footer.php'; ?>
'''

files['admin/login.php'] = r'''<?php
require_once __DIR__ . '/../includes/config.php';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';
    $stmt = get_db()->prepare('SELECT * FROM users WHERE email = ? LIMIT 1');
    $stmt->execute([$email]);
    $user = $stmt->fetch();
    if ($user && password_verify($password, $user['password_hash']) && ($user['role'] ?? 'customer') === 'admin') {
        $_SESSION['user'] = $user;
        redirect('admin/dashboard.php');
    }
}
?>
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Admin Login</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head><body class="bg-dark text-white"><div class="container py-5"><div class="row justify-content-center"><div class="col-lg-5"><div class="card bg-black text-white border-secondary p-4"><h2 class="fw-bold mb-3">Admin Portal</h2><form method="post"><div class="mb-3"><label class="form-label">Email</label><input type="email" name="email" class="form-control" required></div><div class="mb-3"><label class="form-label">Password</label><input type="password" name="password" class="form-control" required></div><button class="btn btn-accent w-100" type="submit">Login</button></form></div></div></div></div></body></html>
'''

files['admin/dashboard.php'] = r'''<?php
require_once __DIR__ . '/../includes/config.php';
if (!is_admin()) redirect('admin/login.php');
$page_title = 'Admin Dashboard';
?>
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title><?= escape($page_title) ?></title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet"><link rel="stylesheet" href="<?= asset('css/style.css') ?>"></head><body class="bg-dark text-white"><div class="container py-4"><div class="d-flex justify-content-between align-items-center mb-4"><h2 class="fw-bold">Admin Dashboard</h2><a href="<?= url('index.php') ?>" class="btn btn-outline-light">View Store</a></div><div class="row g-4"><div class="col-md-3"><div class="glass-card p-4"><h5>Products</h5><div class="fs-3 fw-bold"><?= get_db()->query('SELECT COUNT(*) FROM products')->fetchColumn() ?></div></div></div><div class="col-md-3"><div class="glass-card p-4"><h5>Orders</h5><div class="fs-3 fw-bold"><?= get_db()->query('SELECT COUNT(*) FROM orders')->fetchColumn() ?></div></div></div><div class="col-md-3"><div class="glass-card p-4"><h5>Customers</h5><div class="fs-3 fw-bold"><?= get_db()->query('SELECT COUNT(*) FROM users')->fetchColumn() ?></div></div></div><div class="col-md-3"><div class="glass-card p-4"><h5>Revenue</h5><div class="fs-3 fw-bold">$<?= number_format(get_db()->query('SELECT COALESCE(SUM(total_amount),0) FROM orders')->fetchColumn(), 2) ?></div></div></div></div><div class="mt-4 d-flex flex-wrap gap-2"><a class="btn btn-outline-light" href="<?= url('admin/products.php') ?>">Products</a><a class="btn btn-outline-light" href="<?= url('admin/categories.php') ?>">Categories</a><a class="btn btn-outline-light" href="<?= url('admin/orders.php') ?>">Orders</a><a class="btn btn-outline-light" href="<?= url('admin/customers.php') ?>">Customers</a></div></div></body></html>
'''

files['admin/products.php'] = r'''<?php
require_once __DIR__ . '/../includes/config.php';
if (!is_admin()) redirect('admin/login.php');
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  if (isset($_POST['delete'])) { $stmt = get_db()->prepare('DELETE FROM products WHERE id = ?'); $stmt->execute([(int)$_POST['id']]); } else { $thumbnail = '/assets/images/products/' . basename($_FILES['thumbnail']['name'] ?? 'product.jpg'); move_uploaded_file($_FILES['thumbnail']['tmp_name'] ?? '', __DIR__ . '/../' . ltrim($thumbnail, '/')); $stmt = get_db()->prepare('INSERT INTO products (name, price, discount_percent, description, sizes, colors, rating, reviews_count, stock, category_id, thumbnail, featured) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'); $stmt->execute([$_POST['name'] ?? '', (float)($_POST['price'] ?? 0), (int)($_POST['discount_percent'] ?? 0), $_POST['description'] ?? '', $_POST['sizes'] ?? '', $_POST['colors'] ?? '', (float)($_POST['rating'] ?? 0), (int)($_POST['reviews_count'] ?? 0), (int)($_POST['stock'] ?? 0), (int)($_POST['category_id'] ?? 0), $thumbnail, isset($_POST['featured']) ? 1 : 0]); }
}
$products = get_db()->query('SELECT p.*, c.name AS category_name FROM products p LEFT JOIN categories c ON p.category_id = c.id ORDER BY p.id DESC')->fetchAll();
$categories = get_categories();
?>
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Manage Products</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head><body class="bg-dark text-white"><div class="container py-4"><h2 class="fw-bold">Manage Products</h2><form class="row g-3 my-4" method="post" enctype="multipart/form-data"><div class="col-md-4"><input class="form-control" name="name" placeholder="Product name" required></div><div class="col-md-2"><input class="form-control" name="price" type="number" step="0.01" placeholder="Price" required></div><div class="col-md-2"><input class="form-control" name="discount_percent" type="number" placeholder="Discount %"></div><div class="col-md-2"><input class="form-control" name="stock" type="number" placeholder="Stock"></div><div class="col-md-2"><select class="form-select" name="category_id"><?php foreach ($categories as $cat): ?><option value="<?= (int)$cat['id'] ?>"><?= escape($cat['name']) ?></option><?php endforeach; ?></select></div><div class="col-md-12"><textarea class="form-control" name="description" rows="3" placeholder="Description"></textarea></div><div class="col-md-4"><input class="form-control" name="sizes" placeholder="Sizes"></div><div class="col-md-4"><input class="form-control" name="colors" placeholder="Colors"></div><div class="col-md-2"><input class="form-control" name="rating" type="number" step="0.1" placeholder="Rating"></div><div class="col-md-2"><input class="form-control" name="reviews_count" type="number" placeholder="Reviews"></div><div class="col-md-12"><input class="form-control" type="file" name="thumbnail"></div><div class="col-md-12"><label><input type="checkbox" name="featured" value="1"> Featured</label></div><div class="col-md-12"><button class="btn btn-accent" type="submit">Add Product</button></div></form><div class="table-responsive"><table class="table table-dark table-striped align-middle"><thead><tr><th>ID</th><th>Name</th><th>Category</th><th>Price</th><th>Stock</th><th>Actions</th></tr></thead><tbody><?php foreach ($products as $product): ?><tr><td><?= (int)$product['id'] ?></td><td><?= escape($product['name']) ?></td><td><?= escape($product['category_name']) ?></td><td><?= format_price($product['price']) ?></td><td><?= (int)$product['stock'] ?></td><td><form method="post" class="d-inline"><input type="hidden" name="id" value="<?= (int)$product['id'] ?>"><input type="hidden" name="delete" value="1"><button class="btn btn-outline-danger btn-sm" type="submit">Delete</button></form></td></tr><?php endforeach; ?></tbody></table></div></div></body></html>
'''

files['admin/categories.php'] = r'''<?php
require_once __DIR__ . '/../includes/config.php';
if (!is_admin()) redirect('admin/login.php');
if ($_SERVER['REQUEST_METHOD'] === 'POST') { $stmt = get_db()->prepare('INSERT INTO categories (name, slug) VALUES (?, ?)'); $stmt->execute([$_POST['name'] ?? '', strtolower(str_replace(' ', '-', $_POST['name'] ?? ''))]); }
$categories = get_categories();
?>
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Manage Categories</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head><body class="bg-dark text-white"><div class="container py-4"><h2 class="fw-bold">Manage Categories</h2><form class="row g-3 my-4" method="post"><div class="col-md-8"><input class="form-control" name="name" placeholder="Category name" required></div><div class="col-md-4"><button class="btn btn-accent w-100" type="submit">Add Category</button></div></form><ul class="list-group"><?php foreach ($categories as $cat): ?><li class="list-group-item bg-black text-white border-secondary"><?= escape($cat['name']) ?></li><?php endforeach; ?></ul></div></body></html>
'''

files['admin/orders.php'] = r'''<?php
require_once __DIR__ . '/../includes/config.php';
if (!is_admin()) redirect('admin/login.php');
if ($_SERVER['REQUEST_METHOD'] === 'POST') { $stmt = get_db()->prepare('UPDATE orders SET status = ? WHERE id = ?'); $stmt->execute([$_POST['status'] ?? 'pending', (int)$_POST['id']]); }
$orders = get_db()->query('SELECT o.*, u.full_name FROM orders o LEFT JOIN users u ON o.user_id = u.id ORDER BY o.created_at DESC')->fetchAll();
?>
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Orders</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head><body class="bg-dark text-white"><div class="container py-4"><h2 class="fw-bold">Orders</h2><div class="table-responsive"><table class="table table-dark table-striped"><thead><tr><th>ID</th><th>Customer</th><th>Total</th><th>Status</th><th>Action</th></tr></thead><tbody><?php foreach ($orders as $order): ?><tr><td><?= (int)$order['id'] ?></td><td><?= escape($order['full_name']) ?></td><td><?= format_price($order['total_amount']) ?></td><td><?= escape($order['status']) ?></td><td><form method="post" class="d-flex gap-2"><input type="hidden" name="id" value="<?= (int)$order['id'] ?>"><select class="form-select form-select-sm" name="status"><option value="pending">Pending</option><option value="shipped">Shipped</option><option value="delivered">Delivered</option></select><button class="btn btn-outline-light btn-sm" type="submit">Save</button></form></td></tr><?php endforeach; ?></tbody></table></div></div></body></html>
'''

files['admin/customers.php'] = r'''<?php
require_once __DIR__ . '/../includes/config.php';
if (!is_admin()) redirect('admin/login.php');
$customers = get_db()->query('SELECT * FROM users ORDER BY id DESC')->fetchAll();
?>
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Customers</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head><body class="bg-dark text-white"><div class="container py-4"><h2 class="fw-bold">Customers</h2><div class="table-responsive"><table class="table table-dark table-striped"><thead><tr><th>ID</th><th>Name</th><th>Email</th><th>Role</th></tr></thead><tbody><?php foreach ($customers as $customer): ?><tr><td><?= (int)$customer['id'] ?></td><td><?= escape($customer['full_name']) ?></td><td><?= escape($customer['email']) ?></td><td><?= escape($customer['role']) ?></td></tr><?php endforeach; ?></tbody></table></div></div></body></html>
'''

files['assets/css/style.css'] = r'''body { font-family: 'Poppins', sans-serif; background: #f7f7f8; color: #121212; }
.brand-text { letter-spacing: .3rem; }
.hero-section { min-height: 100vh; background: linear-gradient(135deg, #000, #111); }
.hero-video { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; filter: brightness(.35); }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(120deg, rgba(0,0,0,.8), rgba(0,0,0,.35)); }
.z-2 { z-index: 2; }
.glass-card { background: rgba(255,255,255,.8); backdrop-filter: blur(18px); border: 1px solid rgba(255,255,255,.25); border-radius: 1.5rem; box-shadow: 0 20px 60px rgba(0,0,0,.12); }
.card-product { position: relative; border-radius: 1.4rem; overflow: hidden; background: #fff; box-shadow: 0 14px 40px rgba(0,0,0,.08); transition: transform .3s ease, box-shadow .3s ease; }
.card-product:hover { transform: translateY(-6px); box-shadow: 0 24px 70px rgba(0,0,0,.16); }
.card-product-image { width: 100%; height: 240px; object-fit: cover; display: block; }
.product-badge { position: absolute; top: 16px; left: 16px; padding: .35rem .7rem; background: #00ff84; color: #000; border-radius: 999px; font-size: .75rem; font-weight: 700; }
.btn-accent { background: linear-gradient(90deg, #00ff84, #00c7ff); color: #000; font-weight: 600; }
.eyebrow { letter-spacing: .25rem; text-transform: uppercase; color: #00c7ff; font-size: .8rem; font-weight: 700; }
.countdown { display: flex; gap: 1rem; }
.countdown .unit { background: #111; color: #fff; padding: .75rem 1rem; border-radius: .75rem; min-width: 72px; text-align: center; }
.count-badge { position: absolute; top: -6px; right: -6px; background: #00ff84; color: #000; border-radius: 999px; padding: .1rem .35rem; font-size: .7rem; font-weight: 700; }
.back-to-top { position: fixed; bottom: 24px; right: 24px; display: none; z-index: 999; }
.floating-card { animation: float 4s ease-in-out infinite; }
@keyframes float { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-10px);} }
'''

files['assets/css/responsive.css'] = r'''@media (max-width: 991px) { .hero-section { min-height: auto; } .search-bar { display: none !important; } }
@media (max-width: 768px) { .card-product-image { height: 200px; } .countdown { flex-wrap: wrap; } }
'''

files['assets/css/animation.css'] = r'''.typing-wrap { min-height: 2rem; }
.typing-text::after { content: '|'; animation: blink .8s infinite; }
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
'''

files['assets/js/app.js'] = r'''document.addEventListener('DOMContentLoaded', () => {
  AOS.init({ duration: 800, once: true });
  const typing = document.querySelector('.typing-text');
  if (typing) {
    const words = ['Running', 'Football', 'Lifestyle', 'Training'];
    let idx = 0;
    setInterval(() => { typing.textContent = words[idx % words.length]; idx += 1; }, 1400);
  }
  const backToTop = document.getElementById('backToTop');
  window.addEventListener('scroll', () => { backToTop.style.display = window.scrollY > 400 ? 'block' : 'none'; });
  backToTop?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  document.querySelectorAll('.countdown').forEach((el) => {
    const deadline = new Date(el.dataset.deadline);
    const tick = () => {
      const diff = deadline - new Date();
      if (diff <= 0) return;
      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
      const mins = Math.floor((diff / (1000 * 60)) % 60);
      const secs = Math.floor((diff / 1000) % 60);
      el.innerHTML = `<div class="unit">${days}d</div><div class="unit">${hours}h</div><div class="unit">${mins}m</div><div class="unit">${secs}s</div>`;
    };
    tick(); setInterval(tick, 1000);
  });
});
'''

files['assets/js/slider.js'] = r'''new Swiper('.swiper', { slidesPerView: 1, loop: true, autoplay: { delay: 3500 }, pagination: { el: '.swiper-pagination', clickable: true } });
'''

files['assets/js/cart.js'] = r'''document.addEventListener('click', (event) => {
  const btn = event.target.closest('[data-cart-add]');
  if (!btn) return;
  const toast = document.createElement('div');
  toast.className = 'toast align-items-center text-bg-dark border-0 position-fixed bottom-0 end-0 m-3';
  toast.innerHTML = '<div class="d-flex"><div class="toast-body">Added to cart</div></div>';
  document.body.appendChild(toast);
  bootstrap.Toast.getOrCreateInstance(toast).show();
});
'''

files['assets/js/wishlist.js'] = r'''document.addEventListener('click', (event) => {
  const btn = event.target.closest('[data-wishlist-add]');
  if (!btn) return;
  alert('Added to wishlist');
});
'''

files['assets/js/search.js'] = r'''document.querySelectorAll('input[name="search"]').forEach((input) => {
  input.addEventListener('focus', () => input.setAttribute('placeholder', 'Search for sneakers, apparel and more'));
});
'''

files['database/adidas.sql'] = r'''CREATE DATABASE IF NOT EXISTS adidas_store CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE adidas_store;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(150) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role ENUM('customer','admin') DEFAULT 'customer',
  phone VARCHAR(30) DEFAULT '',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  slug VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  discount_percent INT DEFAULT 0,
  description TEXT NOT NULL,
  sizes VARCHAR(255) NOT NULL,
  colors VARCHAR(255) NOT NULL,
  rating DECIMAL(2,1) DEFAULT 4.8,
  reviews_count INT DEFAULT 0,
  stock INT DEFAULT 10,
  category_id INT,
  thumbnail VARCHAR(255) NOT NULL,
  featured TINYINT(1) DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE reviews (
  id INT AUTO_INCREMENT PRIMARY KEY,
  product_id INT NOT NULL,
  user_id INT NOT NULL,
  rating INT NOT NULL,
  comment TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (product_id) REFERENCES products(id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE wishlist (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  product_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE cart (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT DEFAULT 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE coupons (
  id INT AUTO_INCREMENT PRIMARY KEY,
  code VARCHAR(50) UNIQUE NOT NULL,
  discount_percent INT NOT NULL,
  active TINYINT(1) DEFAULT 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  total_amount DECIMAL(10,2) NOT NULL,
  status VARCHAR(30) DEFAULT 'pending',
  shipping_address TEXT NOT NULL,
  payment_method VARCHAR(30) DEFAULT 'card',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE order_items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE banners (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  active TINYINT(1) DEFAULT 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (full_name, email, password_hash, role, phone) VALUES
('Admin User', 'admin@adidas-store.test', '$2y$12$M1wzIPdRkK5f5t2yMn6H5eQLGx0GnpwUAA7D8R0Smy5M8f2BSfoN6', 'admin', '+1 800 000 0000'),
('Guest Customer', 'customer@adidas-store.test', '$2y$12$M1wzIPdRkK5f5t2yMn6H5eQLGx0GnpwUAA7D8R0Smy5M8f2BSfoN6', 'customer', '+1 800 111 1111');

INSERT INTO categories (name, slug) VALUES
('Running', 'running'),
('Football', 'football'),
('Lifestyle', 'lifestyle'),
('Training', 'training'),
('Basketball', 'basketball'),
('Originals', 'originals'),
('Outdoor', 'outdoor');

INSERT INTO products (name, price, discount_percent, description, sizes, colors, rating, reviews_count, stock, category_id, thumbnail, featured) VALUES
('Ultra Boost 24', 180.00, 15, 'A premium running silhouette engineered for smooth comfort and speed.', '8-12', 'Black/Green', 4.9, 128, 24, 1, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80', 1),
('Predator Elite', 220.00, 10, 'Football boots crafted for precise control and explosive energy.', '7-13', 'White/Black', 4.8, 95, 18, 2, 'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?auto=format&fit=crop&w=900&q=80', 1),
('Forum Low', 110.00, 5, 'Elevated streetwear with a sculpted profile and premium finish.', '6-12', 'Cream/Green', 4.7, 64, 36, 3, 'https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=900&q=80', 1),
('Adizero Pro', 160.00, 20, 'Lightweight training shoe built for acceleration and agility.', '7-11', 'Silver/Black', 4.9, 110, 27, 4, 'https://images.unsplash.com/photo-1491553895911-0055eca6402d?auto=format&fit=crop&w=900&q=80', 1),
('Dame 8', 140.00, 8, 'Modern basketball cushioning with responsive support.', '6-13', 'Core Black', 4.6, 82, 20, 5, 'https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=900&q=80', 0),
('Stan Smith', 95.00, 12, 'The timeless classic reimagined in refined material.', '7-12', 'White', 4.8, 91, 44, 6, 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=900&q=80', 1),
('Terrex Free Hiker', 170.00, 18, 'Outdoor-ready performance with durable grip.', '8-13', 'Olive/Black', 4.7, 76, 15, 7, 'https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=900&q=80', 0),
('Nizza Platform', 120.00, 10, 'Retro profile softened with a contemporary platform sole.', '6-11', 'Pink/White', 4.5, 58, 22, 3, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80', 0),
('Superstar', 100.00, 10, 'Iconic shell toe in a premium premium finish.', '7-12', 'White/Gold', 4.8, 89, 31, 6, 'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?auto=format&fit=crop&w=900&q=80', 0),
('Runfalcon', 90.00, 15, 'A balanced daily trainer with all-day comfort.', '7-12', 'Grey/Green', 4.6, 73, 28, 1, 'https://images.unsplash.com/photo-1511556532299-8f662fc26c06?auto=format&fit=crop&w=900&q=80', 0),
('X Crazyfast', 210.00, 12, 'Fast football boot for explosive speed and agility.', '8-12', 'Solar Red', 4.9, 105, 17, 2, 'https://images.unsplash.com/photo-1584735175097-719d848f8449?auto=format&fit=crop&w=900&q=80', 1),
('Yeezy-inspired', 130.00, 8, 'Luxury minimalism with plush comfort.', '6-10', 'Black', 4.7, 67, 21, 3, 'https://images.unsplash.com/photo-1608231387042-66d1773070a5?auto=format&fit=crop&w=900&q=80', 0),
('Galaxy 6', 150.00, 5, 'Training edition with responsive cushioning.', '8-13', 'Mint/Black', 4.6, 84, 23, 4, 'https://images.unsplash.com/photo-1526256262350-7da7584cf5eb?auto=format&fit=crop&w=900&q=80', 0),
('Harden Vol 8', 155.00, 10, 'Court-ready basketball shoe with full support.', '7-12', 'Purple/Black', 4.7, 88, 19, 5, 'https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=900&q=80', 1),
('Tiro Track Pant', 85.00, 10, 'Performance pants with streamlined comfort.', 'S-XL', 'Black', 4.6, 49, 14, 4, 'https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=900&q=80', 0),
('AEROREADY Hoodie', 95.00, 12, 'Soft warmth and breathable structure for all-day wear.', 'S-XL', 'Grey', 4.7, 51, 13, 3, 'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=900&q=80', 0),
('Sleeveless Tee', 45.00, 5, 'Performance tee for warm-weather sessions.', 'S-XL', 'White', 4.4, 41, 35, 1, 'https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&w=900&q=80', 0),
('Terrex Trail Jacket', 125.00, 15, 'Weather-ready outerwear for rough terrain.', 'S-XL', 'Olive', 4.8, 60, 16, 7, 'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=900&q=80', 0),
('Copa Pure', 190.00, 8, 'Boots with precision engineering and comfort.', '7-13', 'White/Blue', 4.8, 112, 22, 2, 'https://images.unsplash.com/photo-1517649763962-0c623066013b?auto=format&fit=crop&w=900&q=80', 1),
('NMD_R1', 140.00, 12, 'Contemporary street sneaker with futuristic cushioning.', '6-12', 'Grey/Blue', 4.7, 92, 32, 3, 'https://images.unsplash.com/photo-1608231387042-66d1773070a5?auto=format&fit=crop&w=900&q=80', 1),
('Swift Run', 110.00, 10, 'Daily training shoe with smooth transitions.', '7-11', 'Black/White', 4.5, 70, 26, 1, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80', 0),
('Breaknet', 90.00, 5, 'Lightweight comfort for everyday movement.', '6-11', 'Silver', 4.4, 53, 30, 4, 'https://images.unsplash.com/photo-1517649763962-0c623066013b?auto=format&fit=crop&w=900&q=80', 0),
('Run 70s', 130.00, 10, 'Retro running influence with premium support.', '7-12', 'Cream', 4.6, 88, 24, 1, 'https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=900&q=80', 0),
('AEROREADY Tee', 55.00, 8, 'Breathable workout top for high intensity routines.', 'S-XL', 'Neon Green', 4.5, 46, 29, 4, 'https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=900&q=80', 0),
('Sport Backpack', 80.00, 12, 'Structured carryall for training and travel.', 'One Size', 'Black', 4.8, 62, 12, 4, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80', 0),
('Racer TR', 145.00, 10, 'Premium lifestyle sneaker with sculpted lines.', '8-12', 'Taupe', 4.7, 75, 18, 3, 'https://images.unsplash.com/photo-1551489186-cf8726f514f8?auto=format&fit=crop&w=900&q=80', 0),
('Tiro 21 Match', 115.00, 15, 'Performance training essentials built for layers.', 'S-XL', 'Black/White', 4.6, 59, 20, 2, 'https://images.unsplash.com/photo-1496747611176-843222e1e57c?auto=format&fit=crop&w=900&q=80', 0),
('Bask Bold', 135.00, 10, 'Basketball-inspired everyday footwear.', '6-13', 'Multicolor', 4.6, 71, 16, 5, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80', 0),
('Adifit Shorts', 60.00, 5, 'Flexible training shorts with modern silhouette.', 'S-XL', 'Navy', 4.5, 43, 25, 4, 'https://images.unsplash.com/photo-1496747611176-843222e1e57c?auto=format&fit=crop&w=900&q=80', 0),
('Samba OG', 125.00, 8, 'Classic football-inspired shape in modern comfort.', '7-12', 'White/Green', 4.8, 94, 30, 6, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80', 1),
('Gazelle', 110.00, 10, 'Streamlined lifestyle sneaker with soft leather.', '7-12', 'Cream', 4.7, 81, 27, 6, 'https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=900&q=80', 0),
('AEROREADY Cap', 40.00, 5, 'Premium cap designed for comfort and mobility.', 'One Size', 'Black', 4.4, 38, 17, 3, 'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=900&q=80', 0),
('Run 100s', 115.00, 12, 'Precision comfort for everyday miles.', '7-12', 'Blue/White', 4.6, 77, 25, 1, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80', 0),
('Sports Bra', 70.00, 10, 'Supportive fit with premium stretch fabric.', 'XS-L', 'Black', 4.7, 63, 18, 4, 'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=900&q=80', 0),
('Trail Runners', 135.00, 10, 'Outdoor-ready support with a durable outsole.', '7-12', 'Brown', 4.7, 66, 20, 7, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80', 0),
('Fractal Shoes', 165.00, 15, 'A futuristic take on comfort and style.', '8-12', 'Silver/Black', 4.8, 86, 24, 3, 'https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=900&q=80', 0),
('Energy Hoodie', 100.00, 8, 'Soft premium fleece designed for rest days and workouts.', 'S-XL', 'Green', 4.6, 55, 19, 4, 'https://images.unsplash.com/photo-1496747611176-843222e1e57c?auto=format&fit=crop&w=900&q=80', 0),
('Primeknit Trainers', 175.00, 10, 'Premium knit upper for next-level comfort.', '6-12', 'Black/Neon', 4.9, 103, 21, 6, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80', 1),
('Core Shorts', 52.00, 8, 'Modern performance shorts with a secure fit.', 'S-XL', 'Pink', 4.5, 48, 26, 4, 'https://images.unsplash.com/photo-1496747611176-843222e1e57c?auto=format&fit=crop&w=900&q=80', 0),
('NMD S1', 155.00, 10, 'Contemporary sneaker with sculpted cushioning.', '7-12', 'Grey', 4.7, 73, 20, 3, 'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?auto=format&fit=crop&w=900&q=80', 0);

INSERT INTO coupons (code, discount_percent) VALUES ('ADIDAS10', 10), ('SPRING20', 20);
INSERT INTO banners (title, image_url) VALUES ('New Arrival', 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=1400&q=80');
INSERT INTO reviews (product_id, user_id, rating, comment) VALUES (1, 2, 5, 'Incredible comfort and style. The cushioning is outstanding.'), (2, 2, 4, 'Great lockdown and premium feel.'), (3, 2, 5, 'Looks amazing and feels superb.');
'''

files['README.md'] = r'''# Adidas Store

Premium Adidas-inspired e-commerce storefront built with PHP, MySQL, Bootstrap, and modern UI patterns. It includes a storefront, shopping cart, wishlist, authentication, checkout flow, and an admin panel.

## Features
- Premium responsive storefront
- Product catalog, filters, search, wishlist, cart, checkout
- Admin dashboard and product management
- SEO and accessibility-friendly structure
- Database-driven product catalog with sample data

## Requirements
- XAMPP with Apache, MySQL, PHP 8.3+
- Visual Studio Code

## Installation
1. Place this project inside your XAMPP `htdocs` folder, for example `C:/xampp/htdocs/adidas-store`.
2. Start Apache and MySQL in XAMPP.
3. Open phpMyAdmin and create a database named `adidas_store` or let the app create it automatically.
4. Import `database/adidas.sql` if needed.
5. Visit http://localhost/adidas-store/

## Default Login
- Admin: admin@adidas-store.test / adidas123
- Customer: customer@adidas-store.test / adidas123
'''

files['robots.txt'] = 'User-agent: *\nAllow: /\nSitemap: http://localhost/adidas-store/sitemap.xml\n'
files['sitemap.xml'] = r'''<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>http://localhost/adidas-store/</loc></url>
  <url><loc>http://localhost/adidas-store/pages/shop.php</loc></url>
  <url><loc>http://localhost/adidas-store/pages/about.php</loc></url>
  <url><loc>http://localhost/adidas-store/pages/contact.php</loc></url>
  <url><loc>http://localhost/adidas-store/pages/login.php</loc></url>
  <url><loc>http://localhost/adidas-store/pages/register.php</loc></url>
</urlset>
'''

# Write files
for rel, content in files.items():
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')

# Create placeholder asset directories
(root / 'assets/images/hero/.gitkeep').write_text('', encoding='utf-8')
(root / 'assets/images/products/.gitkeep').write_text('', encoding='utf-8')
(root / 'assets/images/banner/.gitkeep').write_text('', encoding='utf-8')
(root / 'assets/images/icons/.gitkeep').write_text('', encoding='utf-8')
(root / 'assets/fonts/.gitkeep').write_text('', encoding='utf-8')
(root / 'uploads/.gitkeep').write_text('', encoding='utf-8')

# Create logo placeholder png via base64
from base64 import b64decode
(root / 'assets/images/logo.png').write_bytes(b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAACklEQVR4nGMAAIAAeIhG9QAAAABJRU5ErkJggg=='))

print('Project files written to', root)
