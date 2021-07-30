
/*jshint esversion: 6 */
/*jshint -W117 */
/*
    jQuery for MaterializeCSS initialization
*/
$(document).ready(function () {
    
    $(".dropdown-trigger").dropdown({ hover: true });
    $(".sidenav").sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('select').formSelect();

    // tool tip for all the edit, delete contact and add, delete review buttons.
    
    $('.tooltipped').tooltip();

    // Autocomplete feature for the search bar.

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

      // Validate function for the select elements.

      validateMaterializeSelect();
      function validateMaterializeSelect() {
          let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
          let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
          if ($("select.validate").prop("required")) {
              $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
          }
          $(".select-wrapper input.select-dropdown").on("focusin", function () {
              $(this).parent(".select-wrapper").on("change", function () {
                  if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                      $(this).children("input").css(classValid);
                  }
              });
          }).on("click", function () {
              if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                  $(this).parent(".select-wrapper").children("input").css(classValid);
              } else {
                  $(".select-wrapper input.select-dropdown").on("focusout", function () {
                      if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                          if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                              $(this).parent(".select-wrapper").children("input").css(classInvalid);
                          }
                      }
                  });
              }
          });
      }
});

// For highlighting the active page on Nav menu.

if(window.location.pathname.indexOf("/home") !== -1){
    document.getElementById("home").style.backgroundColor = "rgba(0,0,0,0.1)";
}
if(window.location.pathname.indexOf("/login") !== -1){
    document.getElementById("login").style.backgroundColor = "rgba(0,0,0,0.1)";
}
if(window.location.pathname.indexOf("/register") !== -1){
    document.getElementById("register").style.backgroundColor = "rgba(0,0,0,0.1)";
}

