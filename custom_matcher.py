from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod

class ReturnVENI(BaseMatcher):
    def _matches(self, val):
        return val == 'VENI'
    def describe_to(self, description):
        description.append("Wrong val")

def eq_to_VENI():
    return ReturnVENI()  
