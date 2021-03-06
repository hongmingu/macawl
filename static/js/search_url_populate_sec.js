var search_url_populate_sec = function search_url_populate_sec(id) {
    var con_id = id
    $(function () {
        $.ajax({
            url: '/re/url/populate/', type: 'post', dataType: 'json', cache: false,
            data: {
                url_id: id,
            },
            success: function (data) {
                if (data.res === 1) {
                    var appender = '<div class="div_base">' +
                        '<div align="right">' +
                        '<a href=""><span class="glyphicon glyphicon-option-horizontal url_pop_menu" id="pop_menu_' + id + '"></span></a>' +
                        '</div>' +
                        '<a href="' + data.full_url + '" target="_blank" rel="noopener noreferrer">' +
                        '<div class="url_pop_main_wrapper">' +
                        '<div class="url_pop_title_wrapper"><span class="url_pop_title">' + data.title + '</span></div>' +
                        '<div class="url_pop_url_wrapper"><span class="url_pop_url">' + data.full_url + '</span></div>' +
                        '</div>' +
                        '</a>' +
                        '<a href="/url/' + data.id + '/"><div class="more_load_url clickable">url info</div></a>' +
                        '</div>'
                    $('#url_wrapper_' + id).append(appender)

                    $('#pop_menu_' + id).click(function (e) {
                        e.preventDefault()
                        $('#search_link_source').html('/url/' + id + '/')
                        $('#modal_pop_menu').modal('show')
                    })


                }
            }
        })


    })
}

$(function () {


    $("#modal_pop_menu").on("shown.bs.modal", function () {
        var source = $('#search_link_source').html()
        var scheme = window.location.protocol == "https:" ? "https" : "http";
        var path = scheme + '://' + window.location.host + source;
        $('#modal_pop_menu_input').val(path).select();
    }).on("hidden.bs.modal", function () {
        $('#link_source').html('')
        $('#modal_pop_menu_input').val('')
    });

    $('#modal_pop_menu_copy').click(function (e) {
        e.preventDefault()
        var source = $('#search_link_source').html()
        var scheme = window.location.protocol == "https:" ? "https" : "http";
        var path = scheme + '://' + window.location.host + source;
        $('#modal_pop_menu_input').val(path).select();
        document.execCommand('Copy')
    })
    $('#modal_pop_menu_locate').click(function (e) {
        e.preventDefault()
        var source = $('#search_link_source').html()
        var scheme = window.location.protocol == "https:" ? "https" : "http";
        var path = scheme + '://' + window.location.host + source;
        location.href = path
    })
})
