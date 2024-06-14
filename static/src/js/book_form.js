odoo.define('library_management.book_form', function (require) {
    'use strict';

    var FormController = require('web.FormController');

    FormController.include({
        _onDeleteButtonClicked: function (ev) {
            var self = this;
            var bookId = self.model.get(self.handle).res_id;

            $.ajax({
                url: `/api/books/${bookId}`,
                type: 'DELETE',
                success: function (result) {
                    alert(result.message);
                    self.do_action('action_library_book');
                },
                error: function (err) {
                    alert(err.responseJSON.detail);
                }
            });
        },

        _onSaveButtonClicked: function (ev) {
            var self = this;
            var bookId = self.model.get(self.handle).res_id;
            var formData = self.renderer.state.data;

            $.ajax({
                url: `/books/${bookId}`,
                type: 'PUT',
                data: formData,
                success: function (result) {
                    alert(result.message);
                    self.do_action('action_library_book');
                },
                error: function (err) {
                    alert(err.responseJSON.detail);
                }
            });
        }
    });
});
