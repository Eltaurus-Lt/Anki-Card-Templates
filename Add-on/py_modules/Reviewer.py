from aqt import gui_hooks, mw
import json

def embed_card_info(card):
    reviewer = mw.reviewer
    if not reviewer or not reviewer.web:
        return

    card_info = {
        "interval": card.ivl,
        "reviewCount": card.reps,
        "type": card.type # 0 = new, 1 = learning, 2 = review, 3 = relearning
    }
    # sm2
    if hasattr(card, "factor"):
        card_info["ease"] = card.factor
    # fsrs
    if hasattr(card, "memory_state"):
        if hasattr(card.memory_state, "difficulty"):
            card_info["difficulty"] = card.memory_state.difficulty 
        if hasattr(card.memory_state, "stability"): # 90% interval
            card_info["stability"] = card.memory_state.stability             
    reviewer.web.eval(f"""
            (()=>{{
                let scriptL = document.getElementById('lt-card-data');
                if (!scriptL) {{
                    scriptL = document.createElement("script");
                    scriptL.type = "application/json";
                    scriptL.id = 'lt-card-data';
                    document.head.appendChild(scriptL);
                }}
                scriptL.textContent = '{json.dumps(card_info)}';
            }})();
        """)

gui_hooks.reviewer_did_show_question.append(embed_card_info)