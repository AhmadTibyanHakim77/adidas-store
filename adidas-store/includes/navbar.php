<?php
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
        <div class="rounded-circle bg-dark text-white d-flex align-items-center justify-content-center" style="width:42px;height:42px;">A</div>
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
