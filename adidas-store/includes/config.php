<?php
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

function ensure_database_schema(PDO $pdo): void {
    $tableCheck = $pdo->query("SHOW TABLES LIKE 'categories'");
    if ($tableCheck && $tableCheck->fetch()) {
        return;
    }

    $sqlFile = APP_ROOT . '/database/adidas.sql';
    if (!is_file($sqlFile)) {
        return;
    }

    $sql = file_get_contents($sqlFile);
    $sql = preg_replace('/--.*$/m', '', $sql);
    $sql = str_replace(["\r\n", "\r"], "\n", $sql);
    $statements = preg_split('/;\s*(?:\n|$)/', $sql);

    foreach ($statements as $statement) {
        $statement = trim($statement);
        if ($statement === '' || preg_match('/^(CREATE\s+DATABASE|USE\s+)/i', $statement)) {
            continue;
        }
        try {
            $pdo->exec($statement);
        } catch (PDOException $e) {
            // Ignore duplicate/optional statements during first boot.
        }
    }
}

ensure_database_schema($pdo);

function asset($path) { return BASE_URL . '/assets/' . ltrim($path, '/'); }
function url($path) { return BASE_URL . '/' . ltrim($path, '/'); }

if (!function_exists('get_db')) {
    require_once APP_ROOT . '/includes/functions.php';
}

if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}

function csrf_token() { return $_SESSION['csrf_token']; }
function csrf_field() { return '<input type="hidden" name="csrf_token" value="' . htmlspecialchars(csrf_token()) . '">'; }
function require_csrf() { if (!hash_equals($_SESSION['csrf_token'] ?? '', $_POST['csrf_token'] ?? '')) throw new Exception('Invalid CSRF token.'); }
