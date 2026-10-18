"""
Synthetic Trajectory Generator for Agentic Tool-Use
--------------------------------------------------
Generates multi-turn reasoning traces (Reason -> Action -> Observation) 
with intentionally injected edge cases (malformed JSON, missing args) 
to improve model robustness during SFT.
"""

import json
from typing import Dict, List, Any

class AgentTrajectorySynthesizer:
    def __init__(self, tools_schema: List[Dict[str, Any]]):
        self.tools = {tool["name"]: tool for tool in tools_schema}

    def generate_sample_trace(self, task_prompt: str, successful: bool = True) -> Dict[str, Any]:
        """Creates a structured training example with reasoning and tool call tags."""
        
        thought_process = "I need to fetch user data and filter active subscriptions."
        
        if successful:
            tool_call = {
                "name": "fetch_user_data",
                "arguments": {"user_id": "usr_994", "include_subs": True}
            }
            observation = '{"status": "success", "data": {"id": "usr_994", "active": true}}'
            final_answer = "The user's subscription is active and verified."
        else:
            # Injected edge case: missing required argument to train error recovery
            tool_call = {
                "name": "fetch_user_data",
                "arguments": {}  # Missing 'user_id'
            }
            observation = '{"error": "Missing required argument: user_id"}'
            final_answer = "I apologize, but I need the user ID to proceed."

        trace = {
            "prompt": task_prompt,
            "trajectory": [
                {"role": "assistant", "content": f"<thought>{thought_process}</thought>\n<tool_call>{json.dumps(tool_call)}</tool_call>"},
                {"role": "tool", "content": observation},
                {"role": "assistant", "content": f"<thought>Analyzing tool response...</thought>\n<final_answer>{final_answer}</final_answer>"}
            ]
        }
        return trace

if __name__ == "__main__":
    sample_tools = [{"name": "fetch_user_data", "parameters": ["user_id"]}]
    synthesizer = AgentTrajectorySynthesizer(sample_tools)
    print(json.dumps(synthesizer.generate_sample_trace("Verify user account"), indent=2))
