<?php
session_start();
$answer10 = $_POST['answer10'];

$_SESSION['answer10'] = $answer10;
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Результаты</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <h1>Тест по программированию в компьютерных сетях</h1>

    <form action="index.html">
        <h3>Результаты:</h3>

        <?php
        $answers = ["answer1" => "1", "answer2" => "1", "answer3" => "1", "answer4" => "1", "answer5" => "1", "answer6" => "1", "answer7" => "1", "answer8" => "1", "answer9" => "1", "answer10" => "1"];

        foreach ($_SESSION as $key => $value) {
            echo "$key: $value";
            if ($_SESSION[$key] == $answers[$key])
                print "<p class='valid'> Верно</p><br>";
            else
                print "<p class='invalid'> Неверно</p><br>";
        }
        session_destroy();
        ?>
        <button>Вернуться</button>
    </form>
</body>
</html>