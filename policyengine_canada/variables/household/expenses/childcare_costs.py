from policyengine_canada.model_api import *


class childcare_costs(Variable):
    value_type = float
    entity = Person
    label = "Costs for child care"
    unit = CAD
    definition_period = YEAR
