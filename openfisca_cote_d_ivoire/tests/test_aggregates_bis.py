# -*- coding: utf-8 -*-

import pandas as pd

from openfisca_survey_manager.aggregates import AbstractAggregates


class CoteDIvoireAggregates(AbstractAggregates):
    aggregate_variables = ['impot_general_revenu']
    amount_unit = 1e9
    currency = "F CFA"
    beneficiaries_unit = 1e3

    def load_actual_data(self, year = None):
        from openfisca_cote_d_ivoire.tests.test_aggregates import read_aggregates
        recette_by_variable = read_aggregates()
        amounts = pd.Series(recette_by_variable)
        print(amounts)
        return pd.DataFrame(data = {
            "actual_amount": amounts,
            # "actual_beneficiaries": beneficiaries[str(year)],
            })


if __name__ == '__main__':
    from openfisca_cote_d_ivoire.tests.test_aggregates import create_survey_sceanrio
    survey_scenario = create_survey_sceanrio()
    aggregates = CoteDIvoireAggregates(survey_scenario)
    df = aggregates.load_actual_data()
    print(df)

    df = aggregates.compute_aggregates(use_baseline = False, actual = True)
    print(df.transpose())
    df.to_csv('aggregates.csv')