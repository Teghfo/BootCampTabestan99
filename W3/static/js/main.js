(function ($) {
  $.extend({
    persianNumbers: function (input) {
      var persian = {
        0: "۰",
        1: "۱",
        2: "۲",
        3: "۳",
        4: "۴",
        5: "۵",
        6: "۶",
        7: "۷",
        8: "۸",
        9: "۹",
      };
      var string = (input + "").split("");
      var count = string.length;
      var num;
      for (var i = 0; i <= count; i++) {
        num = string[i];
        if (persian[num]) {
          string[i] = persian[num];
        }
      }
      return string.join("");
    },
  });
})(jQuery);

$(document).ready(function () {
  var now = new Date();
  $("#date").text(
    now.getDay() + "-" + now.getMonth() + "-" + now.getFullYear()
  );
});

console.log("salam bacheha");
console.log("ashkan");

var tag = document.createElement("p");
var text = document.createTextNode("Tutorix is the best e-learning platform");
tag.appendChild(text);
var element = document.getElementById("new");
element.appendChild(tag);

$(document).ready(function () {
  $("#new").click(function () {
    $(this).hide();
  });
});
