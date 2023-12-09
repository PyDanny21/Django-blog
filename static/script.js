document.addEventListener('DOMContentLoaded',()=>{
    const menu= document.querySelector('.menu');
    menu.addEventListener('click',()=>{
        const menuItem=document.querySelector('.menu-items');
        const toggled=menuItem.classList.toggle('menu-height');
        const UL=toggled ? document.querySelector('.menu-items ul').style.display='flex':document.querySelector('.menu-items ul').style.display='none';
        const menuText=toggled ? menu.innerHTML='x':menu.innerHTML='&equiv;';

    });
});