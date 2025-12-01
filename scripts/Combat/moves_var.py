import random

moves = {
    "General_Moves": {
        "Punch": {
            "Description": "A basic punch.",
            "Damage": 5,
            "Recoil": 0,
            "Acurracy": 95,
            "Type": "Attack"
        },
        "Kick": {
            "Description": "A basic kick.",
            "Damage": 5,
            "Recoil": 0,
            "Acurracy": 95,
            "Type": "Attack"
        },
        "Bite": {
            "Description": "A bite with a bit of recoil.",
            "Damage": 7,
            "Recoil": 1,
            "Acurracy": 95,
            "Type": "Attack"
        }
    },
    "Warrior": {
        "Slash": {
            "Description": "A clean sword swing.",
            "Damage": 10,
            "Accuracy": 90,
            "Type": "Physical",
            "Recoil": 0
        },
        "Rage Strike": {
            "Description": "A strong hit with low accuracy.",
            "Damage": 18,
            "Accuracy": 65,
            "Type": "Physical",
            "Recoil": 0
        },
        "Guard Break": {
            "Description": "Weak hit that lowers defense.",
            "Damage": 8,
            "Accuracy": 85,
            "Type": "Physical",
            "Recoil": 0
        },
        "Parry": {
            "Description": "Block the next attack.",
            "Damage": 0,
            "Accuracy": 100,
            "Type": "Buff",
            "Recoil": 0
        },
        "Whirlwind": {
            "Description": "Spin attack that hits hard.",
            "Damage": 16,
            "Accuracy": 80,
            "Type": "Physical",
            "Recoil": 0
        }
    },

    "Mage": {
        "Firebolt": {
            "Description": "A small fire spell.",
            "Damage": 12,
            "Accuracy": 90,
            "Type": "Magic",
            "Recoil": 0
        },
        "Ice Shard": {
            "Description": "Weak hit that slows the enemy.",
            "Damage": 8,
            "Accuracy": 95,
            "Type": "Magic",
            "Recoil": 0
        },
        "Arcane Burst": {
            "Description": "Big magic blast.",
            "Damage": 20,
            "Accuracy": 80,
            "Type": "Magic",
            "Recoil": 0
        },
        "Mana Shield": {
            "Description": "Block damage using mana.",
            "Damage": 0,
            "Accuracy": 100,
            "Type": "Buff",
            "Recoil": 0
        },
        "Thunder Spike": {
            "Description": "Strong lightning hit.",
            "Damage": 18,
            "Accuracy": 85,
            "Type": "Magic",
            "Recoil": 0
        }
    },

    "Archer": {
        "Quick Shot": {
            "Description": "Low-power shot.",
            "Damage": 9,
            "Accuracy": 95,
            "Type": "Physical",
            "Recoil": 0
        },
        "Power Arrow": {
            "Description": "Heavy arrow.",
            "Damage": 17,
            "Accuracy": 75,
            "Type": "Physical",
            "Recoil": 0
        },
        "Piercing Arrow": {
            "Description": "Ignores some defense.",
            "Damage": 12,
            "Accuracy": 85,
            "Type": "Physical",
            "Recoil": 0
        },
        "Volley": {
            "Description": "Shoot many arrows.",
            "Damage": 15,
            "Accuracy": 70,
            "Type": "Physical",
            "Recoil": 0
        },
        "Eagle Eye": {
            "Description": "Boost critical chance.",
            "Damage": 0,
            "Accuracy": 100,
            "Type": "Buff",
            "Recoil": 0
        }
    },

    "Tank": {
        "Shield Bash": {
            "Description": "Low damage, may stun.",
            "Damage": 8,
            "Accuracy": 90,
            "Type": "Physical",
            "Recoil": 0
        },
        "Fortify": {
            "Description": "Raise defense.",
            "Damage": 0,
            "Accuracy": 100,
            "Type": "Buff",
            "Recoil": 0
        },
        "Taunt": {
            "Description": "Force enemy to use atacking moves.",
            "Damage": 0,
            "Accuracy": 100,
            "Type": "Debuff",
            "Recoil": 0
        },
        "Bulwark": {
            "Description": "Reduce damage taken next hit.",
            "Damage": 0,
            "Accuracy": 100,
            "Type": "Buff",
            "Recoil": 0
        },
        "Body Slam": {
            "Description": "Heavy physical hit with some recoil.",
            "Damage": 14,
            "Accuracy": 85,
            "Type": "Physical",
            "Recoil": 6
        }
    },

    "Shaman": {
        "Heal Pulse": {
            "Description": "Small heal.",
            "Damage": 0,
            "Accuracy": 100,
            "Type": "Heal",
            "Recoil": 0
        },
        "Lightning Jolt": {
            "Description": "Medium shock hit.",
            "Damage": 12,
            "Accuracy": 90,
            "Type": "Magic",
            "Recoil": 0
        },
        "Spirit Ward": {
            "Description": "Lower enemy attack.",
            "Damage": 0,
            "Accuracy": 95,
            "Type": "Debuff",
            "Recoil": 0
        },
        "Earthbind": {
            "Description": "Reduce enemy speed.",
            "Damage": 0,
            "Accuracy": 95,
            "Type": "Debuff",
            "Recoil": 0
        },
        "Nature Spike": {
            "Description": "Big earth spell.",
            "Damage": 16,
            "Accuracy": 85,
            "Type": "Magic",
            "Recoil": 0
        }
    },

    "Summoner": {
        "Call Imp": {
            "Description": "Summon a small Imp.",
            "Damage": 6,
            "Accuracy": 100,
            "Type": "Summon",
            "Recoil": 0
        },
        "Call Golem": {
            "Description": "Summon a strong Golem.",
            "Damage": 14,
            "Accuracy": 100,
            "Type": "Summon",
            "Recoil": 0
        },
        "Sacrifice Minion": {
            "Description": "Destroy a summon for big hit.",
            "Damage": 18,
            "Accuracy": 90,
            "Type": "Magic",
            "Recoil": 0
        },
        "Overseer": {
            "Description": "Buff all summons.",
            "Damage": 0,
            "Accuracy": 100,
            "Type": "Buff",
            "Recoil": 0
        },
        "Spirit Beam": {
            "Description": "Strong magic shot.",
            "Damage": 15,
            "Accuracy": 85,
            "Type": "Magic",
            "Recoil": 0
        }
    },

    "Wildcard": {
        "Chaos Strike": {
            "Description": "Random damage.",
            "Damage": random.randint(0, 15),
            "Accuracy": 80,
            "Type": "Chaos",
            "Recoil": 0
        },
        "Flip": {
            "Description": "Swap attack and defense.",
            "Damage": 0,
            "Accuracy": 100,
            "Type": "Buff",
            "Recoil": 0
        },
        "Shock Gamble": {
            "Description": "Hits you or your oponent.",
            "Damage": 15,
            "Accuracy": 75,
            "Type": "Chaos",
            "Recoil": 0
        },
        "Wild Surge": {
            "Description": "Random buff or debuff.",
            "Damage": 0,
            "Accuracy": 100,
            "Type": "Chaos",
            "Recoil": 0
        },
        "Unstable Burst": {
            "Description": "Either insta kills the enemy or do very high damge to yourseld.",
            "Damage": 99999999999,
            "Accuracy": 90,
            "Type": "Chaos",
            "Recoil": 0
        }
    }
}
