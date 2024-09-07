window.addEventListener('DOMContentLoaded', event => {

    var datatablesSimple = document.querySelector(
        'table[id="DataTable"]');
    if (datatablesSimple) {
        new DataTable(datatablesSimple);
    };
});