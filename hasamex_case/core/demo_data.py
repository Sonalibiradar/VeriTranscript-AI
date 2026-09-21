"""
Pre-computed, fully grounded demo responses for the 3 case transcripts.
Used when running in Demo/Offline mode or when an Anthropic API key is not yet configured.
Every quote is an exact verbatim quote matching the source transcript files.
"""

DEMO_GUIDE_ANSWERS = {
    # Question 1: How would you describe current adoption of robotic surgery in your market?
    (1, "Transcript_1_France"): {
        "covered": True,
        "answer": "Adoption in France is growing steadily but remains heavily concentrated in large academic hospitals and private centers with capital resources, while regional hospitals lag.",
        "quotes": [
            {
                "text": "Adoption is growing, but it is still concentrated in larger academic hospitals and private centres with stronger capital budgets. Smaller regional hospitals are much slower.",
                "timestamp": "00:18",
            }
        ],
    },
    (1, "Transcript_2_Germany"): {
        "covered": True,
        "answer": "Adoption in Germany is expanding but uneven across regions; large university medical centers are significantly advanced while smaller facilities remain hesitant.",
        "quotes": [
            {
                "text": "It is growing, but adoption is quite uneven. Large university hospitals are much more advanced, while many smaller hospitals are still waiting.",
                "timestamp": "00:16",
            }
        ],
    },
    (1, "Transcript_3_UK"): {
        "covered": True,
        "answer": "In the UK, adoption is increasing and robotic surgery is becoming standard for selected procedures in major NHS trusts, though access varies widely across hospitals.",
        "quotes": [
            {
                "text": "Adoption is increasing, and in some larger NHS trusts robotic surgery is becoming standard for selected procedures. But access still varies significantly by hospital.",
                "timestamp": "00:14",
            }
        ],
    },

    # Question 2: What are the main barriers to adoption?
    (2, "Transcript_1_France"): {
        "covered": True,
        "answer": "Capital budget approval is the primary hurdle in France; clinical endorsement is insufficient without a rigorously validated economic case.",
        "quotes": [
            {
                "text": "The biggest issue is still capital budget approval. Hospitals may like the technology clinically, but purchasing committees need a strong economic case before approving a system.",
                "timestamp": "01:20",
            }
        ],
    },
    (2, "Transcript_2_Germany"): {
        "covered": True,
        "answer": "Upfront capital costs and strained hospital finances are the leading barriers, followed by the challenge of proving that case volume will justify the purchase.",
        "quotes": [
            {
                "text": "Cost is the first barrier. These are large capital purchases, and hospital finances are under pressure. The second issue is proving that the system will be used enough.",
                "timestamp": "01:10",
            }
        ],
    },
    (2, "Transcript_3_UK"): {
        "covered": True,
        "answer": "While funding is a significant constraint, training capacity for surgical teams and theatre staff is equally critical in preventing adoption from stalling.",
        "quotes": [
            {
                "text": "Funding is important, but I would say training capacity is just as important. You can buy a system, but if you cannot train enough surgeons and theatre staff, adoption stalls.",
                "timestamp": "01:05",
            }
        ],
    },

    # Question 3: How important are hospital budgets and ROI in purchasing decisions?
    (3, "Transcript_1_France"): {
        "covered": True,
        "answer": "ROI is paramount in France; hospital finance committees strictly analyze procedure volume, utilization metrics, and ongoing maintenance before greenlighting a purchase.",
        "quotes": [
            {
                "text": "Very important. The clinical argument may get surgeons interested, but the finance team wants to understand utilisation, procedure volume, maintenance cost and whether the system will actually pay for itself.",
                "timestamp": "02:18",
            }
        ],
    },
    (3, "Transcript_2_Germany"): {
        "covered": True,
        "answer": "Economic considerations and total cost of ownership decide whether a system gets approved, including procedure volumes and recurring service contracts.",
        "quotes": [
            {
                "text": "We look at total cost of ownership, expected procedure volume, maintenance, service contracts and training requirements. A strong clinical case helps, but the economic case decides whether it gets approved.",
                "timestamp": "02:08",
            }
        ],
    },
    (3, "Transcript_3_UK"): {
        "covered": True,
        "answer": "Financial ROI matters in the UK, but NHS trusts balance economics with broader clinical strategy, patient length of stay, and surgeon recruitment.",
        "quotes": [
            {
                "text": "It matters, but the discussion is not always purely financial. Hospitals also consider patient outcomes, length of stay, surgeon recruitment and whether the technology improves their clinical position.",
                "timestamp": "02:07",
            }
        ],
    },

    # Question 4: How important are surgeon training and clinical outcomes?
    (4, "Transcript_1_France"): {
        "covered": True,
        "answer": "Training multiple surgeons is critical during the first year to ensure high utilization; clinical outcomes are a necessary prerequisite but cannot sell the system alone.",
        "quotes": [
            {
                "text": "Training matters, especially in the first year. If only one surgeon can use the system, the economics become difficult. Hospitals want several surgeons trained so utilisation is high enough.",
                "timestamp": "03:10",
            },
            {
                "text": "Clinical outcomes are necessary, but they are not enough on their own. If two systems offer similar outcomes, the hospital will look hard at economics and utilisation.",
                "timestamp": "04:08",
            }
        ],
    },
    (4, "Transcript_2_Germany"): {
        "covered": True,
        "answer": "Surgeon training is operationally vital; if only one surgeon uses the platform, low utilization weakens the entire financial business case.",
        "quotes": [
            {
                "text": "Very important operationally. If the hospital buys a system but only one surgeon is comfortable using it, utilisation will be poor. That weakens the business case.",
                "timestamp": "03:05",
            }
        ],
    },
    (4, "Transcript_3_UK"): {
        "covered": True,
        "answer": "Sustainable adoption requires both adequate trained personnel and sufficient caseload; clinical outcomes and surgeon recruitment are central to the overall program.",
        "quotes": [
            {
                "text": "The key point is that adoption is not just about buying the machine. Hospitals need enough trained people and enough procedure volume to make the programme sustainable.",
                "timestamp": "06:04",
            }
        ],
    },

    # Question 5: What adoption trend do you expect over the next 3–5 years?
    (5, "Transcript_1_France"): {
        "covered": True,
        "answer": "Expects steady procedure growth of 15% to 20% annually in high-volume centres, while regional facilities will continue to move slowly.",
        "quotes": [
            {
                "text": "I expect adoption to continue increasing, probably steadily rather than explosively. I would expect maybe 15 to 20 percent more procedures annually in some of the stronger centres, but smaller hospitals will remain slower.",
                "timestamp": "05:07",
            }
        ],
    },
    (5, "Transcript_2_Germany"): {
        "covered": True,
        "answer": "Projects modest, gradual growth in the high single digits or low double digits, as competing capital priorities restrain explosive market-wide expansion.",
        "quotes": [
            {
                "text": "I would expect continued growth, but probably closer to high single digits or low double digits in procedure volumes rather than something like 20 percent across the whole market.",
                "timestamp": "05:08",
            }
        ],
    },
    (5, "Transcript_3_UK"): {
        "covered": True,
        "answer": "Optimistic about acceleration exceeding 15% annual procedure growth in select areas, especially if training access broadens and pricing becomes more competitive.",
        "quotes": [
            {
                "text": "I am quite positive. I think adoption could accelerate if training expands and systems become more cost competitive. I could see procedure growth above 15 percent annually in some areas.",
                "timestamp": "04:06",
            }
        ],
    },

    # Question 6: What is the typical hospital decision-making timeline for purchasing a new robotic system?
    (6, "Transcript_1_France"): {
        "covered": True,
        "answer": "Realistic procurement timeline is 6 to 12 months once serious interest is established, extending further if deferred to the subsequent budget cycle.",
        "quotes": [
            {
                "text": "Six to twelve months is realistic once the hospital becomes serious. It can be longer if the capital committee pushes the purchase into the next budget cycle.",
                "timestamp": "06:08",
            }
        ],
    },
    (6, "Transcript_2_Germany"): {
        "covered": True,
        "answer": "A timeline of 9 to 18 months is common in Germany due to extensive multi-stakeholder consensus required across administration, finance, and surgery.",
        "quotes": [
            {
                "text": "Nine to eighteen months is common. Procurement, clinical leadership, finance and management all need to align, so it can move slowly.",
                "timestamp": "06:05",
            }
        ],
    },
    (6, "Transcript_3_UK"): {
        "covered": True,
        "answer": "Procurement takes 6 to 9 months if capital is already allocated, but can stretch significantly longer if waiting for NHS capital funding cycles.",
        "quotes": [
            {
                "text": "Around six to nine months can happen if funding is already available. If the trust has to wait for a new capital cycle, it can take much longer.",
                "timestamp": "05:04",
            }
        ],
    },
}


DEMO_THEMES = {
    1: {
        "common_themes": [
            {
                "theme": "Adoption is growing across all markets but remains heavily skewed toward large academic/teaching hospitals and private facilities.",
                "supporting_experts": ["Dr. Jean Martin", "Anna Keller", "Dr. Emily Carter"],
            },
            {
                "theme": "Smaller regional or district hospitals face significant access barriers and lag behind in robotic implementation.",
                "supporting_experts": ["Dr. Jean Martin", "Anna Keller", "Dr. Emily Carter"],
            },
        ],
        "disagreements": [],
    },
    2: {
        "common_themes": [
            {
                "theme": "Upfront capital costs and institutional budget constraints are major universal barriers across European healthcare systems.",
                "supporting_experts": ["Dr. Jean Martin", "Anna Keller", "Dr. Emily Carter"],
            },
            {
                "theme": "Surgeon and theatre staff training availability represents a major operational bottleneck.",
                "supporting_experts": ["Dr. Jean Martin", "Anna Keller", "Dr. Emily Carter"],
            },
        ],
        "disagreements": [
            {
                "topic": "Primary hurdle: Capital approval vs Training capacity",
                "positions": [
                    {"expert": "Dr. Jean Martin", "position": "Capital budget approval is the primary hurdle; clinical interest is secondary to the financial case."},
                    {"expert": "Anna Keller", "position": "Large capital expense and proving adequate utilization are the top dual barriers."},
                    {"expert": "Dr. Emily Carter", "position": "Argues training capacity is just as important as capital funding in preventing adoption stalls."},
                ],
            }
        ],
    },
    3: {
        "common_themes": [
            {
                "theme": "Financial viability, procedural volume, and total cost of ownership are critical metrics for purchasing sign-off.",
                "supporting_experts": ["Dr. Jean Martin", "Anna Keller", "Dr. Emily Carter"],
            }
        ],
        "disagreements": [
            {
                "topic": "Pure ROI vs Holistic Strategic Impact",
                "positions": [
                    {"expert": "Dr. Jean Martin", "position": "Finance teams demand that the system directly pays for itself through utilization and procedure volume."},
                    {"expert": "Anna Keller", "position": "Strict economic case decides approval based on total cost of ownership and service contracts."},
                    {"expert": "Dr. Emily Carter", "position": "ROI is balanced against patient outcomes, hospital length of stay, and surgeon recruitment rather than finance alone."},
                ],
            }
        ],
    },
    4: {
        "common_themes": [
            {
                "theme": "Multi-surgeon training is essential; relying on a single trained surgeon threatens case volume and destroys the economic model.",
                "supporting_experts": ["Dr. Jean Martin", "Anna Keller", "Dr. Emily Carter"],
            },
            {
                "theme": "Clinical outcomes are necessary baseline requirements, but they are not sufficient on their own without high utilization.",
                "supporting_experts": ["Dr. Jean Martin", "Anna Keller"],
            },
        ],
        "disagreements": [],
    },
    5: {
        "common_themes": [
            {
                "theme": "Positive overall growth trajectory expected over the next 3-5 years without an abrupt overnight disruption.",
                "supporting_experts": ["Dr. Jean Martin", "Anna Keller", "Dr. Emily Carter"],
            }
        ],
        "disagreements": [
            {
                "topic": "Growth rate expectations (Modest vs Strong)",
                "positions": [
                    {"expert": "Anna Keller", "position": "Expects high single-digit or low double-digit growth due to competing hospital capital priorities."},
                    {"expert": "Dr. Jean Martin", "position": "Projects 15% to 20% annual procedure expansion in leading French medical centers."},
                    {"expert": "Dr. Emily Carter", "position": "Anticipates growth exceeding 15% annually if system prices drop and training ramps up."},
                ],
            }
        ],
    },
    6: {
        "common_themes": [
            {
                "theme": "Purchasing cycles are substantially elongated if the proposal misses the hospital's annual capital budget allocation.",
                "supporting_experts": ["Dr. Jean Martin", "Anna Keller", "Dr. Emily Carter"],
            }
        ],
        "disagreements": [
            {
                "topic": "Expected decision timeline",
                "positions": [
                    {"expert": "Dr. Jean Martin", "position": "6 to 12 months once the hospital is serious."},
                    {"expert": "Anna Keller", "position": "9 to 18 months due to alignment needed across procurement, clinicians, and administration."},
                    {"expert": "Dr. Emily Carter", "position": "6 to 9 months if funds are available; longer if dependent on fresh NHS capital cycles."},
                ],
            }
        ],
    },
}


def get_demo_freeform_answer(question: str) -> dict:
    q = question.lower()
    if any(k in q for k in ["roi", "budget", "finance", "cost", "economic"]):
        return {
            "covered": True,
            "answer": "Experts across France and Germany emphasize that hospital budgets and ROI are decisive gatekeepers: in France, finance teams demand proof that procedure volumes will cover maintenance and capital costs, while in Germany, total cost of ownership and service contracts dictate approval. In contrast, the UK expert notes that while ROI matters, NHS decisions balance financial return against clinical strategy, patient length of stay, and surgeon recruitment.",
            "quotes": [
                {
                    "text": "The clinical argument may get surgeons interested, but the finance team wants to understand utilisation, procedure volume, maintenance cost and whether the system will actually pay for itself.",
                    "timestamp": "02:18",
                    "expert": "Dr. Jean Martin",
                },
                {
                    "text": "A strong clinical case helps, but the economic case decides whether it gets approved.",
                    "timestamp": "02:08",
                    "expert": "Anna Keller",
                },
                {
                    "text": "It matters, but the discussion is not always purely financial. Hospitals also consider patient outcomes, length of stay, surgeon recruitment and whether the technology improves their clinical position.",
                    "timestamp": "02:07",
                    "expert": "Dr. Emily Carter",
                },
            ],
        }
    elif any(k in q for k in ["timeline", "cycle", "long", "months"]):
        return {
            "covered": True,
            "answer": "Decision-making timelines range from 6 to 18 months across Europe. In France and the UK, purchasing typically takes 6 to 12 months (or 6 to 9 months in the UK if funding is already allocated). In Germany, the process is longer (9 to 18 months) because multiple internal committees—procurement, clinical chiefs, and management—must reach formal consensus. In all three markets, missing the capital budget window can postpone the purchase into the subsequent fiscal cycle.",
            "quotes": [
                {
                    "text": "Six to twelve months is realistic once the hospital becomes serious. It can be longer if the capital committee pushes the purchase into the next budget cycle.",
                    "timestamp": "06:08",
                    "expert": "Dr. Jean Martin",
                },
                {
                    "text": "Nine to eighteen months is common. Procurement, clinical leadership, finance and management all need to align, so it can move slowly.",
                    "timestamp": "06:05",
                    "expert": "Anna Keller",
                },
                {
                    "text": "Around six to nine months can happen if funding is already available. If the trust has to wait for a new capital cycle, it can take much longer.",
                    "timestamp": "05:04",
                    "expert": "Dr. Emily Carter",
                },
            ],
        }
    elif any(k in q for k in ["training", "staff", "surgeon", "skill"]):
        return {
            "covered": True,
            "answer": "All three experts agree that surgeon and staff training is essential to program viability. If only one surgeon is trained, machine utilization drops and the financial case fails. The UK expert notes that training capacity is a primary bottleneck alongside funding, while France and Germany stress that multiple trained surgeons are required from year one.",
            "quotes": [
                {
                    "text": "Training matters, especially in the first year. If only one surgeon can use the system, the economics become difficult. Hospitals want several surgeons trained so utilisation is high enough.",
                    "timestamp": "03:10",
                    "expert": "Dr. Jean Martin",
                },
                {
                    "text": "Very important operationally. If the hospital buys a system but only one surgeon is comfortable using it, utilisation will be poor. That weakens the business case.",
                    "timestamp": "03:05",
                    "expert": "Anna Keller",
                },
                {
                    "text": "The key point is that adoption is not just about buying the machine. Hospitals need enough trained people and enough procedure volume to make the programme sustainable.",
                    "timestamp": "06:04",
                    "expert": "Dr. Emily Carter",
                },
            ],
        }
    elif any(k in q for k in ["barrier", "hurdle", "holding", "obstacle", "slow"]):
        return {
            "covered": True,
            "answer": "The main barriers to robotic surgery adoption across Europe are high capital costs, institutional budget pressures, and the challenge of establishing sufficient case volumes. Additionally, the UK expert highlights training capacity for surgeons and operating theatre staff as a bottleneck that directly stalls adoption.",
            "quotes": [
                {
                    "text": "The biggest issue is still capital budget approval. Hospitals may like the technology clinically, but purchasing committees need a strong economic case before approving a system.",
                    "timestamp": "01:20",
                    "expert": "Dr. Jean Martin",
                },
                {
                    "text": "Cost is the first barrier. These are large capital purchases, and hospital finances are under pressure. The second issue is proving that the system will be used enough.",
                    "timestamp": "01:10",
                    "expert": "Anna Keller",
                },
                {
                    "text": "Funding is important, but I would say training capacity is just as important. You can buy a system, but if you cannot train enough surgeons and theatre staff, adoption stalls.",
                    "timestamp": "01:05",
                    "expert": "Dr. Emily Carter",
                },
            ],
        }
    elif any(k in q for k in ["adoption", "trend", "future", "forecast", "growth", "year"]):
        return {
            "covered": True,
            "answer": "Adoption is growing across all three markets, primarily led by large academic and university hospitals. Looking 3-5 years out, experts in France and the UK project up to 15-20% annual procedure growth in leading centers, whereas the German expert expects more measured high-single to low-double-digit growth due to competing capital priorities.",
            "quotes": [
                {
                    "text": "Adoption is growing, but it is still concentrated in larger academic hospitals and private centres with stronger capital budgets. Smaller regional hospitals are much slower.",
                    "timestamp": "00:18",
                    "expert": "Dr. Jean Martin",
                },
                {
                    "text": "I would expect continued growth, but probably closer to high single digits or low double digits in procedure volumes rather than something like 20 percent across the whole market.",
                    "timestamp": "05:08",
                    "expert": "Anna Keller",
                },
                {
                    "text": "I am quite positive. I think adoption could accelerate if training expands and systems become more cost competitive. I could see procedure growth above 15 percent annually in some areas.",
                    "timestamp": "04:06",
                    "expert": "Dr. Emily Carter",
                },
            ],
        }
    else:
        return {
            "covered": False,
            "answer": "",
            "quotes": [],
        }
