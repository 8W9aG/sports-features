"""The main process function."""

import datetime

import pandas as pd

from .bets_process import bet_process
from .datetime_process import datetime_process
from .datetimesub_process import datetimesub_process
from .distance_process import distance_process
from .identifier import Identifier
from .margin_process import margin_process
from .offensive_efficiency_process import offensive_efficiency_process
from .remove_process import remove_process
from .skill_process import skill_process
from .timeseries_process import timeseries_process


def process(
    df: pd.DataFrame,
    dt_column: str,
    identifiers: list[Identifier],
    windows: list[datetime.timedelta | None],
) -> pd.DataFrame:
    """Process the dataframe for sports features."""
    df = skill_process(df, dt_column, identifiers, windows)
    df = offensive_efficiency_process(df, identifiers)
    df = margin_process(df, identifiers)
    df = bet_process(df, identifiers, dt_column)
    df = datetimesub_process(df, dt_column, identifiers)
    df = timeseries_process(df, identifiers, windows, dt_column)
    df = datetime_process(df)
    df = distance_process(df, identifiers)
    df = remove_process(df, identifiers)
    return df
