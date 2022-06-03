<?
echo "<!DOCTYPE html><html><head><meta charset='utf-8'/><link rel=stylesheet href=style.css></head><body style = 'font-family: Book Antiqua, serif;'>";
	print '<div class="content">';
	print '<div class="form1">';
	print '<form action="index.html" method="POST">';
	if ($_POST['number'] == '13') {
	    print '<p style="color: red; font-size: 1.5rem;">ВЕРНО</p>';
	}
	else {
        print $_POST['number'].' - неверно.';
	    if ($_POST['number'] < '13') {
	        print '<p>Загаданное число больше.</p>';
	    }
	    else {
	        print '<p>Загаданное число меньше.</p>';
	    }

	    print '<button type ="submit">Попробовать ещё раз.</button>';
	}
	print '</form>';
    print "</div>";
    print "</div>";
echo "</body></html>";
?>