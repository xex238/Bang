const login = document.querySelector(".login");
const regin = document.querySelector(".regin");
const showlog = document.querySelector("#showlog");
const showreg = document.querySelector("#showreg");
const cancellog = document.querySelector("#cancellog");
const cancelreg = document.querySelector("#cancelreg");

const shower = () => {
    login.style.display = "block";
  
  
  
};
const hider = () => {
  login.style.display = "none";



};
const shower2 = () => {
  regin.style.display = "block";



};
const hider2 = () => {
regin.style.display = "none";



};
showlog.addEventListener("click", shower);
cancellog.addEventListener("click", hider);
showreg.addEventListener("click", shower2);
cancelreg.addEventListener("click", hider2);

