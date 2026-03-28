var foldBtns = document.getElementsByClassName("fold-button");
console.log(foldBtns);
for (let element of foldBtns) {
    element.addEventListener("click", function (event) {
        console.log(document.querySelector(`.need-to-hide-${element.dataset.hide}`))
        if (element.textContent.trim()  == 'Свернуть') {
            element.textContent  = 'Развернуть'
            document.querySelector(`.need-to-hide-${element.dataset.hide}`).classList.add('hidden')

        }
        else{
            element.textContent  = 'Свернуть'
            document.querySelector(`.need-to-hide-${element.dataset.hide}`).classList.remove('hidden')
        }
    });
}

$(document).ready(function () {
    $('.one-post').on("mouseenter", function (event) {

        $(event.currentTarget).find('.one-post-shadow').animate({
            opacity:
                '0.1'
        }, 300);
    })
    $('.one-post').on("mouseleave", function (event) {
        $(event.currentTarget).find('.one-post-shadow').animate({ opacity: '0' },
            300);
    })
});

$(document).ready(function () {
    $('.logo').on("mouseenter", function (event) {

        $(event.currentTarget).animate({width: '90px' }, 300)
    })
    $('.logo').on("mouseleave", function (event) {
        $(event.currentTarget).animate({width: '70px'}, 300)

    })
});

$(document).ready(function () {
    var yPosition;
    var scrolled = 0;
    var parallaxElements = $('.icons-for-parallax img');
    console.log(parallaxElements);

    $(window).scroll(function () {
        scrolled = $(window).scrollTop();
        for (var i = 0; i < parallaxElements.length; i++) {
            yPosition = (scrolled * 0.15 * (i + 1));
            parallaxElements.eq(i).css({ top: yPosition });
        }
    });
});