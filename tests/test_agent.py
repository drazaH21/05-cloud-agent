from src.agent import run_cloud_agent

def test_anthropic_agent():
    print("=== Initializing Anthropic Tool-Use Agent Test ===")
    query = "What is the status of the pnl_bridge right now?"
    
    response = run_cloud_agent(query)
    
    print("\n==========================================")
    print("TEST RESULT:")
    print(response)
    print("==========================================")

if __name__ == "__main__":
    test_anthropic_agent()
