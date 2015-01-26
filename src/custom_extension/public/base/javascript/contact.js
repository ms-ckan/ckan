(function($) {
    $(function() {
        var form = $("#form-contact"),
            submit = $('#submit-contact'),
            success = $('#contact-success'),
            danger = $('#contact-danger');
        form.validate({
            rules: {
                name: "required",
                email_address: {
                    required: true,
                    email: true
                },
                phone_number: "required"
            },
            message: {
                name: "Please enter your name.",
                email_address: "Please enter a valid email address.",
                phone_number: "Please enter a valid phone number."
            },
            submitHandler: function(f) {
                submit.attr('disabled', 'disabled');
                $.ajax({
                    url: '/create_contact',
                    type: 'post',
                    data: form.serialize(),
                    success: function(data) {
                        if(data.success) {
                            success.html('<strong>Success!</strong> Please wait for our response.').show();
                        } else {
                            submit.removeAttr('disabled');
                            danger.html('<strong>Error!</strong>' + data.error.message).show();
                        }
                    }
                });
            }
        });
    });
})(jQuery)