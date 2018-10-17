from flask import Blueprint, render_template, flash
from flask_table import Table, Col

from deviceNanny.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')


class DeviceTable(Table):
    html_attrs = {'class': 'table table-hover'}
    device_id = Col('Device Id')
    device_name = Col('Device Name')
    manufacturer = Col('Manufacture')
    model = Col('Model')
    device_type = Col('Device Type')
    os_version = Col('OS Version')
    checked_out_by = Col('Checked out by')
    location = Col('Office Location')

    def get_tr_attrs(self, item):
        if int(item['id']) % 2 == 0:
            return {'class': 'table-primary'}
        else:
            return {'class': 'table-secondary'}


@bp.route('/')
def home():
    db = get_db()
    rows = db.execute(
        'SELECT id, device_id, device_name, manufacturer, model, device_type, os_version, checked_out_by, location FROM devices'
    ).fetchall()
    table = DeviceTable(rows)

    return render_template('home.html', table=table)
