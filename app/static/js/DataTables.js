window.addEventListener('DOMContentLoaded', event => {

    var datatablesSimple = document.querySelector(
        'table[id="DataTable"]');
    if (datatablesSimple) {
        new DataTable(datatablesSimple,{
        "language": {
            "emptyTable": "Não há dados disponíveis na tabela",
            "lengthMenu": "Mostrar _MENU_ registros por página",
            "zeroRecords": "Nenhum registro encontrado",
            "info": "Mostrando _START_ até _END_ de _TOTAL_ registros",
            "infoEmpty": "Mostrando 0 até 0 de 0 registros",
            "infoFiltered": "(filtrado de _MAX_ registros no total)",
            "search": "Buscar:"
        }
    }
        );
    };
});