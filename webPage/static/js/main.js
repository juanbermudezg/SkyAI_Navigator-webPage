const username = document.getElementById("user")
const password = document.getElementById("pass")
const email = document.getElementById("email")
const form=document.getElementById("form")
const parrafo=document.getElementById("warnings")

form.addEventListener("submit", (e)=>{
    e.preventDefault()
    let warnigns=""
    let regexEmail=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    let entrar=false
    parrafo.innerHTML=""

    if(username.value.length <6){
        warnigns+=`Nombre de usuario muy corto <br>`
        document.getElementById("user").value = "";
        entrar=true
    }
    if(password.value.length<8){
        warnigns+=`Contraseña muy corta <br>`
        entrar=true
        document.getElementById("pass").value = "";
    }
    if(!regexEmail.test(email.value)){
        warnigns+=`Correo electrónico no valido <br>`
        document.getElementById("email").value = "";
        entrar=true
    }
    
    if(entrar){
        parrafo.innerHTML=warnigns
    }
    
})
document.addEventListener('DOMContentLoaded', ()=>{
    const switcherTheme= document.querySelector('.main__check');
    const root = document.documentElement;
    if(root.getAttribute('data-theme')=='dark'){
        switcherTheme.checked=true;
    }
    switcherTheme.addEventListener('click', toogleTheme);
    function toogleTheme(){
        const setTheme= switcherTheme.checked ? 'dark':'ligth';
        root.setAttribute('data-theme', setTheme);
        localStorage.setItem('theme', setTheme);
        
    }
});