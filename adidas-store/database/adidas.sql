CREATE DATABASE IF NOT EXISTS adidas_store CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE adidas_store;

CREATE TABLE IF NOT EXISTS categories (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  slug VARCHAR(100) NOT NULL UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  category_id INT NOT NULL,
  name VARCHAR(200) NOT NULL,
  slug VARCHAR(200) NOT NULL UNIQUE,
  description TEXT,
  price DECIMAL(10,2) NOT NULL,
  discount_percent INT DEFAULT 0,
  thumbnail VARCHAR(255) DEFAULT 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80',
  rating DECIMAL(2,1) DEFAULT 4.5,
  reviews_count INT DEFAULT 0,
  stock INT DEFAULT 10,
  sizes VARCHAR(100) DEFAULT 'M, L, XL',
  colors VARCHAR(100) DEFAULT 'Black, White',
  featured TINYINT(1) DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(150) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(20) DEFAULT 'customer',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS orders (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  total_amount DECIMAL(10,2) NOT NULL,
  status VARCHAR(30) DEFAULT 'pending',
  shipping_address TEXT,
  payment_method VARCHAR(50) DEFAULT 'card',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS order_items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS reviews (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  product_id INT,
  rating INT DEFAULT 5,
  comment TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS wishlist (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  product_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS banners (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(200),
  image VARCHAR(255),
  active TINYINT(1) DEFAULT 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS coupons (
  id INT AUTO_INCREMENT PRIMARY KEY,
  code VARCHAR(50) UNIQUE NOT NULL,
  discount_percent INT DEFAULT 10,
  active TINYINT(1) DEFAULT 1
);

INSERT INTO categories (name, slug) VALUES
('Running', 'running'),
('Football', 'football'),
('Training', 'training'),
('Lifestyle', 'lifestyle');

INSERT INTO products (category_id, name, slug, description, price, discount_percent, thumbnail, rating, reviews_count, stock, sizes, colors, featured) VALUES
(1, 'Adidas Ultraboost 24', 'adidas-ultraboost-24', 'Responsive cushioning for everyday performance.', 220.00, 15, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80', 4.8, 182, 18, '8-12', 'Core Black, Solar Red', 1),
(1, 'Adidas NMD R1', 'adidas-nmd-r1', 'Street-ready comfort with futuristic design.', 160.00, 10, 'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?auto=format&fit=crop&w=800&q=80', 4.6, 94, 12, '7-11', 'Cloud White, Navy', 1),
(2, 'Adidas Predator', 'adidas-predator', 'Precision detailing for better control.', 180.00, 12, 'https://images.unsplash.com/photo-1511556532299-8f662fc26c06?auto=format&fit=crop&w=800&q=80', 4.7, 71, 9, 'M, L, XL', 'Black, Silver', 1),
(3, 'Adidas Essentials Hoodie', 'adidas-essentials-hoodie', 'Soft everyday layer designed for motion.', 85.00, 5, 'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=800&q=80', 4.5, 58, 20, 'S, M, L', 'Grey, Black', 0),
(4, 'Adidas Forum Low', 'adidas-forum-low', 'A timeless basketball-inspired silhouette.', 140.00, 8, 'https://images.unsplash.com/photo-1543508282-6319a3e2621f?auto=format&fit=crop&w=800&q=80', 4.9, 133, 15, '8-12', 'White, Blue', 1),
(2, 'Adidas Copa Pure', 'adidas-copa-pure', 'Comfort and control for modern football.', 130.00, 0, 'https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=800&q=80', 4.4, 42, 11, '7-10', 'Green, White', 0),
(3, 'Adidas Training Tee', 'adidas-training-tee', 'Breathable comfort for training sessions.', 45.00, 0, 'https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=800&q=80', 4.3, 26, 25, 'S, M, L', 'Black, Pink', 0),
(4, 'Adidas Stan Smith', 'adidas-stan-smith', 'Classic style with clean premium finish.', 110.00, 10, 'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?auto=format&fit=crop&w=800&q=80', 4.7, 72, 14, '8-12', 'White, Green', 0);

INSERT INTO users (full_name, email, password_hash, role) VALUES
('Admin User', 'admin@example.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'admin'),
('Customer Demo', 'customer@example.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'customer');

INSERT INTO reviews (user_id, product_id, rating, comment) VALUES
(2, 1, 5, 'Amazing comfort and premium quality.'),
(2, 2, 4, 'Stylish and lightweight.'),
(1, 4, 5, 'Feels premium and perfect for daily wear.');

INSERT INTO banners (title, image, active) VALUES
('Spring Drop', 'https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=1200&q=80', 1),
('Performance Essentials', 'https://images.unsplash.com/photo-1483721310020-03333e577078?auto=format&fit=crop&w=1200&q=80', 1);

INSERT INTO coupons (code, discount_percent, active) VALUES
('ADIDAS10', 10, 1),
('WELCOME20', 20, 1);
