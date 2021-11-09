$(document).ready(function() {
        var table = $('#mydatatable').DataTable({
            lengthChange: false,
            buttons: [{
                extend: 'excel',
                className: 'button_slide slide'
            }, {

                extend: 'pdf',
                className: 'button_slide slide'
            }]
        });

        table.buttons().container()
            .appendTo('#mydatatable_wrapper .col-md-6:eq(0)');

    }

);