"""Replace this equal-weight example with your research strategy.

The function is called once per execution day with history through the previous
close. Returning {} means cash. Missing assets receive zero target weight.
"""


def generate_positions(history, current_date):
    latest = history.loc[history.date == current_date]
    inv_vol = 1 / latest["realized_vol_20d"]
    weights = inv_vol / inv_vol.sum()
    return dict(zip(latest["asset_id"], weights))

