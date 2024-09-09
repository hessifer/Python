chracter = {
    "entity": {
        "character": {
            "name": "Kaladin",
            "quests": {
                "bridge_run": {
                    "status": "In Progress",
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        }
    }
}

for quest, data in chracter["entity"]["character"]["quests"].items():
    print(f"Quest: {quest}")
    print(f"Status: {data['status']}")
    print()
