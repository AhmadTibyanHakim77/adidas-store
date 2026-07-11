<?php
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
