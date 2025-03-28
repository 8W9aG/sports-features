"""Tests for the process function."""
import datetime
import os
import tempfile
import unittest

import pandas as pd

from sportsfeatures.process import process
from sportsfeatures.identifier import Identifier
from sportsfeatures.entity_type import EntityType


class TestProcess(unittest.TestCase):

    def test_process(self):
        current_dir = os.getcwd()
        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                os.chdir(tmpdir)
                team_0_column_prefix = "teams/0"
                team_1_column_prefix = "teams/1"
                dt_column = "dt"
                team_0_id_column = team_0_column_prefix + "/id"
                team_0_kicks = team_0_column_prefix + "/kicks"
                team_0_points_column = team_0_column_prefix + "/points"
                team_0_field_goals_column = team_0_column_prefix + "/field_goals"
                team_0_assists_column = team_0_column_prefix + "/assists"
                team_0_field_goals_attempted_column = team_0_column_prefix + "/field_goals_attempted"
                team_0_offensive_rebounds_column = team_0_column_prefix + "/offensive_rebounds"
                team_0_turnovers_column = team_0_column_prefix + "/turnovers"
                team_1_id_column = team_1_column_prefix + "/id"
                team_1_kicks = team_1_column_prefix + "/kicks"
                team_1_points_column = team_1_column_prefix + "/points"
                team_1_field_goals_column = team_1_column_prefix + "/field_goals"
                team_1_assists_column = team_1_column_prefix + "/assists"
                team_1_field_goals_attempted_column = team_1_column_prefix + "/field_goals_attempted"
                team_1_offensive_rebounds_column = team_1_column_prefix + "/offensive_rebounds"
                team_1_turnovers_column = team_1_column_prefix + "/turnovers"
                df = pd.DataFrame(data={
                    dt_column: [datetime.datetime(2022, 1, 1), datetime.datetime(2022, 1, 2), datetime.datetime(2022, 1, 3)],
                    team_0_id_column: ["0", "1", "0"],
                    team_0_kicks: [10, 20, 30],
                    team_0_points_column: [50, 100, 150],
                    team_0_field_goals_column: [12, 24, 36],
                    team_0_assists_column: [10, 20, 30],
                    team_0_field_goals_attempted_column: [20, 40, 60],
                    team_0_offensive_rebounds_column: [30, 60, 90],
                    team_0_turnovers_column: [10.0, 20.0, 30.0],
                    team_1_id_column: ["1", "0", "1"],
                    team_1_kicks: [20, 40, 60],
                    team_1_points_column: [60, 120, 180],
                    team_1_field_goals_column: [30, 60, 90],
                    team_1_assists_column: [20, 40, 60],
                    team_1_field_goals_attempted_column: [80, 160, 240],
                    team_1_offensive_rebounds_column: [90, 180, 270],
                    team_1_turnovers_column: [10.0, 20.0, 30.0],
                })
                identifiers = [
                    Identifier(
                        EntityType.TEAM,
                        team_0_id_column,
                        [team_0_kicks],
                        team_0_column_prefix,
                        points_column=team_0_points_column,
                        field_goals_column=team_0_field_goals_column,
                        assists_column=team_0_assists_column,
                        field_goals_attempted_column=team_0_field_goals_attempted_column,
                        offensive_rebounds_column=team_0_offensive_rebounds_column,
                        turnovers_column=team_0_turnovers_column,
                    ),
                    Identifier(
                        EntityType.TEAM,
                        team_1_id_column,
                        [team_1_kicks],
                        team_1_column_prefix,
                        points_column=team_1_points_column,
                        field_goals_column=team_1_field_goals_column,
                        assists_column=team_1_assists_column,
                        field_goals_attempted_column=team_1_field_goals_attempted_column,
                        offensive_rebounds_column=team_1_offensive_rebounds_column,
                        turnovers_column=team_1_turnovers_column,
                    ),
                ]
                df = process(df, dt_column, identifiers, [datetime.timedelta(days=365), None])
                print(df)
                print(df.columns.values)
        finally:
            os.chdir(current_dir)
