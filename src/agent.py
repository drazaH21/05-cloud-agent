import os
import json
from groq import Groq
from dotenv import load_dotenv
from src.tools import VERTEX_TOOLS, get_enterprise_metric

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_cloud_agent(prompt: str):
    print(f"\n[Groq Agent] Sending query: '{prompt}'")
    
    messages = [{"role": "user", "content": prompt}]
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": t["name"],
                "description": t["description"],
                "parameters": t["input_schema"]
            }
        }
        for t in VERTEX_TOOLS
    ]

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        tools=tools,
        tool_choice="auto",
        max_tokens=1024
    )

    response_message = response.choices[0].message
    messages.append(response_message)

    if response_message.tool_calls:
        for tool_call in response_message.tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            print(f"[Groq Agent] Tool requested: '{function_name}' with args: {function_args}")

            tool_result = ""
            if function_name == "get_enterprise_metric":
                tool_result = get_enterprise_metric(function_args.get("metric_name", ""))

            print(f"[Groq Agent] Tool execution result: {tool_result}")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": function_name,
                "content": tool_result
            })

        final_response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
            max_tokens=1024
        )
        return final_response.choices[0].message.content
    else:
        return response_message.content

if __name__ == "__main__":
    query = "Can you check the current status of the global_revenue_pipeline and summarize it?"
    result = run_cloud_agent(query)
    print("\n==========================================")
    print("AGENT FINAL RESPONSE:")
    print(result)
    print("==========================================")
