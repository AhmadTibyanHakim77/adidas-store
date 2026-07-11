  <footer class="py-5 bg-dark text-white">
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
