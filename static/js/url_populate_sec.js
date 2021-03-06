$(function () {
    $.ajax({
        url: '/re/url/object/', type: 'post', dataType: 'json', cache: false,
        data: {
            url_id: $('#id').html(),
            end_id: $('#end_id').html()
        },
        success: function (data) {
            if (data.res === 1) {
                //user set
                if (data.output.length === 0) {
                    $('#content_result').append('<div class="h4">end results</div>')

                } else {
                    $.each(data.output, function (key, value) {
                        var appender = '<div class="row div_base" id="suobj_wrapper_' + value.id + '">' +
                            '<script defer>' +
                            '    suobj_populate_url("' + value.id + '")' +
                            '<' + '/script>' +
                            '</div>'
                        $('#content_result').append(appender)

                    })
                }

                if (data.end === null) {
                    $('#more_load').addClass('hidden')
                    $('#end_id').html('')
                } else {
                    $('#more_load').removeClass('hidden')
                    $('#end_id').html(data.end)
                }
            }
        }
    })


    $('#more_load').on('click', function (e) {
        e.preventDefault()
        $.ajax({
            url: '/re/url/object/', type: 'post', dataType: 'json', cache: false,
            data: {
                url_id: $('#id').html(),
                end_id: $('#end_id').html()
            },
            success: function (data) {
                if (data.res === 1) {
                    //user set
                    if (data.output.length === 0) {
                        $('#content_result').append('<div class="h4">end results</div>')

                    } else {
                        $.each(data.output, function (key, value) {
                            var appender = '<div class="row div_base" id="suobj_wrapper_' + value.id + '">' +
                                '<script defer>' +
                                '    suobj_populate_url("' + value.id + '")' +
                                '<' + '/script>' +
                                '</div>'
                            $('#content_result').append(appender)


                        })
                    }


                    if (data.end === null) {
                        $('#more_load').addClass('hidden')
                        $('#end_id').html('')
                    } else {
                        $('#more_load').removeClass('hidden')
                        $('#end_id').html(data.end)
                    }
                }


            }
        })
    })
})

$(function () {
    $('#pop_menu_url').click(function (e) {
        e.preventDefault()
        $('#modal_pop_menu_url').modal('show')
    })

    $("#modal_pop_menu_url").on("shown.bs.modal", function () {
        var source = $('#link_source').html()
        var scheme = window.location.protocol == "https:" ? "https" : "http";
        var path = scheme + '://' + window.location.host + source;
        $('#modal_pop_menu_input_url').val(path).select();
    }).on("hidden.bs.modal", function () {
        $('#modal_pop_menu_input_url').val('')
    });

    $('#modal_pop_menu_copy_url').click(function (e) {
        e.preventDefault()
        var source = $('#link_source').html()
        var scheme = window.location.protocol == "https:" ? "https" : "http";
        var path = scheme + '://' + window.location.host + source;
        $('#modal_pop_menu_input_url').val(path).select();
        document.execCommand('Copy')
    })
    $('#modal_pop_menu_locate_url').click(function (e) {
        e.preventDefault()
        var source = $('#link_source').html()
        var scheme = window.location.protocol == "https:" ? "https" : "http";
        var path = scheme + '://' + window.location.host + source;
        location.href = path
    })
})
