from LoanStake import LoanStake
import pytest

class TestStake:
    def test_stake(self):
        new_stake = LoanStake("BUSINESS", 0, 1, 'EMPLOYEE')
        stake_val = new_stake.calculate_stake()
        print(stake_val)
        assert True