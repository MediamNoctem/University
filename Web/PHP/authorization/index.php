<html lang="ru">
<head>
    <title>Главная</title>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<?php
//if ($_SESSION['try'] == 3)
//    sleep(15);
//?>
    <form method="POST" action="authorize.php">
        <div class="form-element">
            <label>Логин</label>
            <input type="text" name="username" pattern="[a-zA-Z0-9]+" required />
        </div>
        <div class="form-element">
            <label>Пароль</label>
            <input type="password" name="password" required />
        </div>
        <button type="submit" name="submit" value="submit">Войти</button>
    </form>
</body>
</html>
