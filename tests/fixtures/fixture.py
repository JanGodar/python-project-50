import pytest


@pytest.fixture
def result_string_small():
    return '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'


@pytest.fixture
def result_string_big():
    return "{\n    common: {\n      + follow: false\n        setting1: Value 1\n      - setting2: 200\n      - setting3: true\n      + setting3: null\n      + setting4: blah blah\n      + setting5: {\n            key5: value5\n        }\n        setting6: {\n            doge: {\n              - wow: \n              + wow: so much\n            }\n            key: value\n          + ops: vops\n        }\n    }\n    group1: {\n      - baz: bas\n      + baz: bars\n        foo: bar\n      - nest: {\n            key: value\n        }\n      + nest: str\n    }\n  - group2: {\n        abc: 12345\n        deep: {\n            id: 45\n        }\n    }\n  + group3: {\n        deep: {\n            id: {\n                number: 45\n            }\n        }\n        fee: 100500\n    }\n}"


@pytest.fixture
def result_string_plain():
    return """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""


@pytest.fixture
def result_string_json():
    return [{"key": "common", "operation": "nested", "value": [{"key": "follow", "operation": "added", "value": False}, {"key": "setting1", "operation": "same", "value": "Value 1"}, {"key": "setting2", "operation": "removed", "value": 200}, {"key": "setting3", "operation": "change", "value": True, "value_new": None}, {"key": "setting4", "operation": "added", "value": "blah blah"}, {"key": "setting5", "operation": "added", "value": {"key5": "value5"}}, {"key": "setting6", "operation": "nested", "value": [{"key": "doge", "operation": "nested", "value": [{"key": "wow", "operation": "change", "value": "", "value_new": "so much"}]}, {"key": "key", "operation": "same", "value": "value"}, {"key": "ops", "operation": "added", "value": "vops"}]}]}, {"key": "group1", "operation": "nested", "value": [{"key": "baz", "operation": "change", "value": "bas", "value_new": "bars"}, {"key": "foo", "operation": "same", "value": "bar"}, {"key": "nest", "operation": "change", "value": {"key": "value"}, "value_new": "str"}]}, {"key": "group2", "operation": "removed", "value": {"abc": 12345, "deep": {"id": 45}}}, {"key": "group3", "operation": "added", "value": {"deep": {"id": {"number": 45}}, "fee": 100500}}]
