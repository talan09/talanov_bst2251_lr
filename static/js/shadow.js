$(document).ready(function () {
    console.log('test');
    
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