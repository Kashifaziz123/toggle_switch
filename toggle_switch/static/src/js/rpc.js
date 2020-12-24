odoo.define('toggling.rpc', function (require) {
"use strict";


    var rpc = require('web.rpc');
    rpc.query({
                model:'res.config.settings',
                method: 'get_config_value',
                args: ['toggling.tog_shape'],
            }).then(function (backend_result) {
                 var table = backend_result;
                 localStorage.setItem("ClassName",backend_result['className']);
                 console.log(localStorage.getItem("ClassName"));
            });



});

