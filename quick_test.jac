"""
Quick test of AI Pair Programming Tool
"""

include:jac ai_pair_programmer;

with entry:__main__ {
    print("=== Quick Custom Test ===");
    
    # Test a JavaScript function analysis
    root spawn ProgrammingAssistant(
        request_type="analyze",
        code="function add(a, b) { return a + b; }",
        language="javascript",
        session_id="custom_test"
    );
    
    # Test a complex debugging scenario
    root spawn ProgrammingAssistant(
        request_type="debug",
        code="for i in range(len(my_list)):\n    print(my_list[i+1])",
        error_message="IndexError: list index out of range",
        language="python",
        session_id="debug_test"
    );
}
