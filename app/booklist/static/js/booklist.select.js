$(document).ready(function () {
    $('.js-select').select2({
        language: 'ru',
        placeholder: '...',
        allowClear: true,
        width: 'resolve',
    }).change(function(){
        $('.js-form').submit();
    });
});
