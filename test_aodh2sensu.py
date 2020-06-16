import aodh2sensu
# import json


def test_health():
    response = aodh2sensu.app.test_client().get('/health')

    assert response.status_code == 200
    assert response.data == b'200 OK'

# def test_jenkins():
#    mock_request_data = {
#      'alarm_name': 'cpu_hi4',
#        'reason': 'Transition to alarm due to 1 samples outside threshold,
#                   most recent: 35.0979427429',
#        'current': '1'
#    }
#    response = aodh2sensu.app.test_client().post('/',
#                                                 data=json.dumps(mock_request_data))
#    assert response.status_code == 200
#    assert response.data == b'200 OK'
