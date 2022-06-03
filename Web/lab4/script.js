function clickOnButton(i) {
    if (getComputedStyle(document.getElementsByClassName("sol")[i]).display === 'none')
            document.getElementsByClassName("sol")[i].style.display = 'block'
    else document.getElementsByClassName("sol")[i].style.display = 'none'
}

function zero_first_format(value) {
    if (value < 10)
    {
        value='0' + value;
    }
    return value;
}

function date_time() {
    let current_datetime = new Date();
    let day_of_week;
    switch (current_datetime.getDay()) {
        case 1:
            day_of_week = 'Понедельник';
            break;
        case 2:
            day_of_week = 'Вторник';
            break;
        case 3:
            day_of_week = 'Среда';
            break;
        case 4:
            day_of_week = 'Четверг';
            break;
        case 5:
            day_of_week = 'Пятница';
            break;
        case 6:
            day_of_week = 'Суббота';
            break;
        case 0:
            day_of_week = 'Воскресенье';
            break;
    }
    let day = zero_first_format(current_datetime.getDate());
    let month;
    switch (current_datetime.getMonth() + 1) {
        case 1:
            month = 'января';
            break;
        case 2:
            month = 'февраля';
            break;
        case 3:
            month = 'марта';
            break;
        case 4:
            month = 'апреля';
            break;
        case 5:
            month = 'мая';
            break;
        case 6:
            month = 'июня';
            break;
        case 7:
            month = 'июля';
            break;
        case 8:
            month = 'августа';
            break;
        case 9:
            month = 'сентября';
            break;
        case 10:
            month = 'октября';
            break;
        case 11:
            month = 'ноября';
            break;
        case 12:
            month = 'декабря';
            break;
    }
    let year = current_datetime.getFullYear();
    let hours = zero_first_format(current_datetime.getHours());
    let minutes = zero_first_format(current_datetime.getMinutes());
    let seconds = zero_first_format(current_datetime.getSeconds());

    return day_of_week + ", " + day+" " + month+" " + year + ", " + hours + " / " + minutes + " / " + seconds;
}

function printDate() {
    setInterval(function () {
        document.getElementsByClassName("sol")[0].innerHTML = '<p>' + date_time() + '</p>';
    }, 1000);
    document.getElementsByClassName("sol")[0].style.textAlign = 'center';
    document.getElementsByClassName("sol")[0].style.height = '120px';
}

printDate();

function Calendar(id, year, month0) {
    let Dlast = new Date(year,month0 + 1,0).getDate(),
        D = new Date(year,month0,Dlast),
        DNlast = new Date(D.getFullYear(),D.getMonth(),Dlast).getDay(),
        DNfirst = new Date(D.getFullYear(),D.getMonth(),1).getDay(),
        calendar = '<tr>',
        month=["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"];

    if (DNfirst !== 0) {
        for(let i = 1; i < DNfirst; i++)
            calendar += '<td></td>';
    }
    else {
        for(let i = 0; i < 6; i++)
            calendar += '<td></td>';
    }

    for (let i = 1; i <= Dlast; i++) {
        if (i === new Date().getDate() && D.getFullYear() === new Date().getFullYear() && D.getMonth() === new Date().getMonth()) {
            calendar += '<td class="today">' + i + '</td>';
        }
        else {
            calendar += '<td>' + i + '</td>';
        }
        if (new Date(D.getFullYear(),D.getMonth(),i).getDay() === 0) {
            calendar += '</tr><tr>';
        }
    }

    for (let  i = DNlast; i < 7; i++)
        calendar += '<td></td>';

    document.querySelector('.'+id+' tbody').innerHTML = calendar;
    document.querySelector('.'+id+' thead td:nth-child(2)').innerHTML = month[D.getMonth()] +' '+ D.getFullYear();
    document.querySelector('.'+id+' thead td:nth-child(2)').dataset.month = D.getMonth().toString();
    document.querySelector('.'+id+' thead td:nth-child(2)').dataset.year = D.getFullYear().toString();
    if (document.querySelectorAll('.'+id+' tbody tr').length < 6) {
        document.querySelector('.'+id+' tbody').innerHTML += '<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>';
    }
}
Calendar("calendar", new Date().getFullYear(), new Date().getMonth());

document.querySelector('.calendar thead tr:nth-child(1) td:nth-child(1)').onclick = function() {
    Calendar("calendar", document.querySelector('.calendar thead td:nth-child(2)').dataset.year, parseFloat(document.querySelector('.calendar thead td:nth-child(2)').dataset.month)-1);
}

document.querySelector('.calendar thead tr:nth-child(1) td:nth-child(3)').onclick = function() {
    Calendar("calendar", document.querySelector('.calendar thead td:nth-child(2)').dataset.year, parseFloat(document.querySelector('.calendar thead td:nth-child(2)').dataset.month)+1);
}

function findTable() {
    let count = document.querySelectorAll('table')[0].querySelectorAll('*').length;
    document.getElementsByClassName('sol')[2].innerHTML += '<p>' + 'Количество дочерних тегов для тега <strong><i>table</i></strong>:' + '</p>';
    document.getElementsByClassName('sol')[2].innerHTML += '<p>' + count + '</p>';
}

findTable();

function printText() {
    let i = 0;
    setInterval(function () {
        document.getElementsByClassName('block')[i].innerHTML += '<p>Hello world!</p>';
        i += 1;
    }, 80);
}

function createTable() {
    let c_row = parseInt(prompt('Введите количество строк.')),
        c_col = parseInt(prompt('Введите количество столбцов.')),
        table = '<table>';
    table += '<tbody>';
    for (let i = 0; i < c_row; i += 1) {
        table += '<tr>';
        for (let j = 0; j < c_col; j += 1)
            table += '<td>' + parseInt(prompt('Введите элемент строки ' + i.toString() + ' столбца ' + j.toString() + '.')) + '</td>'
        table += '</tr>';
    }
    table += '</tbody>';
    table += '</table>';
    document.getElementsByClassName('table')[0].innerHTML += table;

    deleteElemTable(c_col);
}

function deleteElemTable(col) {
    let tds = document.getElementsByClassName('table')[0].querySelectorAll('td');
    for (let i = 0; i < tds.length; i++) {
        tds[i].addEventListener('click', function func() {
            let answer = confirm("Вы действительно хотите удалить элемент со значением " + tds[i + col].textContent + "?");
            if (answer) {
                tds[i + col].remove();
                tds[i + col].removeEventListener('click', func);
            }
        });
    }
}

function pressKey() {
    let sol = document.getElementsByClassName('sol')[5];
    document.addEventListener('keydown', function func(e1) {
        if (e1.key === 'Escape') {
            let input = document.createElement('input');
            sol.appendChild(input);
        }
        let input = document.getElementsByClassName('sol')[5].querySelectorAll('input');
        for (let i = 0; i < input.length; i++) {
            input[i].addEventListener('keydown', function key(e2) {
                if (e2.key.match(/[^a-zA-Zа-яА-Я]/))
                    return e2.preventDefault();
                input[i].removeEventListener('keydown', key);
            });
            sol.removeEventListener('keydown', func);
        }
    });
}

pressKey();

function hide() {
    if (getComputedStyle(document.getElementById("menu")).display !== "none")
    {
        document.getElementById("menu").style.display = "none";
    } else {
        document.getElementById("menu").style.display = "block";
    }
}
function toggle(x) {
    x.classList.toggle("change");
}

let count = 0;

function slowlyHide(i) {
    let menu_li = document.getElementsByClassName('menu_li')[i],
        op = 0.8;
    setInterval(function () {
        menu_li.style.opacity = op.toString();
        op -= 0.1;
    }, 50);
    setTimeout(function () {
        menu_li.style.display = "None"
    }, 530);
    count += 1;
    if (count === 5) {
        document.getElementById('menu_ul').outerHTML = '<p>Сладости закончились!</p>';
    }
}

function ex8(setEvent) {
    setTimeout(function () {document.getElementById("img").style.opacity = "100"; }, 50)
    setEvent();
}

function setEvent() {
    document.getElementById("img").onmouseover = function (event) {
        event.target.style.opacity = "0";
    }
    document.getElementById("img").onmouseout = function (event) {
        event.target.style.opacity = "100%";
    }
}

function checkPhone(x) {
    let tel = new RegExp(/^[+]?[0-9][(| ]?[0-9]{3}[)| ]?[-]?[0-9]{3}[-| ]?[0-9]{2}[-| ]?[0-9]{2}$/im)
    if (x.value.search(tel)===-1 && x.value!=='') {
        x.className = 'error';
        document.getElementById('error').innerHTML ='Неверный формат номера телефона'
    }
}
function checkEmail(x) {
    let email = new RegExp(/^[a-zA-Z0-9]{2,}@([a-zA-Z0-9]{2,}\.)+[a-zA-Z0-9]{2,4}$/im)
    if (x.value.search(email)===-1 && x.value!=='') {
        x.className = 'error';
        document.getElementById('error').innerHTML ='Неверный формат почты'
    }
}
function checkText(x) {
    if (x.value.search(/[^a-zA-Zа-яА-Я]/)!==-1) {
        x.className = 'error';
        document.getElementById('error').innerHTML ='Поле должно содержать только буквы'
    }
}
function checkPass(x) {
    let p1 = document.getElementById('pass1').value
    if (x.value !== p1) {
        x.className = 'error';
        document.getElementById('error').innerHTML ='Пароль не подтвержден'
    }
}
function onF(x) {
    if (x.className === 'error') {
        x.className = 'inp';
        document.getElementById('error').innerHTML = '';
    }
}
function delErrors() {
    let inps = document.getElementsByClassName("error");
    while(inps.length > 0) {
        inps.item(0).className = 'inp';
    }
    document.getElementById('error').innerHTML = '';
}