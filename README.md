# GameTracker-Python-Api

You can track data through Gametracker.com. It is not official. Developed using request and xpath. You can shoot many data such as online -top players, map, server name, server rank values, statistics image urls ext... with 2 lines of code.

### Example

```
api = GT("95.173.175.56","27015")
print(api.getinfo())
```
As in the gt.py.

### The output is as follows

```
{'name': '[TR] ReqaL. Server |128Tick| !ws !knife !glove', 'status': True, 'map': 'aim_dev_allpistols_v2', 'current_players': '10', 'max_players': '16', 'average_players': '5', 'last_scan_mins': '1', 'last_scan_secs': '23', 'rank': '2454', 'rank_higest': '2328', 'rank_lowest': '2862', 'players': [{'name': '<ツÇ.Sツ>lreqal.xyz', 'frag': '58', 'time': '07:22'}, {'name': 'yaso.exe-hellcase.com-', 'frag': '19', 'time': '13:23'}, {'name': 'Ela', 'frag': '16', 'time': '11:53'}, {'name': 'm0x3r☭│cs.reqal.xyz', 'frag': '14', 'time': '23:21'}, {'name': 'YouAreCheaterToo', 'frag': '12', 'time': '07:22'}, {'name': '𝔅𝔲𝔩𝔩', 'frag': '10', 'time': '13:23'}, {'name': 'SMURFSYDRAPEEK', 'frag': '4', 'time': '29:22'}, {'name': 'IIIIIIIIIIII', 'frag': '0', 'time': '02:54'}, {'name': '♥𝘌│cs.reqal.xyz', 'frag': '0', 'time': '27:51'}, {'name': 'gameOVER', 'frag': '0', 'time': '02:54'}], 'top_players': [], 'img': {'server_map_api': 'https://cache.gametracker.com/images/graphs/server_maps.php?GSID=6108740', 'server_rank_api': 'https://cache.gametracker.com/images/graphs/server_rank.php?GSID=6108740', 'server_players_api_d': 'https://cache.gametracker.com/images/graphs/server_players.php?GSID=6108740&start=-1d', 'server_players_api_w': 'https://cache.gametracker.com/images/graphs/server_players.php?GSID=6108740&start=-1w', 'server_players_api_m': 'https://cache.gametracker.com/images/graphs/server_players.php?GSID=6108740&start=-1m'}}
```

Top players are not getting because they are not activated on this server.

### Keys Meanings

Key | Description | Value Type
------------ | ------------- | -------------
`name` | Name of the server | str
`status` | Status of the server (True or False) | bool
`map` | Current map of the server | str
`current_players` | Current players of the server (number) | str
`max_players` | Maximum players of the server (number) | str
`average_players`  | Maximum players of the server (number) | str
`last_scan_mins` | Latest update minute value (set to 0 if less than 1 minute) | str
`last_scan_secs` | Latest update second value | str
`rank` | Current rank of the server | str
`rank_higest` | Highest value in last month rank of the server | str
`rank_lowest` | Lowest value in last month rank of the server | str
`players` | Current players of the server (with frag and playing time) | dict
`top_players` | Top 10 players of the server (with frag and playing time)  | dict
`img` | Statistics data pictures of the server (with 1 day-week-month) | dict

### Players and Top Players Dict Keys Meanings

Key | Description | Value Type
------------ | ------------- | -------------
`name` | Name of the player| str
`frag` | Frag of the player| str
`time` | Playing time of the player | str

### Img Dict Keys Meanings

Key | Description | Value Type
------------ | ------------- | -------------
`server_map_api` | "FAVORITE MAPS" image URL of the server  | str
`server_rank_api` | "SERVER RANK" image URL of the server  | str
`server_players_api_d` | "PLAYERS" past 1 day image URL of the server | str
`server_players_api_w` | "PLAYERS" past 1 week image URL of the server | str
`server_players_api_m` | "PLAYERS" past 1 month image URL of the server | str