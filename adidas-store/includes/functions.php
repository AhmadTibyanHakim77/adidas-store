<?php
function get_db() { global $pdo; return $pdo; }
function redirect($path) { header('Location: ' . url($path)); exit; }
function escape($value) { return htmlspecialchars((string)$value, ENT_QUOTES, 'UTF-8'); }
function get_categories() { try { $stmt = get_db()->query('SELECT * FROM categories ORDER BY name ASC'); return $stmt->fetchAll(); } catch (PDOException $e) { return []; } }
function get_product($id) { try { $stmt = get_db()->prepare('SELECT p.*, c.name AS category_name FROM products p LEFT JOIN categories c ON p.category_id = c.id WHERE p.id = ?'); $stmt->execute([$id]); return $stmt->fetch(); } catch (PDOException $e) { return false; } }
function get_products($limit = 12, $category = null, $search = null, $sort = null) { try { $sql = 'SELECT p.*, c.name AS category_name FROM products p LEFT JOIN categories c ON p.category_id = c.id WHERE 1=1'; $params = []; if ($category) { $sql .= ' AND p.category_id = ?'; $params[] = $category; } if ($search) { $sql .= ' AND (p.name LIKE ? OR p.description LIKE ?)'; $params[] = '%' . $search . '%'; $params[] = '%' . $search . '%'; } switch ($sort) { case 'price_asc': $sql .= ' ORDER BY p.price ASC'; break; case 'price_desc': $sql .= ' ORDER BY p.price DESC'; break; case 'new': $sql .= ' ORDER BY p.created_at DESC'; break; case 'rating': $sql .= ' ORDER BY p.rating DESC'; break; default: $sql .= ' ORDER BY p.featured DESC, p.created_at DESC'; break; } $sql .= ' LIMIT ?'; $params[] = (int)$limit; $stmt = get_db()->prepare($sql); $stmt->execute($params); return $stmt->fetchAll(); } catch (PDOException $e) { return []; } }
function get_related_products($category_id, $current_id) { try { $stmt = get_db()->prepare('SELECT * FROM products WHERE category_id = ? AND id != ? ORDER BY created_at DESC LIMIT 4'); $stmt->execute([$category_id, $current_id]); return $stmt->fetchAll(); } catch (PDOException $e) { return []; } }
function get_banners() { try { $stmt = get_db()->query('SELECT * FROM banners WHERE active = 1 ORDER BY created_at DESC'); return $stmt->fetchAll(); } catch (PDOException $e) { return []; } }
function get_reviews($limit = 3) { try { $stmt = get_db()->prepare('SELECT r.*, u.full_name AS customer_name FROM reviews r LEFT JOIN users u ON r.user_id = u.id ORDER BY r.created_at DESC LIMIT ?'); $stmt->bindValue(1, (int)$limit, PDO::PARAM_INT); $stmt->execute(); return $stmt->fetchAll(); } catch (PDOException $e) { return []; } }
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
