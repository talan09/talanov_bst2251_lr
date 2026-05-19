    var foldBtns = document.getElementsByClassName("fold-button");
    console.log(foldBtns);
    for (let element of foldBtns) {
        element.addEventListener("click", function (event) {
            console.log('test');
            
            if (element.textContent.trim() == 'Свернуть') {
                element.textContent = 'Развернуть'
                document.querySelector(`.need-to-hide-${element.dataset.hide}`)?.classList.add('hidden')

            }
            else {
                element.textContent = 'Свернуть'
                document.querySelector(`.need-to-hide-${element.dataset.hide}`)?.classList.remove('hidden')
            }
        });
    }
$(document).ready(function () {
    $('.logo').on("mouseenter", function (event) {
        
        $(event.currentTarget).animate({width: '90px' }, 300)
    })
    $('.logo').on("mouseleave", function (event) {
        $(event.currentTarget).animate({width: '70px'}, 300)

    })
});