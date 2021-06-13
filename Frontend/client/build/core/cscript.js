document.querySelector("#contact-submit").onclick = function (event) {
  event.preventDefault();
  let name = document.querySelector("#contact-name").value;
  let email = document.querySelector("#contact-email").value;
  let text = document.querySelector("#contact-text").value;
  document.getElementById("contact-name").value = "";
  document.getElementById("contact-email").value = "";
  document.getElementById("contact-text").value = "";
  let data = {
    name: name,
    email: email,
    text: text,
  };

  ajax("core/contact.php", "POST", login, data);

  function login(result) {
    console.log(result);
  }
};
