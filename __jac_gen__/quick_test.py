"""
Quick test of AI Pair Programming Tool
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
    print('=== Quick Custom Test ===')
    _Jac.spawn_call(_Jac.get_root(), ProgrammingAssistant(request_type='analyze', code='function add(a, b) { return a + b; }', language='javascript', session_id='custom_test'))
    _Jac.spawn_call(_Jac.get_root(), ProgrammingAssistant(request_type='debug', code='for i in range(len(my_list)):\n    print(my_list[i+1])', error_message='IndexError: list index out of range', language='python', session_id='debug_test'))