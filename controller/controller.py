
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class MpesaController(http.Controller):

    @http.route('/pay/callback', type='json', auth='public', csrf=False)
    def mpesa_stk_callback(self, **post):
        data = request.jsonrequest
        #response message
        if data.get('Body', {}).get('stkCallback', {}).get('ResultCode') == 0:
            request.env['mpesa.stk.push'].sudo().payment_success(data)
            return {'status': 'success'}
        else:
            return {'status': 'failed'}
    _logger.info('+++++++++++++++++ mpesa_stk_callback called ++++++++++++')
