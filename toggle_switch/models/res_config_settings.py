# -*- coding: utf-8 -*-
# Copyright 2020-now Al Hadi Tech - Pakistan
# License OPL-1

import base64
from odoo import models, fields, api, _

class InheritedResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _description = 'Toggle Switch Configurations'

    SCSS_TEMPLATE = """
        div.o_boolean_toggle.custom-control.custom-checkbox {{  
               $line-height-computed: $line-height-base * $font-size-base;
               $slider-width: $line-height-computed * 1.5;
               $circle-width: $line-height-computed * 0.6;
               display: inline-block;
               padding-left: $slider-width + 0.25rem;
               
               > label.custom-control-label {{
                        &::before, &::after {{
                            content: "";
                            top: 0;
                            left: -($slider-width + 0.25rem);
                        }}
                        &::before {{
                            width: $slider-width;
                            height: 100%;
                            background-color:gray !important;
                            border-radius:100px !important;
                            outline: none !important;
                        }}
                        &::after {{
                            transform: translate($line-height-computed * 0.2, $line-height-computed * 0.2);
                            width: ceil($circle-width / 1rem * $o-root-font-size);
                            height: ceil($circle-width / 1rem * $o-root-font-size);
                            border-radius: 100px;
                            background-color: $white;
                            cursor: pointer;
                
                        }}
    }}
    
    > input.custom-control-input:checked + label.custom-control-label {{
                &::before {{
                    background-color:{toggle_color} !important;
                    border-radius:100px !important;
                }}
                &::after {{
                    transform: translate($slider-width - $circle-width - $line-height-computed * 0.2, $line-height-computed * 0.2);
                    background-image: none;
        
                }}
    }}
     
     
     
     }}
     
     
             div.o_boolean_toggle_square.custom-control.custom-checkbox {{  
     
               $line-height-computed: $line-height-base * $font-size-base;
               $slider-width: $line-height-computed * 1.5;
               $circle-width: $line-height-computed * 0.6;
               display: inline-block;
               padding-left: $slider-width + 0.25rem;
               
               
               > label.custom-control-label {{
                        &::before, &::after {{
                            content: "";
                            top: 0;
                            left: -($slider-width + 0.25rem);
                        }}
                        &::before {{
                            width: $slider-width;
                            height: 100%;
                            background-color:gray !important;
                            border-radius:0px !important;
                            outline: none !important;
                        }}
                        &::after {{
                            transform: translate($line-height-computed * 0.2, $line-height-computed * 0.2);
                            width: ceil($circle-width / 1rem * $o-root-font-size);
                            height: ceil($circle-width / 1rem * $o-root-font-size);
                            border-radius:0px !important;
                            background-color: $white;
                            cursor: pointer;
                
                        }}
    }}
    > input.custom-control-input:checked + label.custom-control-label {{
                &::before {{
                    background-color:{toggle_color} !important;
                    border-radius:0px !important;
                }}
                &::after {{
                    transform: translate($slider-width - $circle-width - $line-height-computed * 0.2, $line-height-computed * 0.2);
                    background-image: none;
        
                }}
    }}
     
     
     
     }}
        """

    URL = '/toggle_switch/static/src/scss/base.scss'
    toggle_color = fields.Char(config_parameter='toggle_switch.tog_color')
    toggle_shapes = fields.Selection([('0','Rounded'), ('1', 'Square')],config_parameter='toggle_switch.toggle_shape',required=True)


    @api.model
    def get_values(self):
        res = super(InheritedResConfigSettings, self).get_values()
        res.update(
            toggle_shapes =self.env['ir.config_parameter'].sudo().get_param('toggle_shapes'),
            toggle_color = self.env['ir.config_parameter'].sudo().get_param('toggle_color')
        )
        return res

    def set_values(self):
        super(InheritedResConfigSettings,self).set_values()
        self.env['ir.config_parameter'].sudo().set_param("toggle_shapes",self.toggle_shapes)
        self.env['ir.config_parameter'].sudo().set_param("toggle_color",self.toggle_color or '#7C7BAD')
        self.scss_dynamic_attachment()


    @api.model
    def get_config_value(self,config_name):
        shape_value = self.env['ir.config_parameter'].sudo().get_param(config_name)
        toggle_color = self.env['ir.config_parameter'].get_param("toggle_color")
        classname=''
        if shape_value=='0':
            classname = 'o_boolean_toggle'
        elif shape_value == '1':
            classname='o_boolean_toggle_square'
        vals={
            'className':classname,
            'toggle_color':toggle_color


        }
        return vals

    def scss_dynamic_attachment(self):
        IrAttachmentObjects = self.env['ir.attachment']
        parameters = self.sudo().get_config_value([])
        css_data = self.SCSS_TEMPLATE.format(**parameters)
        datas = base64.b64encode(css_data.encode('utf-8'))
        customized_attachment = IrAttachmentObjects.sudo().search([('url', 'like', self.URL)])
        values = {
            'datas': datas,
            'url': self.URL,
            'name': self.URL,
        }
        if customized_attachment:
            customized_attachment.sudo().write(values)
        else:
            values.update({
                'type': 'binary',
                'mimetype': 'text/scss',
            })
            IrAttachmentObjects.sudo().create(values)
        self.env['ir.qweb'].sudo().clear_caches()
        return self.URL

    def reset_values(self):
        toggle_color = self.env['ir.config_parameter'].sudo().set_param("toggle_color",'#7C7BAD')
        vals={
            'toggle_color':toggle_color
        }
        return vals














