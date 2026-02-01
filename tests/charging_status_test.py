from weconnect_cupra.api.cupra.elements.charging_status import ChargingStatus
from weconnect_cupra.addressable import AddressableAttribute


def make_mock_vehicle():
    class MockVehicle:
        pass

    vehicle = MockVehicle()
    vehicle.fetcher = None
    vehicle.vin = AddressableAttribute(localAddress='vin', parent=None, value='VINVINVIN', valueType=str)
    return vehicle


def test_charge_power_and_rate_none_disabled():
    """If the incoming dict contains None for chargePower_kW and chargeRate_kmph, the attributes should be disabled."""
    vehicle = make_mock_vehicle()
    cs = ChargingStatus(vehicle=vehicle, parent=None, statusId='chargingStatus', fromDict=None, fixAPI=True)

    data = {
        'value': {
            'chargingState': 'charging',
            'chargeMode': 'manual',
            'remainingChargingTimeToComplete_min': 15,
            'chargePower_kW': None,
            'chargeRate_kmph': None,
        }
    }

    cs.update(data)

    assert cs.chargingState.enabled is True
    assert cs.chargingState.value == ChargingStatus.ChargingState.CHARGING
    assert cs.remainingChargingTimeToComplete_min.value == 15
    assert cs.chargePower_kW.enabled is False
    assert cs.chargeRate_kmph.enabled is False


def test_fixapi_zeroes_power_and_rate_when_state_off():
    """When fixAPI is True and chargingState is OFF but power/rate are non-zero, they should be set to 0.0."""
    vehicle = make_mock_vehicle()
    cs = ChargingStatus(vehicle=vehicle, parent=None, statusId='chargingStatus', fromDict=None, fixAPI=True)

    data = {
        'value': {
            'chargingState': 'off',
            'chargeMode': 'manual',
            'remainingChargingTimeToComplete_min': 0,
            'chargePower_kW': 7.5,
            'chargeRate_kmph': 10.0,
        }
    }

    cs.update(data)

    assert cs.chargingState.value == ChargingStatus.ChargingState.OFF
    # Because of fixAPI and OFF state, values should be zeroed
    assert cs.chargePower_kW.value == 0.0
    assert cs.chargeRate_kmph.value == 0.0
