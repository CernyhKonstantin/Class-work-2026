document.addEventListener('DOMContentLoaded',(ev)=>{
    const alertButton = document.getElementById('alertButton')
    if (alertButton) alertButton.addEventListener('click', ()=>{
        alert("Don't click again!")
    })
})