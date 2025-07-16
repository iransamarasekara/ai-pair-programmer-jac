"""
Test Examples for AI Pair Programming Tool
Demonstrates various use cases and request types
"""
from __future__ import annotations
from jaclang import jac_import as __jac_import__
from jaclang.plugin.feature import JacFeature as _Jac
from jaclang.plugin.builtin import *
from dataclasses import dataclass as __jac_dataclass__
__jac_import__(target='ai_pair_programmer', base_path=__file__, mod_bundle=__jac_mod_bundle__, lng='jac', absorb=True, mdl_alias=None, items={})
from ai_pair_programmer import *
import ai_pair_programmer
if __name__ == '__main__':
    print('=== Extended Test Examples ===\n')
    print('Test 1: Analyzing a complex sorting function')
    _Jac.spawn_call(_Jac.get_root(), ProgrammingAssistant(request_type='analyze', code='\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n        ', language='python', session_id='test_session_1'))
    print('\n' + '=' * 50 + '\n')
    print('Test 2: Generating a binary search tree implementation')
    _Jac.spawn_call(_Jac.get_root(), ProgrammingAssistant(request_type='generate', requirements='Create a binary search tree class with insert, search, and delete methods', language='python', session_id='test_session_2'))
    print('\n' + '=' * 50 + '\n')
    print('Test 3: Debugging an index error')
    _Jac.spawn_call(_Jac.get_root(), ProgrammingAssistant(request_type='debug', code='\ndef get_last_element(lst):\n    return lst[len(lst)]\n        ', error_message='IndexError: list index out of range', language='python', session_id='test_session_3'))
    print('\n' + '=' * 50 + '\n')
    print('Test 4: Explaining a complex list comprehension')
    _Jac.spawn_call(_Jac.get_root(), ProgrammingAssistant(request_type='explain', code='result = [x**2 for x in range(10) if x % 2 == 0 and x > 2]', language='python', session_id='test_session_4'))
    print('\n' + '=' * 50 + '\n')
    print('Test 5: Analyzing JavaScript async function')
    _Jac.spawn_call(_Jac.get_root(), ProgrammingAssistant(request_type='analyze', code="\nasync function fetchData(url) {\n    try {\n        const response = await fetch(url);\n        const data = await response.json();\n        return data;\n    } catch (error) {\n        console.error('Error fetching data:', error);\n        return null;\n    }\n}\n        ", language='javascript', session_id='test_session_5'))
    print('\n=== All Tests Completed ===')