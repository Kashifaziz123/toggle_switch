odoo.define('toggling.basic_fields', function (require) {
"use strict";

    var basic_fields = require('web.basic_fields');
    var field_registry = require('web.field_registry');
    var AbstractField = require('web.AbstractField');
    var rpc = require('web.rpc');

    var FieldBoolean = AbstractField.extend({
    className:'o_boolean_toggle',
    events: _.extend({}, AbstractField.prototype.events, {
        'click': '_onClick'
    }),
    supportedFieldTypes: ['boolean'],



    activate: function (options) {
        var activated = this._super.apply(this, arguments);
        if (activated && options && options.event && $(options.event.target).closest('.custom-control.custom-checkbox').length) {
            this._setValue(!this.value);  // Toggle the checkbox
        }
        return activated;
    },
    getFocusableElement: function () {
        return this.$input || $();
    },

    isSet: function () {
        return true;
    },
    reset: function (record, event) {
        var rendered = this._super.apply(this, arguments);
        if (event && event.target.name === this.name) {
            this.activate();
        }
        return rendered;
    },

    setIDForLabel: function (id) {
        this._super.apply(this, arguments);
        this.$('.custom-control-label').attr('for', id);
    },

    _render: function () {
        var s = localStorage.getItem("ClassName");
        var $checkbox = this._formatValue(this.value);
        var self = this.$el
        this.$input = $checkbox.find('input');
        this.$input.prop('disabled', this.mode === 'readonly');
        this.$el.addClass($checkbox.attr('class'));
        this.$el.empty().append($checkbox.contents());
        console.log('>>',s)
        self.addClass(s);






    },

    _onChange: function () {
        this._setValue(this.$input[0].checked);

    },
    _onKeydown: function (ev) {
        switch (ev.which) {
            case $.ui.keyCode.ENTER:
                this.$input.prop('checked', !this.value);
                this._setValue(!this.value);
                return;
            case $.ui.keyCode.UP:
            case $.ui.keyCode.RIGHT:
            case $.ui.keyCode.DOWN:
            case $.ui.keyCode.LEFT:
                ev.preventDefault();
        }
        this._super.apply(this, arguments);
    },

    _onClick: function (event) {
        event.stopPropagation();
        this._setValue(!this.value);
        this.$el.closest(".o_data_row").toggleClass('text-muted', this.value);
    },

    });

field_registry.add('boolean',FieldBoolean);

});

