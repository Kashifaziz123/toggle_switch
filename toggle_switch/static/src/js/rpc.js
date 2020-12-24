odoo.define('toggle_switch.rpc', function (require) {
"use strict";


    var rpc = require('web.rpc');
    rpc.query({
                model:'res.config.settings',
                method: 'get_config_value',
                args: ['toggle_switch.toggle_shape'],
            }).then(function (backend_result) {
                 var table = backend_result;
                 localStorage.setItem("ClassName",backend_result['className']);
                 console.log(localStorage.getItem("ClassName"));
            });



});

