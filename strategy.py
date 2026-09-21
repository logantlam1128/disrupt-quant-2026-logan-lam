"""Your submission entry point. Replace the equal-weight baseline below."""


def generate_positions(history, current_date):
    latest = history.loc[history.date == current_date]
    inv_vol = 1 / (latest["realized_vol_20d"] ** 0.5)
    weights = inv_vol / inv_vol.sum()
    return dict(zip(latest["asset_id"], weights))

