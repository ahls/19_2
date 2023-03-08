var storyDropDownButton = document.querySelector('#dropdownButton')
var storyDropDownMenu = document.querySelector('#storyDropDown')
storyDropDownButton.addEventListener('click',(e)=>
{
    e.preventDefault();
    console.log("button clicked")
    console.log(storyDropDownMenu)
    storyDropDownMenu.classList.toggle('show')
})

console.log("done")