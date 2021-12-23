from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod

class ReturnTrue(BaseMatcher):
    def __init__(self, value):
        self.value = True #wartosc prawda lub falsz
    def _matches(self, newVal):
        if not hasmethod(newVal, 'value'):
            return False
        return newVal == self.value
    def describe_to(self, description):
        description.append_text('Received value: ')    \
                   .append_text(self.value).append_text(' ,type: ').append_text(type(self.value))

def eq_to_True():
    return ReturnTrue(True)  

