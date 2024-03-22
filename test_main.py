import pytest
import data
import main  


def test_add_asset():
    original_asset_count = len(data.asset_dictionary)
    main.add_asset()
    assert len(data.asset_dictionary) == original_asset_count + 1


def test_add_current_value():
    asset_id = 1  
    original_value = data.asset_dictionary[asset_id]['Current Value']
    main.add_current_value()
    assert data.asset_dictionary[asset_id]['Current Value'] != original_value


def test_add_condition():
    asset_id = 1  
    original_condition = data.asset_dictionary[asset_id]['Condition']
    main.add_condition()
    assert data.asset_dictionary[asset_id]['Condition'] != original_condition


def test_add_department():
    asset_id = 1  
    original_department = data.asset_dictionary[asset_id]['Department']
    main.add_department()
    assert data.asset_dictionary[asset_id]['Department'] != original_department


def test_delete_asset():
    original_asset_count = len(data.asset_dictionary)
    main.delete_asset()
    assert len(data.asset_dictionary) == original_asset_count - 1



