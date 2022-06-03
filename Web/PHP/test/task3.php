<?php
session_start();
$answer2 = $_POST['answer2'];

$_SESSION['answer2'] = $answer2;
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Задание 3</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <h1>Тест по программированию в компьютерных сетях</h1>
    <form action="task4.php" method="POST">
        <h3>Задание 3</h3>
        <p><b>Задание 1</b></p>
        <p><input type="radio" name='answer3' value='1'>ответ 1</p>
        <p><input type="radio" name='answer3' value='2'>ответ 2</p>
        <p><input type="radio" name='answer3' value='3'>ответ 3</p>
        <p><input type="radio" name='answer3' value='4'>ответ 4</p>
        <button type="submit" name="submit" value="submit">Ответить</button>
    </form>
</body>
</html>