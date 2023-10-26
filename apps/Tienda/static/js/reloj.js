function updateClock() {
    var now = new Date();
    var hour = now.getHours();
    var minute = now.getMinutes();
    var second = now.getSeconds();
    var ampm = hour >= 12 ? "PM" : "AM";
    hour = hour % 12;
    hour = hour ? hour : 12;
    minute = minute < 10 ? "0" + minute : minute;
    second = second < 10 ? "0" + second : second;
    var time = hour + ":" + minute + ":" + second + " " + ampm;
    document.getElementById("clock").innerHTML = time;
    setTimeout(updateClock, 1000);
  }
  updateClock();