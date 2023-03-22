#!/usr/bin/python3
""" """
import unittest

class TestCreateState(unittest.TestCase):
    
    def test_create_state(self):
        state_name = "California"
        state = create_state(state_name)
        self.assertEqual(state.name, state_name)
        
def create_state(name):
    class State:
        def __init__(self, name):
            self.name = name
    
    return State(name)
    
if __name__ == '__main__':
    unittest.main()
