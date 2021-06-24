const popup = document.querySelector(".popup");

const chooseplayer = document.querySelector(".chooseplayers");
const exit = document.querySelector(".option3");

const shower = () => {
    chooseplayer.style.display = "block";
  
  
  
};
const hider = () => {
  chooseplayer.style.display = "none";



};
popup.addEventListener("click", shower);
exit.addEventListener("click", hider);

