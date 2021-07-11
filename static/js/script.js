/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".dropdown-trigger").dropdown({ hover: true });
    $(".sidenav").sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.modal').modal();
    $('.tooltipped').tooltip();
    $('input.autocomplete').autocomplete({
        data: {
          "electricians": null,
          "plumbers": null,
          "carpenters": null,
          "painters": null,
          "cleaners": null,
          "gardeners": null,
          "whitegoods": null
        },
      });
});

