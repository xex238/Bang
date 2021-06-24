document.querySelector("#signup-submit").onclick = function (event) {
  event.preventDefault();
  let name = document.querySelector("#signup-name").value;
  let pass = document.querySelector("#signup-pass").value;
  let email = document.querySelector("#signup-email").value;
  let birthday = document.querySelector("#signup-birthday").value;

  let sex = document.querySelectorAll(".sex");

  for (let i = 0; i < sex.length; i++) {
    if (sex[i].checked) {
      sex = sex[i].value;
      break;
    }
  }
  document.getElementById("signup-name").value = "";
  document.getElementById("signup-pass").value = "";
  document.getElementById("signup-email").value = "";
  document.getElementById("signup-birthday").value = "";

  console.log(sex);

  let data = {
    name: name,
    pass: pass,
    email: email,
    birthday: birthday,
    sex: sex,
  };

  ajax("core/signup.php", "POST", login, data);

  function login(result) {
    console.log(result);
  }
};
