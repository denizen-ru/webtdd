/* global $, window, console */

window.Superlists = {};
window.Superlists.initialize = function() {
    $('input').keypress(function() {
        $('.has-error').hide();
    });
};

window.Superlists.initialize();
