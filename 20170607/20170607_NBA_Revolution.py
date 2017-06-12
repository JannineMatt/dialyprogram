# coding=UTF-8
"""
round robin nba
- 每支球隊在 29th round 必須與所有隊伍交手過
- 主場或客場不能連續超出 2 場
- 球隊數保持 30 隊
- 每次產生的 schedule 必須不同

refer https://nrich.maths.org/1443
"""
from collections import deque
from random import shuffle

teams = [
    "Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "Los Angeles Clippers",
    "Los Angeles Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizards",
]

# for test
# teams = [1, 2, 3, 4, 5, 6]
shuffle(teams)


def generate_match(teams_list, reverse=False):
    """generate match from current team list [A, B, C, D] => A-D B-C
    """
    half_length = len(teams_list) // 2
    for teamA, teamB in zip(teams_list[:half_length], reversed(teams_list[half_length:])):
        if reverse:
            print('{} vs {}'.format(teamB, teamA))
        else:
            print('{} vs {}'.format(teamA, teamB))


def deque_remove_and_append(queue=None, index=None, position='left'):
    val = queue[index]
    del queue[index]
    if position == 'left':
        queue.appendleft(val)
    else:
        queue.append(val)
    return queue


shift = False
total = len(teams)

if total % 2 != 0:
    raise Exception('team member must maintain even number')

circle_team = deque(teams[:-1])
core_team = deque([teams[-1], ])

for roundn in range(1, total * 2 - 2 + 1):
    shift ^= True
    print('===== round {} ====='.format(roundn))
    circle_team.rotate(1)
    generate_match(list(circle_team + core_team), shift)
