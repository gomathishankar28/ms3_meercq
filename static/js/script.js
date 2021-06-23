/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".dropdown-trigger").dropdown({ hover: true });
    $(".sidenav").sidenav({edge: "right"});
    
    $('.collapsible').collapsible();
    $('select').formSelect();
});