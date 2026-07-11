<aside class="glass-card p-4 sticky-top" style="top: 100px;">
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
