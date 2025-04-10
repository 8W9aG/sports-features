"""A description of player representation in the dataframe."""

from .bet import Bet
from .entity_type import EntityType


class Identifier:
    """A way to identify an entity."""

    # pylint: disable=too-many-arguments,too-many-positional-arguments,too-few-public-methods,too-many-instance-attributes

    def __init__(
        self,
        entity_type: EntityType,
        column: str,
        feature_columns: list[str],
        column_prefix: str,
        points_column: str | None = None,
        team_identifier_column: str | None = None,
        field_goals_column: str | None = None,
        assists_column: str | None = None,
        field_goals_attempted_column: str | None = None,
        offensive_rebounds_column: str | None = None,
        turnovers_column: str | None = None,
        bets: list[Bet] | None = None,
    ):
        self.entity_type = entity_type
        self.column = column
        self.feature_columns = feature_columns
        self.column_prefix = column_prefix
        self.points_column = points_column
        self.team_identifier_column = team_identifier_column
        self.field_goals_column = field_goals_column
        self.assists_column = assists_column
        self.field_goals_attempted_column = field_goals_attempted_column
        self.offensive_rebounds_column = offensive_rebounds_column
        self.turnovers_column = turnovers_column
        self.bets = bets if bets is not None else []

    @property
    def columns(self) -> list[str]:
        """The columns recognised by the identifier."""
        columns = {self.column}
        for feature_column in self.feature_columns:
            columns.add(feature_column)
        if self.points_column is not None:
            columns.add(self.points_column)
        if self.team_identifier_column is not None:
            columns.add(self.team_identifier_column)
        if self.field_goals_column is not None:
            columns.add(self.field_goals_column)
        if self.assists_column is not None:
            columns.add(self.assists_column)
        if self.field_goals_attempted_column is not None:
            columns.add(self.field_goals_attempted_column)
        if self.offensive_rebounds_column is not None:
            columns.add(self.offensive_rebounds_column)
        if self.turnovers_column is not None:
            columns.add(self.turnovers_column)
        return list(columns)
