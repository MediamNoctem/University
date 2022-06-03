<?php
session_start();
//echo session_id();

if(!isset($_SESSION['logged_user'])){
    header("Location: index.php");
    exit;
}
?>
<html lang="ru">
<head>
    <title>Секретная страница</title>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <form action="index.php">
        <p>Здравствуй, <?php echo $_SESSION['logged_user']; ?>, ты на секретной странице!</p>
        <button type="submit">Вернуться</button>
    </form>
</body>
</html>

