var ajax = new XMLHttpRequest();
ajax.open("GET", "core/data.php", true);
ajax.send();
ajax.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
      console.log(this.responseText);
      var data = JSON.parse(this.responseText);
      // console.log(data);
      var html = "";
for(var a = 0; a < data.length; a++) {
  var name = data[a].name;
  console.log(data[a].sex);
  var sex = data[a].sex;
  var games = data[a].games;
  var email = data[a].email;

  html += "<tr>";
      html += "<td>" + name + "</td>";
      html += "<td>" + sex + "</td>";
      html += "<td>" + games + "</td>";
  html += "</tr>";
}
data = document.querySelector("#data");
data.innerHTML +=html;
  }
};
