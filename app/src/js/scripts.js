/*!
    * Start Bootstrap - SB Admin v7.0.7 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2023 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
// 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

var ModalMessage = document.getElementById("ModalMessage");
if (ModalMessage != null) {
    $(document).ready(function () {
        $('#ModalMessage').modal('show');
    });
}

var selector = document.getElementsByTagName("select");
if (selector != null) {
    $(document).ready(function () {
        $('select').select2({
            theme: "bootstrap-5",
            width: $(this).data('width') ? $(this).data('width') : $(this).hasClass('w-100') ? '100%' : 'style',
            placeholder: $(this).data('placeholder'),
        });
    });
}

function formatarComoMoeda(elemento) {
    let valor = elemento.value.replace(/\D/g, '');  // Remove tudo que não é dígito
    valor = (parseInt(valor) / 100).toFixed(2);     // Divide por 100 e fixa duas casas decimais
    valor = valor.replace('.', ',');                // Troca ponto por vírgula

    // Adiciona separadores de milhar
    valor = valor.replace(/\B(?=(\d{3})+(?!\d))/g, '.');

    // Adiciona o símbolo R$
    elemento.value = 'R$ ' + valor;
}


function formatarComoCNPJouCPF(elemento) {
    let valor = elemento.value.replace(/[^a-zA-Z0-9]/g, ''); // Remove tudo que não é dígito ou letra

    // Formatação para CPF (11 dígitos)
    if (valor.length <= 11) {
        valor = valor.replace(/^(\d{3})(\d)/, '$1.$2');
        valor = valor.replace(/^(\d{3})\.(\d{3})(\d)/, '$1.$2.$3');
        valor = valor.replace(/\.(\d{3})(\d)/, '.$1-$2');
    }

    // Formatação para CNPJ (14 dígitos)
    else if (valor.length >= 11) {
        valor = valor.replace(/^(\d{2})(\d)/, '$1.$2');
        valor = valor.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3');
        valor = valor.replace(/\.(\d{3})(\d)/, '.$1/$2');
        valor = valor.replace(/(\d{4})(\d)/, '$1-$2');
    }

    elemento.value = valor;
}

function formatarComoCNPJ(elemento) {
    let valor = elemento.value.replace(/[^a-zA-Z0-9]/g, ''); // Remove tudo que não é dígito ou letra
    // Adiciona os pontos, barra e traço para formatação do CNPJ
    valor = valor.replace(/^(\w{2})(\w)/, '$1.$2');
    valor = valor.replace(/^(\w{2})\.(\w{3})(\w)/, '$1.$2.$3');
    valor = valor.replace(/\.(\w{3})(\w)/, '.$1/$2');
    valor = valor.replace(/(\w{4})(\w)/, '$1-$2');
    elemento.value = valor;
}