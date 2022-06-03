<?php
session_start();

if (!isset($_SESSION['try']))
    $_SESSION['try'] = 0;

if ($_SESSION['try'] == 3) {
    sleep(15);
    $_SESSION['try'] = 0;
}

//echo "<pre>".print_r($GLOBALS, true)."</pre>";

if($_POST['submit']) {
    $dblocation = "localhost";
    $dbuser = "root";
    $dbpasswd = "root";
    $dbname = "users";

    mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
    $con = mysqli_connect($dblocation,$dbuser,$dbpasswd, $dbname);

    if (!$con)
    {
        echo "Ошибка: Невозможно установить соединение с MySQL.". PHP_EOL;
        echo "Код ошибки errno: " . mysqli_connect_errno().PHP_EOL;
        echo "Текст ошибки error: " . mysqli_connect_error().PHP_EOL;
        exit;
    }

    $username = $_POST['username'];
    $password = $_POST['password'];
    $query = "SELECT * FROM `users` WHERE `login` = '$username' AND `password` = '$password'";
    $result = mysqli_query($con,$query);
    $user = mysqli_fetch_assoc($result);

    if (($_SESSION['try'] < 3) && (count($user) != 0)) {
        $_SESSION['logged_user'] =  $user['name'] . " " . $user['lastname'] ;
        header("Location: secretplace.php");
        exit;
    }

    if ($_SESSION['try'] < 3)
    {
        $_SESSION['message'] = "Количество оставшихся попыток входа: " . (2 - $_SESSION['try']);
        $_SESSION['try'] += 1;
    }
    if ($_SESSION['try'] == 3)
    {
        $_SESSION['stop'] = "Повторите попытку через 15 секунд";
    }

    mysqli_close($con);
}
?>
<html lang="ru">
<head>
    <title>Ошибка входа</title>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="style.css">
 </head>
<body>
<?php
print '<p>' . $_SESSION['message'] . '</p>';
if ($_SESSION['message'] == 3)
    print '<p>' . $_SESSION['stop'] . '</p>';
?>
    <form action="index.php">
        <p class="error">Вы ввели неверный логин или пароль!</p>
        <button type="submit">Вернуться</button>
    </form>

</body>
</html>
