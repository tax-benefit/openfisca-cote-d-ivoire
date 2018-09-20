# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_cote_d_ivoire.entities import *

class salaire(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaires et Traitements"

