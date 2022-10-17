$(document).ready(function () {
    $(".sidenav").sidenav({
        edge: "right"
    });
    $('.parallax').parallax();
    $(".collapsible").collapsible();
    $('input').characterCounter();
    $('.fixed-action-btn').floatingActionButton()
    $('.datepicker').datepicker();
    $('select').formSelect();
});

window.setTimeout(function () {
    $("#flash").fadeTo(500, 0)
}, 4000);

window.onload = function () {

    var seconds = 00;
    var tens = 00;
    var minutes = 00;
    var appendMinutes = document.getElementById("minutes")
    var appendSeconds = document.getElementById("seconds")
    var timerButton = document.getElementById('timer-button');
    var durationField = document.getElementById('duration')
    var Interval;

    timerButton.onclick = function () {
        if (timerButton.value == "START") {
            timerButton.value = "STOP"

            clearInterval(Interval);
            Interval = setInterval(startTimer, 1000);
        } else if (timerButton.value == "STOP") {
            timerButton.value = "START"
            durationField.value = appendMinutes.textContent.toString() + ":" + appendSeconds.textContent.toString()
            document.getElementById("durationLabel").classList.add("active")

            clearInterval(Interval);
            tens = "00";
            seconds = "00";
            minutes = "00";
            appendMinutes.innerHTML = minutes;
            appendSeconds.innerHTML = seconds;
        }
    }


    function startTimer() {
        seconds++;

        if (seconds <= 9) {
            appendSeconds.innerHTML = "0" + seconds;
        }

        if (seconds > 9) {
            appendSeconds.innerHTML = seconds;
        }

        if (seconds == 60 && minutes <= 9) {
            minutes++;
            appendMinutes.innerHTML = "0" + minutes;
            appendSeconds.innerHTML = "00";
            seconds = 0;
            tens = 0;
        }

        if (seconds == 60 && minutes > 9) {
            minutes++;
            appendMinutes.innerHTML = minutes;
            appendSeconds.innerHTML = "00";
            seconds = 0;
            tens = 0;
        }
    }
}